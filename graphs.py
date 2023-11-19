import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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

# Load your dataset
new_dataset = pd.read_csv('data/processed/standardized.csv')

# Scatter plot with regression line for 'State Median Income' vs 'NetWorth'
plt.figure(figsize=(8, 6))
sns.regplot(x='State Median Income', y='NetWorth', data=new_dataset, line_kws={"color":"red"})
plt.title('State Median Income vs Net Worth')
plt.xlabel('State Median Income')
plt.ylabel('Net Worth')
plt.show()
# Heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
corr_matrix = new_dataset[['NetWorth', 'State Median Income', 'DistrictMedInc', 'DW Nominate', 'WealthGrowthIndex']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()
# Residual plot for your regression model
# Assuming 'model' is your fitted regression model
residuals = model.resid
plt.figure(figsize=(8, 6))
plt.scatter(model.predict(), residuals)
plt.title('Residual Plot')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.axhline(y=0, color='red', linestyle='--')
plt.show()


# Scatter plot with regression line for 'State Median Income' vs 'NetWorth'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='State Median Income', y='NetWorth', data=new_dataset)
plt.title('Correlation between State Median Income and Net Worth')
plt.xlabel('State Median Income')
plt.ylabel('Net Worth')
plt.grid(True)
plt.show()