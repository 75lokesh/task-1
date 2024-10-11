#Time-Series Plot for Close Price
plt.figure(figsize=(12, 6))
plt.plot(stock['timestamp'], stock['close'], label='Close Price', color='blue')
plt.xlabel('Time')
plt.ylabel('Close Price (USD)')
plt.title('Stock Close Price Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()

#High-Low Price Range Plot
plt.figure(figsize=(12, 6))
plt.plot(stock['timestamp'], stock['high'], label='High Price', color='green', alpha=0.7)
plt.plot(stock['timestamp'], stock['low'], label='Low Price', color='red', alpha=0.7)
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.title('Stock High and Low Prices Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()

#Volume Over Time
plt.figure(figsize=(12, 6))
plt.bar(stock['timestamp'], stock['volume'], color='orange', width=0.01)
plt.xlabel('Time')
plt.ylabel('Volume')
plt.title('Stock Trading Volume Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#Candlestick Chart
import mplfinance as mpf

# Prepare the data for candlestick chart
stock.set_index('timestamp', inplace=True)
mpf.plot(stock, type='candle', style='charles', title='Candlestick Chart', volume=True)