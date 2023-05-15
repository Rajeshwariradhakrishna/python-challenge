import os
import csv
csvpath = os.path.join(r"C:\Users\rajin\OneDrive\Desktop\UTA Assignments\Module-3 Challenge\python-challenge\pypoll\Resources\election_data.csv")
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total_votes = 0
    votes_for_charles = 0
    votes_for_diana = 0
    votes_for_raymon = 0
    votes_percentage_charles = 0
    votes_percentage_diana = 0
    votes_percentage_raymon = 0
    
    for row in csvreader:
        'Calculating total votes'
        total_votes += 1

        'The total number of votes each candidate won'
        if row[2] == "Charles Casper Stockham":
            votes_for_charles += 1  
            
        elif row[2] == "Diana DeGette":
            votes_for_diana += 1
            
        elif row[2] == "Raymon Anthony Doane":
            votes_for_raymon += 1
            
    'The percentage of votes each candidate won'
    votes_percentage_charles = (votes_for_charles/total_votes) *100
    votes_percentage_diana = (votes_for_diana/total_votes) *100
    votes_percentage_raymon = (votes_for_raymon/total_votes)*100
    
    'The winner of the election based on highest number of votes'
    candidates_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    total_votes_for_candidates_list = [votes_for_charles, votes_for_diana, votes_for_diana]
    dict1 = dict(zip(candidates_list, total_votes_for_candidates_list))
    winner = max(dict1, key = dict1.get)

    print(f"Election Results")
    print("---------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"Charles Casper Stockham: {votes_percentage_charles:.3f}% {votes_for_charles}")
    print(f"Diana DeGette: {votes_percentage_diana:.3f}% {votes_for_diana} ")
    print(f"Raymon Anthony Doane: {votes_percentage_raymon:.3f}% {votes_for_raymon}")
    print("---------------------------------")
    print(f"Winner: {winner}")
    print("---------------------------------")

    'exporting results to a text file'
    txt_file = os.path.join(r"C:\Users\rajin\OneDrive\Desktop\UTA Assignments\Module-3 Challenge\python-challenge\pypoll\Analysis\Election_Results_output.txt")
    with open(txt_file,"w") as newfile:
        newfile.write(f"Election Results")
        newfile.write(f"----------------------------------")
        newfile.write(f"Total Votes: {total_votes}")
        newfile.write(f"Charles Casper Stockham: {votes_percentage_charles:.3f}% {votes_for_charles}")
        newfile.write(f"Diana DeGette: {votes_percentage_diana:.3f}% {votes_for_diana} ")
        newfile.write(f"Raymon Anthony Doane: {votes_percentage_raymon:.3f}% {votes_for_raymon}")
        newfile.write("-----------------------------------")
        newfile.write(f"Winner: {winner}")
        newfile.write("-----------------------------------")
    