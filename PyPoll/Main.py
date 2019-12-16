# import modules for Operating System and CSV Support
import os
import csv

# set file path
csvpath = os.path.join('Resources','election_data.csv')

print("Election Results")
print("--------------------------")

# opening csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header line
    next(csvfile)

    voter_count = sum(1 for row in csvreader)
    print(f'Total Votes: {voter_count}')

    print("--------------------------")