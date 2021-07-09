#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Add our dependencies
import csv
import os
#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to save the path to a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0 

#Declare a new list
candidate_options = []
#declare empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)

    #read the header row 
    headers = next(file_reader)
    
    #print each row in the CSV file 
    for row in file_reader:
        #add total vote count
        total_votes += 1

        #print(get) the candidate's name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
        
            #begin tracking that candidates vote count using dictionary_name[key] format
            candidate_votes[candidate_name] = 0
            
        #add a vote to that candidate's count
        candidate_votes[candidate_name] +=1 

    #print the total votes counted
    print(total_votes)

    #print the candidate list
    print(candidate_options) 

    #print the candidate vote dictionary
    print(candidate_votes)

#determine the % of votes for each candidate by looping through the counts
#iterate through the candidate list:
for candidate_name in candidate_votes:
    #retreive the vote count of a candidate
    votes = candidate_votes[candidate_name]
    #calculate the % of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #print out each candidate's name, vote count, and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}%, ({votes:,})\n")

    #determine winning vote count and candidate
    #determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning:count = votes and winning_percentage = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #and set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
    
    #print the candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the votes.")

winning_candidate_summary = (
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------\n")
print(winning_candidate_summary)




