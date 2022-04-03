# Import the csv module
import csv

# Define the path to the .csv file we want to read so the program knows where to look.
csvpath = 'PyPoll/Resources/election_data.csv'

# Set a variable to sum the total number of votes in our data set as we loop through each row. 
Total_Votes = 0
# Create a dictionary to add the names of candidates in our data set and the number of votes they received as we loop through each row in the data set. 
Unique_Candidates = {}

# Open the file referenced in the csvpath variable as 'read-only' and store its contents in a variable called csvfile.
with open(csvpath) as csvfile:
    # Specify the variable that holds the file's contents and the delimiter type to the csv.reader function.
    csvreader =csv.reader(csvfile, delimiter=',')
    # Skip the header row
    csvheader = next(csvreader)

    # Loop through each row after the header and...
    for row in csvreader:

        # Add one to our total votes counter (one row of data equals one vote).
        Total_Votes += 1

        # Set a variable 'candidate' equal to the value in the third column of the data set (the candidate)
        candidate = row[2]
        # While looping through the rows, if the candidate's name is not in our dictionary, add their name to the dictionary and add one to the value associated with their key in the dictionary. 
        if candidate not in Unique_Candidates:
            Unique_Candidates.update({candidate:0})
        # If their name is in the dictionary, then add one to the value associated with their name (key) in the dictionary. 
        Unique_Candidates[candidate] += 1

    # Create a list of the values in the Unique_Candidates dictionary. 
    list1 = list(Unique_Candidates.values())
    # Create a list of the keys (names) in the Unique_Candidates dictionary. 
    list2 = list(Unique_Candidates.keys())

    # Create an empty list to keep track of the percentage of votes each candidate received. We will add to this list as we loop through the number of votes each candidate received in list1. 
    Vote_Percentages = []

    # Loop through each value in list1 (the number of votes each candidiate received) and calculate the percentage of votes they received relative to the total votes cast. 
    for x in list1:
        percent = (x/Total_Votes)
        percentage = f"{percent:.3%}"
        Vote_Percentages.append(percentage)

    # Find the maximum value in list1. This value represents the highest number of votes for a candidate in our datea set. 
    Winner = max(list1)
    # Find the index location of the Winner value in the list1.
    Winner_Location = list1.index(Winner)
    # Find the name associated with the value of the Winner in list2 using its index location (Winner_Location).
    Winning_name = list2[Winner_Location]

# Store the name of our analysis ('Election Results') in the variable output_header, print it, and print a line that is the length of the output_header to act as a visual separator for the user.
output_header = 'Election Results:'
print(output_header)
print('-'*len(output_header))

# Print the Total Votes cast, a list of each candidate in our data set with the percentage of votes they received as well as the raw total of votes they received, and the winner of the election using f-strings and a for loop.
print(f'Total Votes: {Total_Votes}')
print('-'*len(output_header))
for candidate in range(len(list2)):
    print(f'{list2[candidate]}: {Vote_Percentages[candidate]} ({list1[candidate]})')
print('-'*len(output_header))
print(f'Winner: {Winning_name}')
print('-'*len(output_header))

# Define the path to the .txt file we want to write the output of our analysis to (Results.txt).
# outputpath = 'Analysis/Results.txt'

# Open the txt file referenced in the outputpath variable, with writing functionality, and save its contents in the outputfile variable.
output = open('PyPoll/Analysis/Results.txt','w')

# Define a variable 'lines1' that holds a list of the first section of data we want to add to this .txt file. 
lines1 = [str(output_header),
        str('-'*len(output_header)),
        str(f'Total Votes: {Total_Votes}'),
        str('-'*len(output_header))]

# For each line in the lines1 list, write the line in the .txt file then move to the next row to add the next line.
for line in lines1:
    output.write(line)
    output.write('\n')
    
# Have to separate out the for loop for writing the candidate's name, their percentage of votes won, and total votes. 
# For each candidate in the range of list2 (3 candidates), write the data specified in lines2 to the .txt file, then move to the next row to add the next line.
for candidate in range(len(list2)):
    lines2 = str(f'{list2[candidate]}: {Vote_Percentages[candidate]} ({list1[candidate]})')
    output.write(lines2)
    output.write('\n')

# Define a variable 'lines3' that holds a list of the last section of data we want to add to this .txt file.
lines3 = [str('-'*len(output_header)),
        str(f'Winner: {Winning_name}'),
        str('-'*len(output_header))]

# For each line in the lines3 list, write the line in the .txt file then move to the next row to add the next line.
for line in lines3:
    output.write(line)
    output.write('\n')