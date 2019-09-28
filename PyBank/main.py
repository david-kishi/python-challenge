import os
import csv

# Path to budget_data
csv_path = "budget_data.csv"

total_profit_loss = 0
total_months = 0
average_profit_loss = 0
greatest_profit = 0
greatest_loss = 0
greatest_profit_date = ""
greatest_loss_date = ""

# Opening CSV file
with open(csv_path, 'r') as csv_in:
    reader = csv.reader(csv_in, delimiter=',')
    header = next(reader)
    
    for row in reader:
        if total_months == 0:
            total_months += 1
            previous = int(row[1])
        else:
            # Count Number of Months
            total_months += 1

            # Calculate profit/loss
            difference = int(row[1]) - previous

            # Average profit/loss
            average_profit_loss += difference/2

            # Net total amount of Profit/Losses
            total_profit_loss += difference

            # Greatest Profit/Loss
            if difference > greatest_profit:
                greatest_profit = difference
                greatest_profit_date = row[0]
            elif difference < greatest_loss:
                greatest_loss = difference
                greatest_loss_date = row[0]

            previous = int(row[1])

# Output results to terminal
print(f"Total number of months: {total_months}")
print(f"Net Total Profit/Loss: {total_profit_loss}")
print(f"Average of Profit/Loss: {round(average_profit_loss,2)}")
print(f"Greatest Profit was {greatest_profit} on {greatest_profit_date}")
print(f"Greatest Loss was {greatest_loss} on {greatest_loss_date}")

# Output results to text file
with open ("output.txt", 'w') as out:
    out.write(f"Total number of months: {total_months}\n")
    out.write(f"Net Total Profit/Loss: {total_profit_loss}\n")
    out.write(f"Average of Profit/Loss: {round(average_profit_loss,2)}\n")
    out.write(f"Greatest Profit was {greatest_profit} on {greatest_profit_date}\n")
    out.write(f"Greatest Loss was {greatest_loss} on {greatest_loss_date}\n")

    
