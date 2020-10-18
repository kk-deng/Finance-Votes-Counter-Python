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
An enumerate function was used to calculate the difference for monthly amount
```python
    for i, amount in enumerate(amount_list):
        if i > 0:
            monthly_change = amount_list[i] - amount_list[i-1]
            change_list.append(monthly_change)
```