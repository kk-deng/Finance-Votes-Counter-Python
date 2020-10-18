# Python Challenge - Analyze financial and voting records

*Built by Kelvin Deng*

## Pybank for financial records from a company. 

From the dataset we received, it has two columns: **Date** and **Profit/Losses**.
This python script analyzes the data and generates a financial report with the following info:

- [x] The total number of months included in the dataset
- [x] The net total amount of "Profit/Losses" over the entire period
- [x] The average of the changes in "Profit/Losses" over the entire period
- [x] The greatest increase in profits (date and amount) over the entire period
- [x] The greatest decrease in losses (date and amount) over the entire period

And the final report was printed on the python terminal and a text file in the Analysis folder:
```
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```

### Key features
An enumerate function was used to calculate the difference for monthly amount.
```python
for i, amount in enumerate(amount_list):
    if i > 0:
        monthly_change = amount_list[i] - amount_list[i-1]
        change_list.append(monthly_change)
```

A zipped list was used to get the months of min/max monthly change.
```python
month_change_zipped = zip(month_list[1:], change_list)
for (a, b) in month_change_zipped:
    if b == max_change:
        max_month = a
    elif b == min_change:
        min_month = a
```

Result summary was assigned to one variable to make export/print code concise without showing it twice.
```python
result = ("Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {len(month_list)}\n"
    f"Total: ${sum(amount_list)}\n"
    f"Average Change: ${avg_change(change_list)}\n"
    f"Greatest Increase in Profits: {max_month} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_change})")
```


## PyPoll for automated votes counting

A dataset with a large amount of voting data was given. This python script analyzes the **Candidate** name and **numbers of votes** to find out the winner and his percentage. The result includes:

- [x] The total number of votes cast
- [x] A complete list of candidates who received votes
- [x] The percentage of votes each candidate won
- [x] The total number of votes each candidate won
- [x] The winner of the election based on popular vote.

And the final report was printed on the python terminal and a text file in the Analysis folder:
```
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
```

### Key features
To use the dictionary.get method to find out if the dictionary has existing candidate name, if not, add a new one. Otherwise, add the vote number.
```python
for row in pp_csv:
    if vote_list.get(row[2]) == None:
        vote_list[row[2]] = 1
    else:
        vote_list[row[2]] += 1
```

A key/value for loop was used to reiterate the items in the candidate dictionary to write and print the voting result simultaneously.
```python
for candidate, votes in vote_list.items():
    # ...
    result2 = (f"{candidate}: {percentage_votes}% ({votes})")
    # ...
    if votes == max(vote_list.values()):
        winner = candidate
```

# Appreciation

Thank you so much for the help from **Piro** and **Laurel**.

by Kelvin