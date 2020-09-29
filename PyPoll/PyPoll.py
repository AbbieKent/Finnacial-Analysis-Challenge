# ## PyPoll

# ![Vote Counting](Images/Vote_counting.png)

# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
import  os
import csv

voting_file='Resources/election_data.csv'

with open(voting_file) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    total_votes=0
    candidates_list=[]
    percent_vote=[]
    percent=0
    votes_per_candidate=[]
#   * The winner of the election based on popular vote.
# * As an example, your analysis should look similar to the one below:
    header=next(csvreader) 
    for row in csvreader:
#   * The total number of votes cast
        total_votes= total_votes+1
#   * A complete list of candidates wh received votes
#   * The total number of votes each candidate won
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            index= candidates_list.index(row[2])
            votes_per_candidate.append(1)
        else:
            votes_per_candidate.count(row)
            index=candidates_list.index(row[2])
            votes_per_candidate[index] += 1
#   * The percentage of votes each candidate won
    for x in votes_per_candidate:
        percent=round((x/total_votes)*100)
        percent_vote.append(percent)
print(f'Election Results')
print (f'Total votes: {total_votes}')
print (f'{candidates_list[0]}: {percent_vote[0]}, {votes_per_candidate[0]}')
print (f'{candidates_list[1]}: {percent_vote[1]}, {votes_per_candidate[1]}')
print (f'{candidates_list[2]}: {percent_vote[2]}, {votes_per_candidate[2]}')
print (f'{candidates_list[3]}: {percent_vote[3]}, {votes_per_candidate[3]}')





#   ##text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.