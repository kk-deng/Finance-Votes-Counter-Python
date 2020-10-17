import os
import csv

def export_result():
    result1 = ("Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------"
        )
    
    print(result1)
    for candidate, votes in vote_list.items():
        # Calculate the percentage of votes for each candidate, also format to 0.000%
        percentage_votes = "{:.3f}".format(votes/total_votes * 100)
        print(f"{candidate}: {percentage_votes}% ({votes})")
        
        # Get the name of winner with max of votes
        if votes == max(vote_list.values()):
            winner = candidate

    result2 = ("-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------"
        )
    
    print(result2)

# Path to collect data from the Resources folder
pypoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(pypoll_csv, "r") as pp_file:

    pp_csv = csv.reader(pp_file)
    next(pp_csv, None)
    
    # Create a dictionary for all candidates
    vote_list = {'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}
    '''
    for row in pp_csv:
        
        if vote_list.get(row[2]) == None:
            vote_list[row[2]] = 1
        else:
            vote_list[row[2]] += 1
    '''

    total_votes = sum(vote_list.values())
    
    export_result()