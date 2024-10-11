
#Daily Returns
stock['daily_return'] = stock['close'].pct_change() * 100
print(stock[['timestamp', 'daily_return']].head())

# Plot the daily returns
plt.figure(figsize=(10, 6))
plt.plot(stock['timestamp'], stock['daily_return'], label='Daily Returns', color='purple')
plt.xlabel('Time')
plt.ylabel('Daily Return (%)')
plt.title('Daily Stock Returns Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#Moving Averages
stock['20_day_MA'] = stock['close'].rolling(window=20).mean()
stock['50_day_MA'] = stock['close'].rolling(window=50).mean()

# Plot the moving averages
plt.figure(figsize=(10, 6))
plt.plot(stock['timestamp'], stock['close'], label='Close Price', color='blue')
plt.plot(stock['timestamp'], stock['20_day_MA'], label='20-Day Moving Average', color='orange')
plt.plot(stock['timestamp'], stock['50_day_MA'], label='50-Day Moving Average', color='green')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.title('Stock Price with Moving Averages')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()