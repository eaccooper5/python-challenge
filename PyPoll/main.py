import os
import csv
#import filepath
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
#open filepath 
#list of lines that go to the output text file
lines = []
txtpath = os.path.join("PyPoll", "analysis", "analysis_results.txt")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip headers
    csv_header = next(csvfile)
    #print header in analysis_results.txt
    print("""Election Results
----------------------------""")
    lines.append("""Election Results
----------------------------\n""")
    
    #find total number of votes
    total_votes = 0
    #create a dictionary to hold all of the info from csv file
    votesdic = {}

    for row in csvreader:
        #compile votes total (scan through list and tally votes)
        total_votes = total_votes+1
    
        #list of candidates who received votes
        name = row[2]
        #variable for total candidate votes
        candVotes = 0
        #keying name to running total
        if name in votesdic.keys():
            #pulling current count for given candidate name
            candVotes = votesdic[name]
        #tally number of votes per candidate by counting number of times name appears in file
        votesdic[name] = candVotes+1

    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    lines.append(f"Total Votes: {total_votes}\n")
    lines.append("-------------------------\n")

    #find vote breakdown for each candidate
    maxName = ""
    maxVotes = 0
    for (name,candVotes) in votesdic.items():
        #find percentage of votes for each candidate. Read as "CandPercent"
        candPCT = candVotes/total_votes
        #find winner
        if maxVotes < candVotes:
            maxVotes = candVotes
            maxName = name

        print(f"{name}: {candPCT*100:.03f}% ({candVotes})")
        lines.append(f"{name}: {candPCT*100:.03f}% ({candVotes})\n")
    print("-------------------------")
    lines.append("-------------------------\n")
    print(f"Winner: {maxName}")
    lines.append(f"Winner: {maxName}\n")
with open(txtpath,"w") as outfile:
    outfile.writelines(lines)
    