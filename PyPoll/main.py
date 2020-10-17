import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(pypoll_csv, "r") as pp_file:

    pp_csv = csv.reader(pp_file)
    next(pp_csv, None)
    
    # Create a list for all candidates
    vote_list = {'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}
    '''
    for row in pp_csv:
        
        if vote_list.get(row[2]) == None:
            vote_list[row[2]] = 1
        else:
            vote_list[row[2]] += 1
    '''

    total_votes = sum(vote_list.values())

    for candidate, votes in vote_list.items():
        percentage_votes = round(votes/total_votes * 100, 5)
        print(f"{candidate}: {percentage_votes}% ({votes})")
    