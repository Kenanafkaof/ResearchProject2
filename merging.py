import pandas as pd

# Load the OpenSecrets dataset
opensecrets_data_path = 'data/unprocessed/opensecrets.csv'  # Replace with the actual file path
opensecrets_data = pd.read_csv(opensecrets_data_path)
opensecrets_data.columns = opensecrets_data.columns.str.strip()


# Load the additional state median income dataset
additional_data_path = 'data/unprocessed/median_income.csv'  # Replace with the actual file path
additional_data = pd.read_csv(additional_data_path)

# Clean and transform the additional dataset
# Drop unnecessary header information
cleaned_additional_data = additional_data.drop([0, 1, 2])

# Rename columns
year_columns = ['1990', '2000', '2005', '2010', '2014', '2015', '2016', '2017', '2018']
cleaned_additional_data.columns = ['State'] + year_columns + ['Extra'] * (len(cleaned_additional_data.columns) - len(year_columns) - 1)

# Remove extra columns
cleaned_additional_data = cleaned_additional_data[['State'] + year_columns]

# Melt the DataFrame to long format
additional_data_long = pd.melt(cleaned_additional_data, id_vars=['State'], value_vars=year_columns, var_name='Year', value_name='MedianIncome')

# Clean the 'MedianIncome' column
additional_data_long['MedianIncome'] = additional_data_long['MedianIncome'].str.extract('(\d+,\d+|\d+)')[0]
additional_data_long['MedianIncome'] = additional_data_long['MedianIncome'].str.replace(',', '').astype(float)

# Convert 'Year' to integer in the additional dataset
additional_data_long['Year'] = additional_data_long['Year'].astype(int)

# Prepare the OpenSecrets dataset
# Convert 'Year' to integer
opensecrets_data['Year'] = opensecrets_data['Year'].astype(int)

# Merge the datasets
merged_dataset = pd.merge(opensecrets_data, additional_data_long, on=['State', 'Year'], how='left', suffixes=('', '_additional'))

# Display the merged dataset
merged_dataset.head()

# Save the merged dataset
merged_dataset.to_csv('data/processed/merged_dataset.csv', index=False)
