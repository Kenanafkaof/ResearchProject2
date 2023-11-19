import statsmodels.api as sm
import pandas as pd

new_dataset = pd.read_csv('data/processed/standardized.csv')

# Preparing data for the multivariate regression
X = new_dataset[['State Median Income', 'DistrictMedInc', 'DW Nominate', 'WealthGrowthIndex']]  # Predictor variables
y = new_dataset['NetWorth']  # Dependent variable

# Adding a constant to the model (intercept)
X = sm.add_constant(X)

# Creating the regression model
model = sm.OLS(y, X, missing='drop').fit()

# Displaying the summary of the regression
print(model.summary())
