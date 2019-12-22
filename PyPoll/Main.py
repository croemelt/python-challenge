import os
import csv

# Link for file path
csvpath = os.path.join("Resources","election_data.csv")

# Define variables
voters = 0
# Create Lists
candidates = []
ind_candidate = []
vote_count = []
vote_percent = []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # For Loop for voter count and adding candidates to candidates list
    for row in csvreader:
        # Count the total number of votes
        voters = voters + 1
        # Setting candidate list
        candidates.append(row[2])
    # Second loop for getting each candiate, votes, and percent
    for i in set(candidates):
        ind_candidate.append(i)
        # Get to total votes per person
        p = candidates.count(i)
        vote_count.append(p)
        # Voter percentage calculation
        g = (p/voters)*100
        vote_percent.append(g)

    # Get winning vote count and winner    
    winning_vote_count = max(vote_count)
    winner = ind_candidate[vote_count.index(winning_vote_count)]
    
# Print statement to match formatting shown in instructions 
print(f'-------------------------')
print(f'Election Results')   
print(f'-------------------------')
print(f'Total Votes: {voters}')    
print(f'-------------------------')
for k in range(len(ind_candidate)):
            print(f'{ind_candidate[k]} :  {vote_percent[k]} % ( {vote_count[k]} )')
print(f'-------------------------')
print(f'The winner is: {winner}')
print(f'-------------------------')


with open('print_out.txt', 'w') as text:
    f'Election Results\n'
    f'---------------------------------------\n'
    f'Total Votes: {voters}\n'
    f'---------------------------------------\n"'
    for k in range(len(set(ind_candidate))):
        f'{ind_candidate[k]} :  {vote_percent[k]} % ( {vote_count[k]} )\n'
    f'---------------------------------------\n'
    f'The winner is: {winner}\n'
    f'-------------------------'