# the data we need to retrieve:

# assign a variable for the file to load
# file_to_load = 'Resources/election_results.csv'
# with open(file_to_load) as election_data:
    #print(election_data)

# Add dependencies, use indirect method
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election_results file and read the file
with open(file_to_load) as election_data:
    #to do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # print each row
    #for row in file_reader:
        #print(row)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

# open the file to save results
##open(file_to_save, "w")
# use the open statement to open the file as a text file
#with open(file_to_save, "w") as txt_file:
    # write data to the file
    #txt_file.write("Hello World")
# close the file
#txt_file.close()

# write three counties to the txt_file
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the Election\n---------------------------------\nArapahoe\nDenver\nJefferson")
    






# 1. the total number of votes cast
# 2. a complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winer of the election based on popular votes