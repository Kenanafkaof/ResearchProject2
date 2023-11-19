import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

new_dataset = pd.read_csv('data/processed/standardized.csv')
new_dataset_cleaned = new_dataset.dropna(subset=['State Median Income', 'DistrictMedInc', 'DW Nominate', 'WealthGrowthIndex'])

# Function to calculate VIF for each feature
def calculate_vif(df, features):
    # Adding a constant for intercept
    df = sm.add_constant(df[features])
    vifs = pd.DataFrame()
    vifs["Variable"] = df.columns
    vifs["VIF"] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
    return vifs

# Features for VIF calculation
features = ['State Median Income', 'DistrictMedInc', 'DW Nominate', 'WealthGrowthIndex']

# Calculating VIF
vif_data = calculate_vif(new_dataset_cleaned, features)

# Displaying VIF values
print(vif_data)
