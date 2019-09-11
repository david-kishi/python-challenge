import os
import csv

# Path to the election data in this folder
csv_path = "election_data.csv"

# Dictionary is used to hold the count of votes for each candidate.
candidate_votes = {}

# Open CSV file to read
with open (csv_path, 'r') as csv_reader:
    read = csv.reader(csv_reader, delimiter=',')
    header = next(read)

    # for each row, check if candidate name is already in dictionary
    # if not, update dictionary
    # if exist, increment candidate's vote count in the dictionary
    for row in read:
        if row[2] in candidate_votes:
            candidate_votes.update({
                row[2]:(candidate_votes.get(row[2])+1)
            })
        else:
            candidate_votes.update({row[2]:1})

# Print out results
total_votes = sum(candidate_votes.values())
print(f"Total Number of Votes: {total_votes}")
print("Candidates\t# of Votes\t% Won")
for key, value in candidate_votes.items():
    print(f"{key}\t\t{value}\t\t{int((value*100)/total_votes)}")
print(f"The winner is {max(candidate_votes, key=candidate_votes.get)}!")

# Output results to text file
with open ("Results.txt", 'w') as out:
    out.write(f"Total Number of Votes: {total_votes}\n")
    out.write("Candidates\t# of Votes\t% Won\n")
    for key, value in candidate_votes.items():
        out.write(f"{key}\t\t{value}\t\t{int((value*100)/total_votes)}")
    out.write(f"The winner is {max(candidate_votes, key=candidate_votes.get)}!")
