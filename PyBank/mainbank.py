# main.py
# #* Your task is to create a Python script that analyzes the records to calculate each of the following:


#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

import os
import csv


file= 'Resources/budget_data.csv'

with open(file, 'r') as csv_file:
    csvreader = csv.reader(csv_file,delimiter=",")
    header= next(csvreader)
    total_months= []
    total_profit=[]
    change=[]
    greatest_increase=['',0]
    greatest_decrease=['',0]
   
#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
    previous_profit=867884
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        difference= (int(row[1]))-previous_profit
        change.append(difference)
        previous_profit=int(row[1])
        num_months=len(total_months)
        profit_total=sum(total_profit)
        if difference > greatest_increase[1]:
            greatest_increase[1]= difference
            greatest_increase[0]= row[0]
        if difference < greatest_decrease[1]:
            greatest_decrease[1] = difference
            greatest_decrease[0]=row[0]

average_change=(sum(change))/(len(total_months))
print (f'Total months: {num_months}')
print (f'Total: ${profit_total}')
print (f'Average Change: {average_change}')
print (f'Greatest Increase in Profits: {greatest_increase}')
print (f'Greatest Decrease in Profits: {greatest_decrease}')

#   
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)