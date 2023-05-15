import os
import csv
csvpath = os.path.join(r"C:\Users\rajin\OneDrive\Desktop\UTA Assignments\Module-3 Challenge\python-challenge\pybank\Resources\budget_data.csv")
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total_months = []
    total_profit = []
    monthly_profit_changes = []
    
    for row in csvreader:
        'Calculating the Total number of months'
        total_months.append(row[0])

        'Calculating the net total of Profit/Losses'
        total_profit.append(int(row[1]))

        'Calculating the changes in "Profit/Losses" over the entire period, and then the average of those changes'
    for i in range(len(total_profit)-1):
        monthly_profit_changes.append(total_profit[i+1] - total_profit[i])
        avg_monthly_profit_changes = sum(monthly_profit_changes) / len(monthly_profit_changes)
        
    'Calculating the greatest increase in profits (date and amount) over the entire period'
    greatest_increase =  max(monthly_profit_changes)
    greatest_increase_month = monthly_profit_changes.index(greatest_increase) + 1
    
    'Calculating the greatest decrease in profits (date and amount) over the entire period'
    greatest_decrease =  min(monthly_profit_changes)
    greatest_decrease_month = monthly_profit_changes.index(greatest_decrease) + 1 

    print(f"Financial Analysis")
    print(f"----------------------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average Change: ${avg_monthly_profit_changes: .2f}")
    print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]}(${greatest_increase})")
    print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]}(${greatest_decrease})")

    'exporting results to a text file'
    txt_file = os.path.join(r"C:\Users\rajin\OneDrive\Desktop\UTA Assignments\Module-3 Challenge\python-challenge\pybank\Analysis\Financial_analysis_output.txt")
    with open(txt_file,"w") as newfile:
        newfile.write(f"Financial Analysis")
        newfile.write(f"----------------------------------")
        newfile.write(f"Total Months: {len(total_months)}")
        newfile.write(f"Total: ${sum(total_profit)}")
        newfile.write(f"Average Change: ${avg_monthly_profit_changes: .2f}")
        newfile.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${greatest_increase})")
        newfile.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${greatest_decrease})")
    





