# Import the required modules to get file path, open and read csv file, and for working with hashable objects/values in the dictionary 
import csv
import os.path
from collections import Counter
from operator import itemgetter

# Get the name and location of the input csv file
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvreader:
    votes_count = -1
    # Count grand total votes for all candidates (excludes the header row)
    for row in csvreader:
        votes_count += 1
        
with open(csvpath) as csvreader:   
    # Read the header row first
    csv_header = next(csvreader)
    reader = csv.reader(csvreader)
    
    # Using collections Counter and operator itemgetter to count the number of votes for each candidate and store in the candidate_dict dictionary. The dictionary only stores their name and votes count
    candidate_dict = Counter(map(itemgetter(2), reader))
    
    # Get dictionary key (i.e. candidate name) and values (i.e. total of votes)
    dict_key_list = list(candidate_dict.keys())
    dict_val_list = list(candidate_dict.values())
    
    percent_list = []
    # Convert vote_count for each candidate in the dictionary to percentage, round up to the nearest value, format the number with % with 3 decimal places. Place it in percent_list.
    for i in range(0,len(candidate_dict)):
        percent_vote = dict_val_list[i] / (votes_count-1) * 100
        percent_vote = round(percent_vote) 
        percent_vote = "%.3f%%" % percent_vote 
        percent_list.append(percent_vote)

# Combined the required lists for later use
combined_list = list(zip(dict_key_list, dict_val_list, percent_list))


# Print summary to the console
print(f"\nElection Results")
print(f"-------------------------")
# Print grand total votes count (except the header row)
print(f"Total Votes: "  +  str(votes_count))
print(f"-------------------------")
# Print all candidates with their name, number of votes and %votes count
for i in range(0,len(candidate_dict)):
    print(f'{dict_key_list[i]}: {(percent_list[i])} ({dict_val_list[i]})')
print(f"-------------------------")
# Find the winner form the combined list by using using operator itemgetter
print(f'Winner: {max(combined_list, key=itemgetter(1))[0]}')
print(f"-------------------------")


# Open and write to output Summary.txt text file
with open('analysis/Summary.txt', "w") as text_file:
    text_file.writelines("Election Results\n")
    text_file.writelines("----------------------------\n")
    # Print grand total votes count (except the header row)
    text_file.writelines("Total Votes: "  +  str(votes_count))
    text_file.writelines("\n----------------------------\n")
    # Print all candidates with their name, number of votes and %votes count
    for i in range(0,len(candidate_dict)):
        text_file.writelines(dict_key_list[i] + ": " + str(percent_list[i]) + " (" + str(dict_val_list[i]) + ")" + "\n")
    text_file.writelines("----------------------------\n")
    # Find the winner form the combined list by using operator itemgetter
    text_file.writelines("Winner: " + max(combined_list, key=itemgetter(1))[0] + "\n")
    text_file.writelines("----------------------------\n")
    # Close the output text file when writing is completed
    text_file.close()