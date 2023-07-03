import pandas as pd
bank_df = pd.read_csv ('/Users/anisabraun/Documents/budget_data.csv')
bank_df.head()
#Count number of months

number_of_months=len(bank_df)

print("Total months: ",number_of_months)

net_total = bank_df['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
bank_df['Profit/Losses Change'] = bank_df['Profit/Losses'].shift(1) - bank_df['Profit/Losses']
average_change = bank_df['Profit/Losses Change'].mean()

# Find the greatest increase and decrease in profits
greatest_increase = bank_df['Profit/Losses Change'].max()
greatest_increase_date = bank_df.loc[bank_df['Profit/Losses Change'] == greatest_increase, 'Date'].iloc[0]
greatest_decrease = bank_df['Profit/Losses Change'].min()
greatest_decrease_date = bank_df.loc[bank_df['Profit/Losses Change'] == greatest_decrease, 'Date'].iloc[0]

# Print out the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")