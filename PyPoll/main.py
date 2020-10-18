# Import required libraries
import os
import csv

# ------------- Definition of functions -------------
def export_result():
    # Create a text file to store result
    txt_path = os.path.join("PyPoll", "Analysis", "PP_Output.txt")
    
    with open(txt_path, "w") as result_file:
        # Assign the first result
        result1 = ("Election Results\n"
            "-------------------------\n"
            f"Total Votes: {total_votes}\n"
            "-------------------------"
            )
        
        # Print to terminal and write to file
        print(result1)
        result_file.write(result1 + "\n")
        
        # Loop to print/write all candidates' information as second result
        for candidate, votes in vote_list.items():
            # Calculate the percentage of votes for each candidate, also format to 0.000%
            percentage_votes = "{:.3f}".format(votes/total_votes * 100)
            result2 = (f"{candidate}: {percentage_votes}% ({votes})")

            # Print to terminal and write to file
            print(result2)
            result_file.write(result2 + "\n")

            # Get the name of winner with max of votes
            if votes == max(vote_list.values()):
                winner = candidate
        
        # Assign the third result
        result3 = ("-------------------------\n"
            f"Winner: {winner}\n"
            "-------------------------"
            )

        # Print to terminal and write to file
        print(result3)
        result_file.write(result3)

# ------------- End of definition of functions -------------

# Path of targeted csv in Resources folder
pypoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Main function to read csv file
with open(pypoll_csv, "r") as pp_file:
    # Get csv and move to 2nd line
    pp_csv = csv.reader(pp_file)
    next(pp_csv, None)
    
    # Create a dictionary for all candidates, 'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630
    vote_list = {}
    
    # Collecting candidate names and votes from csv
    for row in pp_csv:
        # If there is no candidate name in the dict, created a new key with vote value as 1
        # Or if there is existing candidate, vote value + 1
        if vote_list.get(row[2]) == None:
            vote_list[row[2]] = 1
        else:
            vote_list[row[2]] += 1
    
    # Get total votes from the values
    total_votes = sum(vote_list.values())

# Print and export result
export_result()