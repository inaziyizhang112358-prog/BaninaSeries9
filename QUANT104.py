import requests
from textblob import TextBlob
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time

class NewsBasedTradingAlgorithm:
    def __init__(self, ticker, api_key):
        self.ticker = ticker
        self.api_key = api_key
        self.sentiment_threshold = 0.1
        self.position = 0
        
    def fetch_news(self, sources=['cnn', 'bbc-news', 'the-new-york-times', 'the-wall-street-journal']):
        """Fetch news articles from NewsAPI"""
        url = f'https://newsapi.org/v2/everything?q={self.ticker}&sources={",".join(sources)}&apiKey={self.api_key}'
        try:
            response = requests.get(url)
            articles = response.json().get('articles', [])
            return articles
        except Exception as e:
            print(f"Error fetching news: {e}")
            return []
    
    def analyze_sentiment(self, articles):
        """Analyze sentiment of news articles"""
        sentiments = []
        for article in articles:
            text = f"{article.get('title', '')} {article.get('description', '')}"
            blob = TextBlob(text)
            sentiments.append(blob.sentiment.polarity)
        
        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
        return avg_sentiment
    
    def get_market_data(self):
        """Fetch current market data"""
        stock = yf.Ticker(self.ticker)
        data = stock.history(period='1d', interval='1m')
        return data
    
    def generate_signal(self, sentiment):
        """Generate trading signal based on sentiment"""
        if sentiment > self.sentiment_threshold:
            return 'BUY'
        elif sentiment < -self.sentiment_threshold:
            return 'SELL'
        else:
            return 'HOLD'
    
    def execute_trade(self, signal, current_price):
        """Simulate trade execution"""
        if signal == 'BUY' and self.position <= 0:
            print(f"BUY {self.ticker} at ${current_price:.2f}")
            self.position = 1
        elif signal == 'SELL' and self.position >= 0:
            print(f"SELL {self.ticker} at ${current_price:.2f}")
            self.position = -1
        else:
            print(f"HOLD {self.ticker} at ${current_price:.2f}")
    
    def run(self):
        """Main trading loop"""
        print(f"Starting trading algorithm for {self.ticker}")
        
        articles = self.fetch_news()
        if not articles:
            print("No articles found")
            return
        
        sentiment = self.analyze_sentiment(articles)
        print(f"Average Sentiment: {sentiment:.3f}")
        
        market_data = self.get_market_data()
        if market_data.empty:
            print("No market data available")
            return
        
        current_price = market_data['Close'].iloc[-1]
        signal = self.generate_signal(sentiment)
        
        print(f"Signal: {signal}")
        self.execute_trade(signal, current_price)

# Usage example
if __name__ == "__main__":
    API_KEY = "PKSXCV6HXJXFII6R22DQVKEKJ6"  # Get from https://newsapi.org
    # Shared symbols list (can be changed to control which tickers are processed)
    symbols = ["AAPL", "MSFT", "GOOGL"]

    for symbol in symbols:
        print(f"\n--- Running algorithm for {symbol} ---")
        algo = NewsBasedTradingAlgorithm(symbol, API_KEY)
        try:
            algo.run()
        except Exception as e:
            print(f"Error running algorithm for {symbol}: {e}")
        time.sleep(1)
