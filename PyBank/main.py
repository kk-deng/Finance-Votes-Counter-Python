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

def print_screen():
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_count(month_list)}")
    print(f"Total: ${sum(amount_list)}")
    print(f"Average Change: ${avg_change(change_list)}")
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

def write_file():
    with open("Analysis/Output.txt", "w") as result_file:
        result_file.write("Financial Analysis")
        result_file.write("----------------------------")
        result_file.write(f"Total Months: {month_count(month_list)}")
        result_file.write(f"Total: ${sum(amount_list)}")
        result_file.write(f"Average Change: ${avg_change(change_list)}")
        result_file.write(f"Greatest Increase in Profits: {max_month} (${max_change})")
        result_file.write(f"Greatest Decrease in Profits: {min_month} (${min_change})")
    
    print("A result report was generated in " + result_file.name)



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
    
    month_change_zipped = zip(month_list[1:], change_list)
    max_change = max(change_list)
    min_change = min(change_list)
    
    for (a, b) in month_change_zipped:
        # If the monthly change equals to the max of the change list, get max month
        if b == max_change:
            max_month = a
        elif b == min_change:
            min_month = a
    
    print_screen()
    write_file()
