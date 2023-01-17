# Importing dependencies 
import csv
import os

# Creating file path for budget_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')

# Opening and reading budget_data.csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    # storing the header row
    csv_header = next(csvfile)

    # creating lists for votes
    votes = []

    # looping through budget_data.csv
    for row in csvreader:
        votes.append(row[2])

    # creating list of candidates
    candidates = []
    for i in range(len(votes)):
        if votes[i] not in candidates:
            candidates.append(votes[i])

    # counting votes recieved by each candidate
    votes_recieved = []
    for i in range(len(candidates)):
        count = 0
        for j in range(len(votes)):
            if votes[j] == candidates[i]:
                count += 1
        votes_recieved.append(count)
    
    # calculating the percentage of votes each candidate recieved
    votes_percentage = []
    total = len(votes)
    for i in range(len(votes_recieved)):
        votes_percentage.append(round((votes_recieved[i]/total) * 100, 3))
    
    # finding the winer of the election 
    for i in range(len(votes_percentage)):
        if votes_percentage[i] > 50:
            winner = candidates[i]
            break
    




# Creating Analysis Text File
csvpath2 = os.path.join('analysis', 'analysis.txt')

with open(csvpath2, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('----------------------------\n')
    for i in range(len(candidates)):
        txtfile.write(f'{candidates[i]}: {votes_percentage[i]}% ({votes_recieved[i]})\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('----------------------------\n')