import os
import csv

def month_count(listname):
    # Get the length of a list
    return len(listname)

def avg_change(listname):
    # Get the mean by calculating sum/len
    avg = sum(listname)/len(listname)
    # Round to 2 decimals
    return round(avg, 2)
    

# Path to collect data from the Resources folder
pybank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(pybank_csv, "r") as pb_file:
    pb_csv = csv.reader(pb_file)
    next(pb_csv, None)

    # Get the total month of the list
    month_list = []
    amount_list = []
    change_list = []
    for row in pb_csv:
        month_list.append(row[0])
        amount_list.append(int(row[1]))

    for i, amount in enumerate(amount_list):
        if i > 0:
            monthly_change = amount_list[i] - amount_list[i-1]
            change_list.append(monthly_change)
    
    max_row = change_list.index(max(change_list))
    min_row = change_list.index(min(change_list))
    max_month = month_list[max_row + 1]
    min_month = month_list[min_row + 1]
    
    #print(month_count(amount_list))
    #print(amount_list)
    print(sum(amount_list))
    print(avg_change(change_list))
    print(f"{max_month} ($ {max(change_list)} )")
    print(f"{min_month} ($ {min(change_list)} )")