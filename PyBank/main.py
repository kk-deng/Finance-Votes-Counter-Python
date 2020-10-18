# Import required libraries
import os
import csv

# ------------- Definition of functions -------------
def avg_change(listname):
    # Get the mean by calculating sum/len, with round to 2 decimals
    return round((sum(listname)/len(listname)), 2)

def export_result():
    # Assign the export result summary
    result = ("Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {len(month_list)}\n"
        f"Total: ${sum(amount_list)}\n"
        f"Average Change: ${avg_change(change_list)}\n"
        f"Greatest Increase in Profits: {max_month} (${max_change})\n"
        f"Greatest Decrease in Profits: {min_month} (${min_change})")
    
    # Write result to PB_Output.txt file
    txt_path = os.path.join("PyBank", "Analysis", "PB_Output.txt")
    with open(txt_path, "w") as result_file:
        result_file.write(result)
    
    # Print out result to terminal
    print(result)
    print("----------------------------\n"
        "A result report was generated in " + result_file.name
        )

# ------------- End of definition of functions -------------


# Path of targeted csv in Resources folder
pybank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Main function to read csv file
with open(pybank_csv, "r") as pb_file:
    # Get csv and move to 2nd line
    pb_csv = csv.reader(pb_file)
    next(pb_csv, None)

    # Create empty lists for Months/Amount/Amount Change
    month_list = []
    amount_list = []
    change_list = []

    # Loop the csv file and add Months/Amount to the list
    for row in pb_csv:
        # Append month name to the list
        month_list.append(row[0])
        # Append integer amount to the list
        amount_list.append(int(row[1]))

    # Calculate the change of amount starting the 2nd month
    for i, amount in enumerate(amount_list):
        if i > 0:
            monthly_change = amount_list[i] - amount_list[i-1]
            change_list.append(monthly_change)
    
    # Zip two lists (month name + amount change, from 2nd month), 
    # also get max/min amount change values
    month_change_zipped = zip(month_list[1:], change_list)
    max_change = max(change_list)
    min_change = min(change_list)

    # Loop the zipped list, if the month has a value equals to max/min, record the months
    for (a, b) in month_change_zipped:
        if b == max_change:
            max_month = a
        elif b == min_change:
            min_month = a
    
# Print and export result
export_result()
