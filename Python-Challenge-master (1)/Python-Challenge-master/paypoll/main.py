
import os


import csv

csvpath = os.path.join('..', 'Python-Challenge-master (1)\\', 'election_data.csv')

csvreader = csv.reader(csvfile, delimiter=',')

print(csvreader)
csv_header = next(csvreader)
print(f"CSV Header: {csv_header}")
for row in csvreader:
    print(row)
    for row in csvreader: 
    
        total_votes +=1    
    if row[2] == "Khan": 
     khan_votes +=1
    elif row[2] == "Correy":
    correy_votes +=1
    elif row[2] == "Li": 
      li_votes +=1
    elif row[2] == "O'Tooley":
    otooley_votes +=1
    
    
    