
import pandas as pd
filecsvname = input("python-challeng-master(1)\\python-challenge-master\\pyroll")

                       
data = pd.read_csv(election_data.csv) 
                                    

Total = int(data.index.size)
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
    candidates = ["Khan", "Correy", "O'Tooley"] 
    votes = ("Khan_votes","Correy_votes","otooley_votes")
candidates_and_votes = dict(zip(candidates, votes)) 
key = max (dict_candidates_and_votes.get)
khan_percent = (khan_votes/total_votes)*100, 
correy_percent = (correy_votes/total_votes)*100, 
li_percent = (li_votes/ total_votes)*100, 
Otooley_percent = (Otooley_votes/total_votes)*100

print(f"election results")
print (f"total_votes:{total_votes}")
print(f"khan:{khan_percent:.3f}% ({khan_votes})") 
print (f"correy:{correy_percent:.3f}% ({correy_votes})") 
print(f"Li: {li_percent:.3f}% ({li_votes})") 
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})") 
print(f"Winner: {key}") 
output_file = Path("python-challenge(1)", "PayPoll", "Election_Results_Summary.txt")

candi_name = data["Candidate"].unique()
candi_name # get candidate name 
candi_count = data.groupby("Candidate")
candidate_count = candi_count.agg({'Voter ID':"count"})["Voter ID"].tolist()


candidate_winner = candi_count.agg({'Voter ID':"count"}).sort_values(by = "Voter ID", ascending=False )

print("-------------------------------------")
print("Winner : ", candidate_winner.index[0])

f = open("Output_analysis.txt" , "w")
f.write("Election Results"+ "\n")
f.write("Total Votes : "+ str(Total) + "\n")
f.write("-------------------------------------"+ "\n")
f.write(lst[0] + "\n")
f.write(lst[1] + "\n")
f.write(lst[2] + "\n")
f.write(lst[3] + "\n")
f.write("-------------------------------------" + "\n")
f.write("Winner : "+ candidate_winner.index[0] + "\n")
f.close()

    