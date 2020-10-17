import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(pypoll_csv, "r") as pp_file:

    pp_csv = csv.reader(pp_file)
    next(pp_csv, None)

    # Create a list for all candidates
    candidate_list = []
    for row in pp_csv:
        