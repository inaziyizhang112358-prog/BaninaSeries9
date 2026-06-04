import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AlgorithmicTradingPlatform:
    def __init__(self, api_key, api_secret, base_url='https://paper-api.alpaca.markets/'):
        """Initialize the trading platform with Alpaca API credentials"""
        self.api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
        self.account = self.api.get_account()
        logging.info(f"Connected to Alpaca API. Account Status: {self.account.status}")
    
    def get_account_info(self):
        """Get current account information"""
        return {
            'buying_power': float(self.account.buying_power),
            'equity': float(self.account.equity),
            'cash': float(self.account.cash)
        }
    
    def get_positions(self):
        """Get all current positions"""
        return self.api.list_positions()
    
    def get_market_data(self, symbol, timeframe='1Min', limit=100):
        """Fetch historical market data for a symbol"""
        bars = self.api.get_bars(symbol, timeframe, limit=limit).df
        return bars
    
    def calculate_signals(self, data):
        """Calculate trading signals using moving average crossover strategy"""
        data['SMA_20'] = data['close'].rolling(window=20).mean()
        data['SMA_50'] = data['close'].rolling(window=50).mean()
        
        # Generate signals
        data['signal'] = 0
        data.loc[data['SMA_20'] > data['SMA_50'], 'signal'] = 1  # Buy
        data.loc[data['SMA_20'] < data['SMA_50'], 'signal'] = -1  # Sell
        
        return data
    
    def execute_trade(self, symbol, qty, side, order_type='market'):
        """Execute a trade order"""
        try:
            order = self.api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type=order_type,
                time_in_force='gtc'
            )
            logging.info(f"Order executed: {side} {qty} shares of {symbol}")
            return order
        except Exception as e:
            logging.error(f"Error executing trade: {e}")
            return None
    
    def run_strategy(self, symbols, check_interval=60):
        """Main trading loop"""
        logging.info("Starting trading strategy...")
        
        # If no symbols passed, use global `symbols` variable if defined
        if symbols is None:
            symbols = globals().get('symbols', ['AAPL', 'MSFT', 'GOOGL'])
        
        while True:
            try:
                for symbol in symbols:
                    # Get market data
                    data = self.get_market_data(symbol, timeframe='1Min', limit=100)
                    
                    # Calculate signals
                    data = self.calculate_signals(data)
                    current_signal = data['signal'].iloc[-1]
                    
                    # Check current position
                    try:
                        position = self.api.get_position(symbol)
                        current_qty = int(position.qty)
                    except:
                        current_qty = 0
                    
                    # Execute trades based on signals
                    if current_signal == 1 and current_qty <= 0:
                        # Buy signal
                        qty = 10  # Define your position size
                        self.execute_trade(symbol, qty, 'buy')
                    
                    elif current_signal == -1 and current_qty > 0:
                        # Sell signal
                        self.execute_trade(symbol, current_qty, 'sell')
                
                # Wait before next iteration
                time.sleep(check_interval)
                
            except KeyboardInterrupt:
                logging.info("Trading stopped by user")
                break
            except Exception as e:
                logging.error(f"Error in trading loop: {e}")
                time.sleep(check_interval)


# Example usage
if __name__ == "__main__":
    # Replace with your Alpaca API credentials
    API_KEY = 'PKN3DQVN7KSGY25PDCPE5QA2HK'
    API_SECRET = '3vBdan9JSasQavZ46uUjfZMpZ42KaAqTQF3Nsvp7PFFe'
    
    # Initialize platform
    platform = AlgorithmicTradingPlatform(API_KEY, API_SECRET)
    # Display account info
    account_info = platform.get_account_info()
    print(f"Account Info: {account_info}")
    
    # Define symbols to trade (will iterate and trade each symbol)
    # Shared symbols list (can be overridden by passing symbols into run_strategy)
    symbols = ['AAPL', 'MSFT', 'GOOGL']

    # Run the trading strategy for all symbols
    platform.run_strategy(symbols, check_interval=60)
