# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
open_change = 0
close_change = 0
avg_change = 0
num_changes = 0
greatest_increase = ['date', 0]
greatest_decrease = ['date', 0]

# Open and read the csv
with open(file_to_load, encoding='utf-8') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    # print(f"{header}")

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    # print(f"{first_row}")

    # Track the total and net change
    total_net = total_net + int(first_row[1])
    first_open = int(first_row[1])
    open_change = int(first_row[1])
    # print(f"open_change {open_change}")

    # Process each row of data
    for row in reader:

        # Track the total
        total_net = total_net + int(row[1])

        # Track the net change, this will just keep grabbing value until last row
        close_change = int(row[1])  

        # Calculate the greatest increase in profits (month and amount)
        if int(greatest_increase[1]) < close_change - open_change:
            greatest_increase[0] = row[0]
            greatest_increase[1] = close_change - open_change

        # Calculate the greatest decrease in losses (month and amount)
        if int(greatest_decrease[1]) > close_change - open_change:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = close_change - open_change
        # Keep track of how many changes
        num_changes += 1
        # Calculate the average net change across the months
        # update average change before swaping old and new changes
        avg_change = (close_change - first_open) / num_changes
        #update close_change to current open_change
        open_change = close_change

# Generate the output summary
output = [
    "Financial Analysis\n",
    "-------------------------------------------------\n",
    "Total Months: " + str(num_changes + 1) + "\n",
    "Total: $" + str(total_net) + "\n",
    "Average Change: $" + str(round(avg_change, 2)) + "\n",
    "Greatest Increase in Profits: " + greatest_increase[0] + " ($"  + str(greatest_increase[1]) + ")\n",
    "Greatest Decrease in Profits: " + greatest_decrease[0] + " ($"  + str(greatest_decrease[1]) + ")\n"
]

# Print the output
for row in output:
    print(row)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.writelines(output)