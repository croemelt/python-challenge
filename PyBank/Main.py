# import modules for Operating System and CSV Support
import os
import csv

# set file path
csvpath = os.path.join('Resources','budget_data.csv')

print("Financial Analysis")
print("--------------------------")

# opening csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header line
    next(csvfile)

    # month counter
    month_count = sum(1 for row in csvreader)
    print(f'Total Months: {month_count}')
    
    # total value
    total = 0
    for row in csv.reader(csvfile):
        total += int(row[1])
    print(f'Total: $ {total}')
    
    # total value different
    total_value = sum(int[2] for r in csv.reader(csvfile))
    print(f'Total: $ {total_value}')


    