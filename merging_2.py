import pandas as pd
from scipy.stats import zscore

# Load the dataset
merged_data_path = 'data/processed/merged_dataset.csv'
merged_dataset = pd.read_csv(merged_data_path)

# Function to calculate annual wealth change
def calculate_annual_wealth_change(df):
    # Sorting by Name and Year to ensure correct year-to-year comparison
    df = df.sort_values(by=['Name', 'Year'])
    # Calculating the yearly change in Net Worth
    df['YearlyChange'] = df.groupby('Name')['NetWorth'].diff().fillna(0)
    return df

# Applying the function to calculate annual wealth change
merged_dataset = calculate_annual_wealth_change(merged_dataset)

# Standardizing the wealth growth (Yearly Change) - using z-score for standardization
merged_dataset['WealthGrowthIndex'] = merged_dataset.groupby('Year')['YearlyChange'].transform(lambda x: zscore(x, nan_policy='omit'))

# Displaying the updated dataset with the Wealth Growth Index
merged_dataset[['Name', 'Year', 'NetWorth', 'YearlyChange', 'WealthGrowthIndex']].head()

# Saving the updated dataset
merged_dataset.to_csv('data/processed/merged_index.csv', index=False)