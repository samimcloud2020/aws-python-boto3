import pandas as pd
import numpy as np

# Create a sample sales dataset
data = {
    'Order_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Sales_Amount': [1200, 800, 300, 400, 1500, 900, 250, 450],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West']
}
df = pd.DataFrame(data)

# Use lambda to categorize Sales_Amount into Low, Medium, High
df['Sales_Category'] = df['Sales_Amount'].apply(
    lambda x: 'High' if x > 1000 else 'Medium' if x > 500 else 'Low'
)

# Use lambda to calculate a discounted sales amount (e.g., 10% off for High sales)
df['Discounted_Amount'] = df.apply(
    lambda row: row['Sales_Amount'] * 0.9 if row['Sales_Category'] == 'High' else row['Sales_Amount'],
    axis=1
)

# Group by Region and Sales_Category, then compute average sales
summary = df.groupby(['Region', 'Sales_Category']).agg({
    'Sales_Amount': 'mean',
    'Discounted_Amount': 'mean'
}).round(2)

# Display results
print("Original Data with New Columns:")
print(df)
print("\nSummary Statistics by Region and Sales Category:")
print(summary)

# Optional: Create a simple chart to visualize average sales by region and category
# Since you didn't explicitly ask for a chart, I'll skip it unless you confirm.
