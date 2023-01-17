# Importing dependencies 
import csv
import os

# Creating file path for budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Opening and reading budget_data.csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    # storing the header row
    csv_header = next(csvfile)

    # creating lists for dates and revenues
    dates = []
    rev = []

    # looping through budget_data.csv
    for row in csvreader:
        dates.append(row[0])
        rev.append(int(row[1]))

    # calculating the total months and net revenue
    months = len(dates)
    net = sum(rev)

    # looping through rev to create profit difference in between months
    difference = []
    for i in range(len(rev) - 1):
        difference.append(rev[i+1] - rev[i])

    # finding the average of difference 
    avg = round(sum(difference)/len(difference), 2)

    #fidning the greatest and lowest change and their months
    increase = difference[0]
    decrease = difference[0] 
    increase_month = 1
    decrease_month = 1
    for i in range(len(difference)):
        # greatest if-else statement 
        if difference[i] > increase:
            increase = difference[i]
            increase_month = i+1
        elif difference[i] < decrease:
            decrease = difference[i]
            decrease_month = i + 1

# Creating Analysis Text File
csvpath2 = os.path.join('analysis', 'analysis.txt')

with open(csvpath2, 'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Total Months: {months}\n')
    txtfile.write(f'Total: ${net}\n')
    txtfile.write(f'Average Change: ${avg}\n')
    txtfile.write(f'Greatest Increase in Profits: {dates[increase_month]} (${increase})\n')
    txtfile.write(f'Greatest Decrease in Profits: {dates[decrease_month]} (${decrease})\n')
