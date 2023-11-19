import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load your dataset
df = pd.read_csv('data/processed/standardized.csv')

selected_members = ['Nancy Pelosi', 'Mitch McConnell', 'Elizabeth Warren', 'Bernie Sanders', 'Alexandria Ocasio-Cortez', 'Rashida Tlaib', 'Rand Paul', 'Ted Cruz']
selected_members = [member.split(' ')[1] + ' ' + member.split(' ')[0] for member in selected_members]

# Filter the data for these members
filtered_data = df[df['Name'].isin(selected_members)]

# Create the plot with dual y-axes
plt.figure(figsize=(12, 8))
ax1 = plt.gca()  # get current axis

for member in selected_members:
    member_data = filtered_data[filtered_data['Name'] == member]
    sns.lineplot(x='Year', y='NetWorth', data=member_data, label=member, ax=ax1)

ax1.set_xlabel('Year')
ax1.set_ylabel('Net Worth')
ax1.legend(loc='upper left')

# Add a second y-axis for state median income
ax2 = ax1.twinx()
for member in selected_members:
    member_data = filtered_data[filtered_data['Name'] == member]
    sns.lineplot(x='Year', y='State Median Income', data=member_data, label=member, ax=ax2, linestyle="--")

ax2.set_ylabel('State Median Income')
ax2.legend(loc='upper right')

plt.title('Net Worth and State Median Income Trajectories of Selected Congressional Members')
plt.show()
