import os
import csv
#import filepath
csvpath = os.path.join("PyBank", "Resources","budget_data.csv")
#open filepath 
#list of lines that go to the output text file (borrowed from "main.py" in "PyPoll")
lines = []
txtpath = os.path.join("PyBank", "analysis", "analysis_results.txt")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip headers
    csv_header = next(csvfile)
    #print headers for testing
    print("""Financial Analysis
----------------------------""")
    lines.append("""Financial Analysis
----------------------------\n""")

#find how many months are in the dataset. 
#make a dictionary of each column.
    profit_loss_dictionary = {}
    for row in csvreader:
        profit_loss_dictionary[row[0]] = float(row[1])

#getting the length of the keys for the dictionary to count the number of date/month entries
    date_count = len(profit_loss_dictionary.keys())
    print(f"Total Months: {date_count}")
    lines.append(f"Total Months: {date_count}\n")
    
#find net total profit/losses over entire period. sum from values in second column of dictionary
    total_profit = sum(profit_loss_dictionary.values())
    #print with formatting ":.0f"
    print(f"Total: ${total_profit:.0f}")
    lines.append(f"Total: ${total_profit:.0f}\n")

    #create a list of the changes in profit/loss
    changelist = {}
    #creating a variable for previous value in the list
    previousVal = 0
    first = True
    for (k,v) in profit_loss_dictionary.items():
        if first:
            previousVal = v
            first = False
        else:

            #find the difference between current row's value and the previous
            dif = v-previousVal
            #creates a dictionary with date as the key
            changelist[k]=dif
            #keeps track of previous value
            previousVal = v
    

#find average change in profit/loss over entire period starting with the second value.
    totalCh = sum(changelist.values())
    averageCh = totalCh/(date_count-1)
    print(f"Average Change: ${averageCh:.2f}")
    lines.append(f"Average Change: ${averageCh:.2f}\n")

#find greatest increase in profit (with date and amount) over entire period
    max_date = (max(changelist, key=changelist.get))
    print(f"Greatest Increase in Profits: {max_date} (${changelist[max_date]:.0f})")
    lines.append(f"Greatest Increase in Profits: {max_date} (${changelist[max_date]:.0f})\n")

#find greatest decrease in profit (with date and amount) over entire period
    min_date = (min(changelist, key=changelist.get))
    print(f"Greatest Decrease in Profits: {min_date} (${changelist[min_date]:.0f})")
    #add line to analysis_results.txt
    lines.append(f"Greatest Decrease in Profits: {min_date} (${changelist[min_date]:.0f})\n")
with open(txtpath,"w") as outfile:
    outfile.writelines(lines)