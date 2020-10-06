import os
import csv

def month_count(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        #Count the months/rows of the csv
        return len(list(csvreader))

def total_amount(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        all_amount = 0
        for row in csvreader:
            all_amount += int(row[1])
        return all_amount

# Path to collect data from the Resources folder
pybank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

print(month_count(pybank_csv))

print(total_amount(pybank_csv))

