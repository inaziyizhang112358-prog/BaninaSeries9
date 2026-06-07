import json
from alpaca.data.live import NewsDataStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from transformers import pipeline

# --- 1. CONFIGURATION ---
# Replace with your actual Alpaca Keys (Paper Trading)
API_KEY = "PKQNZ6GJ67P4MFNEI5K3M7CSLX"
API_SECRET = "EHQEPSbHpuAajEQEL8WSUNvjx1ZzCmi6BApdB8PgML4C"

# Initialize Clients
trading_client = TradingClient(API_KEY, API_SECRET, paper=True)
news_stream = NewsDataStream(API_KEY, API_SECRET)

# Load Financial Sentiment Model (FinBERT)
# FinBERT is better than generic NLP for WSJ/NYT headlines
sentiment_analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")

# --- 2. THE TRADING LOGIC ---
async def handle_news(data):
    """
    This function runs every time a news headline is published.
    """
    headline = data.headline
    symbols = data.symbols  # Alpaca automatically tags symbols in the news
    
    if not symbols:
        return

    # Analyze Sentiment
    result = sentiment_analyzer(headline)[0]
    sentiment = result['label']
    confidence = result['score']

    print(f"[{data.created_at}] News for {symbols}: {headline} ({sentiment} - {confidence:.2f})")

    # High-Conviction Execution
    # Only trade if confidence > 0.90 (Competitive Factor: Alpha Decay Prevention)
    if confidence > 0.90:
        for symbol in symbols:
            side = None
            if sentiment == 'positive':
                side = OrderSide.BUY
            elif sentiment == 'negative':
                side = OrderSide.SELL

            if side:
                try:
                    order_data = MarketOrderRequest(
                        symbol=symbol,
                        qty=10,
                        side=side,
                        time_in_force=TimeInForce.GTC
                    )
                    trading_client.submit_order(order_data)
                    print(f"!!! TRADED {side} {symbol} based on news !!!")
                except Exception as e:
                    print(f"Order failed for {symbol}: {e}")

# --- 3. START STREAMING ---
if __name__ == "__main__":
    try:
        news_stream.subscribe_news(handle_news, "*") # Subscribe to all stock news
        news_stream.run()
    except Exception as e:
        print(f"Stream error: {e}")
        print("Closing stream...")
        try:
            news_stream.close()
        except:
            pass
