
# Import the required modules for open & read csv file
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Get the name and location of the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as budget_data_file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_data_file, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    #initialise variables & lists
    month_count = 0
    total_revenue = 0
    revenue_prev = 0
    revenue_change_list = []
    month_change_list = []
    
    # Read each row of data after the header
    for row in csvreader:
        
        # Count number of months and calculate total revenue
        month_count += 1
        total_revenue += int(row[1])
        
        # Initialise variables and starts working on the second row of data for calculating the revenue changes, as the first row has no change in profit/loss
        if revenue_prev == 0:
            revenue_diff = revenue_diff_total = revenue_diff_count = 0
        elif revenue_prev != 0:
            revenue_diff = int(row[1]) - revenue_prev
            revenue_diff_count += 1
            revenue_diff_total += revenue_diff
                       
            # Store revenue_diff and month_of_change into a lists
            revenue_change_list = revenue_change_list + [revenue_diff]
            month_change_list = month_change_list + [row[0]]
            
            # Zip merge lists together to form dictionary
            merged_list_dict = dict(zip(month_change_list, revenue_change_list))
       
        # Set current row value to revenue_prev
        revenue_prev = int(row[1])
    
# Get month of the greatest increase in profits
max_rev_mth = max(merged_list_dict, key = merged_list_dict.get)
# Get month of the greatest decrease in profits
min_rev_mth = min(merged_list_dict, key = merged_list_dict.get)

# Calculate average revenue changes
ave_diff = revenue_diff_total/(revenue_diff_count)


# Open and write to output Summary text file
with open('analysis/Summary.txt', "w") as text_file:
    text_file.writelines("Financial Analysis\n")
    text_file.writelines("----------------------------\n")
    text_file.writelines("\nTotal Months: %s" % month_count)
    text_file.writelines("\nTotal: %s" % "${:}".format(total_revenue))
    text_file.writelines("\nAverage Change: %s" % "${:.2f}".format(ave_diff))
    text_file.writelines("\nGreatest Increase in Profit: %s ($%s)" % (max_rev_mth, max(revenue_change_list)))
    text_file.writelines("\nGreatest Decrease in Profit: %s ($%s)" % (min_rev_mth, min(revenue_change_list)))
    # Close the output text file when writing is completed
    text_file.close()
    

# Print summary table to the console
print("\n")
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: " + str(month_count))
print(f"Total: " + "${:}".format(total_revenue))
print(f"Average Change: " + "${:.2f}".format(ave_diff))
print(f"Greatest Increase in Profit: " + max_rev_mth + " (" + "${:}".format(max(revenue_change_list)) + ") ")
print(f"Greatest Decrease in Profit: " + min_rev_mth + " (" + "${:}".format(min(revenue_change_list)) + ") ")
