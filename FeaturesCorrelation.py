#features like open, close, volume, and number_of_trades are related
correlation_matrix = stock[['open', 'high', 'low', 'close', 'volume']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Between Stock Features')
plt.show()