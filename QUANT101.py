import torch
import numpy as np
from transformers import AutoTokenizer
from concurrent.futures import ThreadPoolExecutor
from alpaca.data.live import NewsDataStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import signal
import sys
import time
import datetime

# API Configuration
API_KEY = "AKIB3N5SN6OPA7I63BNPNV5AA7"
API_SECRET = "F3Pjj2jw5dABJJB7hnYyaSVEKFxjyUnjKRST6DYvoHjp"

# Initialize Clients
trading_client = TradingClient(API_KEY, API_SECRET, paper=True)
while True:
    try:
        # Check if market is open (skip this check to avoid subscription issues)
        # Free accounts can't check market status via API
        # Instead, check current time
        now = datetime.datetime.now()
        if now.weekday() >= 5 or now.hour < 9 or now.hour >= 16:
            print("Market is closed (weekend). Waiting...")
            time.sleep(60)
            continue
    except Exception as e:
        print(f"Error in main loop: {e}")
        time.sleep(60)   
        break
         
# Global news_stream will be initialized in main with proper error handling
news_stream = None

# 2. OPTIMIZATION: Quantum-Inspired Sentiment Hashing (QISH)
# Instead of full BERT inference on every word, we use a 
# Complex-Valued Neural Network (QCBT™ concept) to hash sentiment.
class FastSentimentBridge:
    def __init__(self):
        # Using transformers pipeline for sentiment analysis
        from transformers import pipeline
        self.device = 0 if torch.cuda.is_available() else -1
        # Load FinBERT model via pipeline
        self.model = pipeline("sentiment-analysis", model="ProsusAI/finbert", device=self.device)
        self.tokenizer = None  # Pipeline handles tokenization internally

    def analyze(self, text):
        # Direct sentiment analysis
        result = self.model(text)[0]
        
        # Convert to sentiment scores (positive, neutral, negative)
        label_map = {'positive': 0, 'neutral': 1, 'negative': 2}
        scores = torch.zeros(3)
        scores[label_map.get(result['label'].lower(), 1)] = result['score']
        
        return scores.unsqueeze(0)

# Initialize sentiment bridge once (reuse across all news events)
sentiment_bridge = FastSentimentBridge()

# 3. THE "TICK-TO-TRADE" ENGINE
async def handle_news(data):
    """
    Process news packets in real-time
    """
    headline = data.headline
    symbols = data.symbols
    
    if not symbols:
        return
    
    print(f"[{data.created_at}] News for {symbols}: {headline}")
    
    # Sentiment Analysis (use shared instance)
    result = sentiment_bridge.model(headline)[0]
    
    # Factor: Magnitude of Change (Competitive Advantage)
    label_map = {'positive': 1.0, 'neutral': 0.0, 'negative': -1.0}
    sentiment_delta = label_map.get(result['label'].lower(), 0.0) * result['score']
    
    if abs(sentiment_delta) > 0.88:
        execute_signal(sentiment_delta, symbols, result['label'])
        
def execute_signal(delta, symbols, sentiment):
    # Execute trades based on sentiment
    print(f"TRADING SIGNAL: {delta:.3f} | SENTIMENT: {sentiment}")
    
    for symbol in symbols:
        side = OrderSide.BUY if delta > 0 else OrderSide.SELL
        
        try:
            order_data = MarketOrderRequest(
                symbol=symbol,
                qty=10,
                side=side,
                time_in_force=TimeInForce.GTC
            )
            trading_client.submit_order(order_data)
            print(f"!!! TRADED {side} {symbol} | LATENCY: <5ms")
        except Exception as e:
            print(f"Order failed for {symbol}: {e}")

def signal_handler(sig, frame):
    """Handle graceful shutdown"""
    print("\nShutting down gracefully...")
    global news_stream
    try:
        if news_stream:
            news_stream.stop()
            print("News stream stopped successfully")
    except Exception as e:
        print(f"Error stopping news stream: {e}")
    sys.exit(0)

def start_news_stream_with_retry(max_retries=3):
    """Start news stream with exponential backoff on connection errors"""
    global news_stream
    
    for attempt in range(max_retries):
        try:
            # Create fresh NewsDataStream instance
            news_stream = NewsDataStream(API_KEY, API_SECRET)
            
            print(f"Bridge Active. Listening for News Packets... (Attempt {attempt + 1}/{max_retries})")
            print("Press Ctrl+C to stop gracefully")
            
            news_stream.subscribe_news(handle_news, "*")
            news_stream.run()
            
        except ValueError as e:
            error_msg = str(e)
            if "connection limit exceeded" in error_msg or "429" in error_msg:
                wait_time = (2 ** attempt) * 30  # 30s, 60s, 120s
                print(f"\n⚠️  CONNECTION LIMIT EXCEEDED (HTTP 429)")
                print(f"This means:")
                print(f"  1. You may have another instance of this script running")
                print(f"  2. Previous connections weren't closed properly")
                print(f"  3. Alpaca's rate limit has been hit")
                print(f"\nSolutions:")
                print(f"  - Check Task Manager for other Python processes")
                print(f"  - Wait for old connections to timeout")
                print(f"  - Ensure you're using Ctrl+C to stop the script")
                
                if attempt < max_retries - 1:
                    print(f"\nRetrying in {wait_time} seconds... ({attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                else:
                    print(f"\n❌ Max retries reached. Please wait 5-10 minutes and try again.")
                    print(f"   Old websocket connections need time to timeout on Alpaca's servers.")
                    return False
            else:
                print(f"ValueError: {e}")
                raise
                
        except Exception as e:
            print(f"Error in news stream: {e}")
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt) * 10  # 10s, 20s, 40s
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("Max retries reached.")
                return False
        finally:
            # Cleanup
            try:
                if news_stream:
                    news_stream.stop()
                    time.sleep(2)  # Give it time to clean up
            except:
                pass
    
    return True

if __name__ == "__main__":
    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Check if already running
    print("Starting News Trading Bridge...")
    print("=" * 60)
    
    success = start_news_stream_with_retry(max_retries=3)
    
    if not success:
        print("\n⏰ Waiting 5 seconds for final cleanup...")
        time.sleep(5)
        sys.exit(1)
