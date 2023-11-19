import statsmodels.api as sm
import pandas as pd

merged_dataset = pd.read_csv('data/processed/merged_dataset.csv')

# Example: Predicting 'Net Worth' using 'State Median Income', 'District Median Income', and 'DW Nominate'
X = merged_dataset[['State Median Income', 'District Median Income', 'DW Nominate']]  # Predictor variables
y = merged_dataset['NetWorth']  # Dependent variable

# Adding a constant to the model (intercept)
X = sm.add_constant(X)

# Creating the regression model
model = sm.OLS(y, X, missing='drop').fit()

# Displaying the summary of the regression
print(model.summary())
