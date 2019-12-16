# import modules for Operating System and CSV Support
import os
import csv

#set file path
csvpath = os.path.join('Resources','budget_data.csv')

print("Financial Analysis")
print("--------------------------")

# opening csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    month_count = sum(1 for row in csvreader) - 1
    print(f'Total Months: {month_count}')

    total_value = sum(2 for row in csvreader)
    print(total_value)
    