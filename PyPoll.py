# the data we need to retrieve:
# 1. the total number of votes cast
# 2. a complete list of candidates who received votes
# 3. the total number of votes each candidate won
# 4. the percentage of votes each candidate won
# 5. the winner of the election based on popular votes

# Add dependencies, use indirect method
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total_votes counter
total_votes = 0

# declare candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# open the election_results file and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # print each row
    for row in file_reader:
        # Add to the total_votes count
        total_votes += 1
    #print(total_votes)
     # print the candidate name from each row
        candidate_name = row[2]
        # if the candidate doesn't match any existing candidate, add it to the list of candidates
        if candidate_name not in candidate_options:
            # add candidate name to candidate list
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # add votes to that candidate's count. Keep outside if statement so it can loop through rows with for statement
        candidate_votes[candidate_name] += 1

# add the results to the text file
with open(file_to_save, "w") as txt_file:
    # print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")
    print(election_results, end="")
    # Save final vote count to text file
    txt_file.write(election_results)


    #print(candidate_votes)

    # determine the percentage of votes per candidate by looping through the counts
    # iterate through the candidate list
    for candidate_name in candidate_votes:
        # retrieve vote count for a candidate with the variable vote using the key method
        vote = candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage = float(vote)/float(total_votes) * 100
        # create candidate_results variable: candidate name, vote count and % of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({vote:,})\n")
        # print each candidate, their votes and % on terminal
        print(candidate_results)
        # save candidate results to txt_file
        txt_file.write(candidate_results)
        # determine winning vote count and candidate
        # determine if the votes is gretater than the winning count
        if (vote > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = vote and winning_percent = vote_percentage
            winning_count = vote
            winning_percentage = vote_percentage
            # and set the winning candidate = candidate_name
            winning_candidate = candidate_name
    # print the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winnning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    # save winning candidate to txt_file
    txt_file.write(winning_candidate_summary)




       



# open the file to save results
# open(file_to_save, "w")
# use the open statement to open the file as a text file
#with open(file_to_save, "w") as txt_file:
    # write data to the file
    #txt_file.write("Hello World")
# close the file
#txt_file.close()

# write three counties to the txt_file
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the Election\n---------------------------------\nArapahoe\nDenver\nJefferson")
    






