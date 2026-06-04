import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import yfinance as yf

class CrossoverTradingBot:
    def __init__(self, api_key, api_secret, base_url='https://api.alpaca.markets', symbols=None):
        """Initialize the trading bot with Alpaca API credentials"""
        self.api = tradeapi.REST(api_key, api_secret, base_url)
        # Normalize symbols input:
        # - If `symbols` is None, try to use global `symbol` variable
        # - If a single string provided, convert to list
        # - If a list/tuple provided, use list
        if symbols is None:
            ext = globals().get('symbol', None)
            if ext is None:
                self.symbols = []
            elif isinstance(ext, str):
                self.symbols = [ext]
            elif isinstance(ext, (list, tuple)):
                self.symbols = list(ext)
            else:
                self.symbols = [str(ext)]
        elif isinstance(symbols, str):
            self.symbols = [symbols]
        elif isinstance(symbols, (list, tuple)):
            self.symbols = list(symbols)
        else:
            self.symbols = [str(symbols)]
        self.short_window = 20
        self.long_window = 50
        self.position_size = 0.95  # Use 95% of portfolio (allocated across symbols)
        
    def get_historical_data(self, symbol, days=100):
        """Fetch historical price data using yfinance (free, no subscription needed)"""
        # Use yfinance instead of Alpaca to avoid SIP data subscription requirements
        stock = yf.Ticker(symbol)
        df = stock.history(period=f"{days}d")
        
        # Rename columns to match Alpaca format
        df = df.rename(columns={
            'Open': 'open',
            'High': 'high', 
            'Low': 'low',
            'Close': 'close',
            'Volume': 'volume'
        })
        
        return df
    
    def calculate_signals(self, data):
        """Calculate moving average crossover signals"""
        data['SMA_short'] = data['close'].rolling(window=self.short_window).mean()
        data['SMA_long'] = data['close'].rolling(window=self.long_window).mean()
        
        # Generate signals
        data['signal'] = 0
        data.loc[data['SMA_short'] > data['SMA_long'], 'signal'] = 1
        data.loc[data['SMA_short'] < data['SMA_long'], 'signal'] = -1
        
        return data
    
    def get_position(self, symbol):
        """Check current position"""
        try:
            position = self.api.get_position(symbol)
            return int(position.qty)
        except:
            return 0
    
    def execute_trade(self, symbol, signal):
        """Execute buy/sell orders based on signals"""
        current_position = self.get_position(symbol)
        account = self.api.get_account()
        buying_power = float(account.buying_power)
        
        try:
            if signal == 1 and current_position <= 0:
                # Buy signal
                # Get current price using yfinance to avoid subscription issues
                stock = yf.Ticker(symbol)
                current_price = stock.info.get('currentPrice', stock.info.get('regularMarketPrice', 100))
                # Allocate buying power across all symbols
                num_symbols = max(1, len(self.symbols))
                buying_power_per_symbol = (buying_power * self.position_size) / num_symbols
                qty = int(buying_power_per_symbol / current_price)
                
                if qty > 0:
                    self.api.submit_order(
                        symbol=symbol,
                        qty=qty,
                        side='buy',
                        type='market',
                        time_in_force='gtc'
                    )
                    print(f"BUY ORDER: {qty} shares of {symbol}")
                    
            elif signal == -1 and current_position > 0:
                # Sell signal
                self.api.submit_order(
                    symbol=symbol,
                    qty=current_position,
                    side='sell',
                    type='market',
                    time_in_force='gtc'
                )
                print(f"SELL ORDER: {current_position} shares of {symbol}")
                
        except Exception as e:
            print(f"Error executing trade: {e}")
    
    def run(self):
        """Main trading loop"""
        print("Starting Crossover Trading Bot...")
        try:
            while True:
                try:
                    # Check if market is open (skip this check to avoid subscription issues)
                    # Free accounts can't check market status via API
                    # Instead, check current time
                    now = datetime.now()
                    if now.weekday() >= 5 or now.hour < 9 or now.hour >= 16:
                        print("Market is closed. Waiting...")
                        time.sleep(60)
                        continue

                    # Iterate each symbol and act on its signal
                    account = self.api.get_account()
                    buying_power = float(account.buying_power)
                    num_symbols = max(1, len(self.symbols)) if self.symbols else 1

                    for symbol in self.symbols:
                        data = self.get_historical_data(symbol)
                        data = self.calculate_signals(data)
                        latest_signal = data['signal'].iloc[-1]
                        if latest_signal != 0:
                            self.execute_trade(symbol, latest_signal)

                    # Wait before next iteration
                    print(f"Waiting 5 minutes before next check...")
                    time.sleep(300)

                except Exception as e:
                    # Log unexpected errors and continue loop
                    print(f"Error in main loop iteration: {e}")
                    try:
                        time.sleep(60)
                    except KeyboardInterrupt:
                        # allow outer handler to catch and exit
                        raise
        except KeyboardInterrupt:
            print("Shutdown request received; exiting.")
            return


if __name__ == "__main__":
    # Replace with your Alpaca API credentials
    API_KEY = "AKIB3N5SN6OPA7I63BNPNV5AA7"
    API_SECRET = "F3Pjj2jw5dABJJB7hnYyaSVEKFxjyUnjKRST6DYvoHjp"
    # Explicit symbols list (Option B): trade all listed symbols
    symbols = ['SPY', 'AAPL', 'MSFT', 'GOOGL']

    bot = CrossoverTradingBot(API_KEY, API_SECRET, symbols=symbols)
    try:
        bot.run()
    except KeyboardInterrupt:
        print("Received interrupt in main; exiting.")
