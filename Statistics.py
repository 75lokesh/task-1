#Descriptive Statistics
# Summary statistics for stock data
print(stock.describe())

# Correlation matrix for numeric columns
correlation = stock.corr()
print("Correlation Matrix:\n", correlation)

# Plotting the correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Stock Metrics')
plt.show()