import os
import csv

# Path to the election data in this folder
csv_path = "election_data.csv"

# Declare list to hold candidate names and dictionary to hold amount of votes
# List is used to hold candidate names as a new one is found.
# Dictionary is used to hold the count of votes for each candidate.
candidate_list = []
candidate_votes = {}
total_votes = 0

# Open CSV file to read
with open (csv_path, 'r') as csv_reader:
    read = csv.reader(csv_reader, delimiter=',')
    header = next(read)

    # for each row, check if candidate name is already in candidate_list
    # if not, add name to candidate list and update dictionary
    # if exist, increment candidate's vote count in the dictionary
    for row in read:
        if row[2] in candidate_list:
            total_votes += 1
            candidate_votes.update({
                row[2]:(candidate_votes.get(row[2])+1)
            })
        else:
            total_votes += 1
            candidate_list.append(row[2])
            candidate_votes.update({
                row[2]:0
            })

# Print out results
winner = candidate_list[0]
print(f"Total Number of Votes: {total_votes}")
print("Candidates\t# of Votes\t% Won")
for cand in candidate_list:
    print(f"{cand}\t\t{candidate_votes.get(cand)}\t\t{int((candidate_votes.get(cand)*100)/total_votes)}")

    # Determine winner by comparing votes
    if candidate_votes.get(cand) > candidate_votes.get(winner):
        winner = cand
print(f"The winner is {winner}!")

# Output results to text file
with open ("Results.txt", 'w') as out:
    out.write(f"Total Number of Votes: {total_votes}\n")
    out.write("Candidates\t# of Votes\t% Won\n")
    for cand in candidate_list:
        out.write(f"{cand}\t\t{candidate_votes.get(cand)}\t\t{int((candidate_votes.get(cand)*100)/total_votes)}\n")
    out.write(f"The winner is {winner}!\n")

