import os
import csv

# link file path
csvpath = os.path.join("Resources","budget_data.csv")

# define variables 
months = 0
total_profit = 0
profit_change = 0
starting_amount = 0

# Create lists 
profit = []
monthly_value = []
dates = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip header row
    csv_header = next(csvreader)

    # for loop
    for row in csvreader:    
      # Month Counter
      months = months + 1 

      # Will need it when collecting the greatest increase and decrease in profits
      dates.append(row[0])

      # Calculating total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      # Calculate average chnage
      final_profit = int(row[1])
      monthly_change_profits = final_profit - starting_amount

      # append month list
      monthly_value.append(monthly_change_profits)

      profit_change = profit_change + monthly_change_profits
      starting_amount = final_profit

      # Average profit calculation
      average_change = (profit_change/months)
      
      # Tracing back to min/max corresponding values
      greatest_increase = max(monthly_value)
      greatest_decrease = min(monthly_value)

      increase_date = dates[monthly_value.index(greatest_increase)]
      decrease_date = dates[monthly_value.index(greatest_decrease)]

# Print statement to match formatting shown in instructions  
print(f'-----------------------------------------------------')
print(f'Financial Analysis')
print(f'-----------------------------------------------------')
print(f'Total Months: {months}')
print(f'Total Profits: $ {total_profit}')
print(f'Average Change: ${int(average_change)}')
print(f'Greatest Increase in Profits: {increase_date} $ {greatest_increase}')
print(f'Greatest Increase in Profits: {decrease_date} $ {greatest_decrease}')
print(f'-----------------------------------------------------')

# Define state to be included in output text file
print_out = (
    f'-----------------------------------------------------\n'
    f'Financial Analysis\n'
    f'-----------------------------------------------------\n'
    f'Total Months: {months}\n'
    f'Total Profits: $ {total_profit}\n'
    f'Average Change: ${int(average_change)}\n'
    f'Greatest Increase in Profits: {increase_date} $ {greatest_increase}\n'
    f'Greatest Increase in Profits: {decrease_date} $ {greatest_decrease}\n'
    f'-----------------------------------------------------')
with open('print_out.txt', 'w') as text:
    text.write(print_out)
    