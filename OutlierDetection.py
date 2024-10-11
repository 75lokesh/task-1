#Using Z-Scores
from scipy.stats import zscore

# Calculate Z-scores for volume and close prices
stock['volume_zscore'] = zscore(stock['volume'])
stock['close_zscore'] = zscore(stock['close'])

# Define a threshold for considering an outlier (e.g., Z-score > 3 or < -3)
threshold = 3

# Find rows where volume or close price has a Z-score above the threshold
volume_outliers = stock[stock['volume_zscore'].abs() > threshold]
price_outliers = stock[stock['close_zscore'].abs() > threshold]

print("Volume Outliers:\n", volume_outliers)
print("Price Outliers:\n", price_outliers)

#Boxplot to Detect Outliers
# Boxplot for volume
plt.figure(figsize=(10, 6))
sns.boxplot(stock['volume'])
plt.title('Volume Outliers Detection')
plt.show()

# Boxplot for closing prices
plt.figure(figsize=(10, 6))
sns.boxplot(stock['close'])
plt.title('Close Price Outliers Detection')
plt.show()