import os
import csv
'''
def month_count(filepath):
    return sum(1 for row in )
'''

# Path to collect data from the Resources folder
pybank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    #Count the months/rows of the csv
    total_months = sum(1 for row in csvreader)
    print(total_months)
    print(csvreader)
    total_amount = 0
    for month in csvreader:
        print(int(month[1]))