# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []
candidate_dict = {}

# Winning Candidate and Winning Count Tracker
winner = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        # See README for reason why this is commented out.
        # print(". ", end="") 

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            # enter first vote into dictionary
            candidate_dict[candidate] = 1 
        # Else already in list, just need to count vote
        else: 
            candidate_dict[candidate] = candidate_dict[candidate] + 1        

# Generate the beginning of the output summary
output = [
    "Election Results\n",
    "-------------------------------\n",
    "Total Votes: " + str(total_votes) + "\n",
    "-------------------------------\n"
]

# Loop through the candidates to determine vote percentages and identify the winner
for i in range(len(candidate_list)):
    # Get the vote count and calculate the percentage
    output.append(str(candidate_list[i]) + ": " + str(round(candidate_dict[candidate_list[i]]/total_votes*100,3)) + "% " + "(" + str(candidate_dict[candidate_list[i]]) + ")" + "\n")

# formatting for output file.
output.append("-------------------------------\n")

# Generate winning candidate summary    
for i in range(len(candidate_list)):
    if candidate_dict[candidate_list[i]] > winning_count: # new winner
        winner = candidate_list[i]
        winning_count = candidate_dict[candidate_list[i]]

# Save the winning candidate summary to output
output.append(f"Winner: {winner}\n")
output.append(f"-------------------------------\n")

# Print output to terminal
for row in output:  
    print(row)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.writelines(output)