# Import the csv module
import csv

# Define the path to the .csv file we want to read so the program knows where to look.
csvpath = 'PyBank/Resources/budget_data.csv'

# Define variables- either lists to add to to keep track of the data from each row we loop through or numbers to add to with the value from the rows we loop through.
# This Total_Months list will keep track of all the months in the data set so we can then use the len function to count the total months in our data set.
Total_Months = []
# This Total_Months_Value variable will track the number of months so we can accurately calculate the average profit change. 
Total_Months_Value = 0
# This Monthly Change variable will keep track of the profit change between rows (months).
Monthly_Change = 0
# We have to set a Current Value variable so the monthly change variable is subtracting the profit in the row right above the current one, rather than from the first row for every loop. 
Current_Value = 0
# This Monthly_Profit list will keep track of the monthly profit changes for all the months in our data set. 
Monthly_Profit = []
# We have to set a Net_Profit_Loss variable so we can sum the profits each month and reach a net Profit/Loss for the time period at the conclusion of all loops.
Net_Profit_Loss = 0

# Open the file referenced in the csvpath variable as 'read-only' and store its contents in a variable called csvfile.
with open(csvpath, 'r') as csvfile:
    # Specify the variable that holds the file's contents and the delimiter type to the csv.reader function. 
    csvreader =csv.reader(csvfile, delimiter=',')
    # Skip the header row
    csvheader = next(csvreader)
    
    # Accurately set the first row so the program knows where to start calculating profit change
    row_one = next(csvreader)
    Total_Months_Value += 1
    Net_Profit_Loss += int(row_one[1])
    Current_Value = int(row_one[1])
    
    # Loop through each row after the header and...
    for row in csvreader:
        # Add the value in the first column (month) to the Total_Months list.
        Total_Months.append(row[0])
        #Calculate the monthly profit change as the value in the second column (profit) minus the current value.
        Monthly_Change = int(row[1]) - Current_Value
        # Add that profit change to the Monthly_Profit list.
        Monthly_Profit.append(Monthly_Change)
        # Reset the current value to equal the value in the second column of the current row (profit this month) so the Monthly_Change variable accurately calculates for each loop.
        Current_Value = int(row[1])
        # Add the current month's profit to the Net_Profit_Loss variable.
        Net_Profit_Loss = Net_Profit_Loss + int(row[1])
    
    # Count the number of months in the Total_Months list using the len function and add back the first row.
    Month_Count = len(Total_Months) + 1
    
    # Define a function for calculating the average Monthly_Profit.  
    def average(numbers):
        length = len(numbers)
        total = 0.0
        for number in numbers:
            total += number
        return total / length
    # Once the function is defined, pass in the Monthly_Profit list.
    Average_Monthly_ProfitChange = average(Monthly_Profit)
  
    # Find the maximum value in the Monthly_Profit list. This value represents the greatest profit increase in our data set. 
    Greatest_ProfitIncrease = max(Monthly_Profit)
    # Find the index location of the Greatest_ProfitIncrease value in the Monthly_Profit list.
    Increase_Location = Monthly_Profit.index(Greatest_ProfitIncrease)
    # Find the date associated with the value of the Greatest_ProfitIncrease in the Total_Months list using its index location (Increase_Location).
    Greatest_ProfitIncreaseDate = Total_Months[Increase_Location]

    # Find the minimum value in the Monthly_Profit list. This value represents the greatest profit decrease in our data set.
    Greatest_ProfitDecrease = min(Monthly_Profit)
    # Find the index location of the Greatest_ProfitDecrease value in the Monthly_Profit list.
    Decrease_Location = Monthly_Profit.index(Greatest_ProfitDecrease)
    # Find the date associated with the value of the Greatest_ProfitDecrease in the Total_Months list using its index location (Decrease_Location).
    Greatest_ProfitDecreaseDate = Total_Months[Decrease_Location]

# Store the name of our analysis ('Financial Analysis') in the variable output_header, print it, and print a line that is the length of the output_header to act as a visual separator for the user.
output_header = 'Financial Analysis:'
print(output_header)
print('-'*len(output_header))

# Print the total Total Months included in the data set, the Net Profit/Loss, the Average Monthly Change, and the Greatest Increase/Decrease months/values using f-strings. 
print(f'Total Months: {Month_Count}')
print(f'Net Profit/Loss: ${Net_Profit_Loss}')
print(f'Average Change: ${round(Average_Monthly_ProfitChange,2)}')
print(f'Greatest Increase in Profits: {Greatest_ProfitIncreaseDate} (${Greatest_ProfitIncrease})')
print(f'Greatest Decrease in Profits: {Greatest_ProfitDecreaseDate} (${Greatest_ProfitDecrease})')

# Open the txt file referenced in the output variable with writing functionality.
output = open('PyBank/Analysis/Analysis.txt','w')

# Define a variable 'lines' that holds a list of the data we want to add to this .txt file. 
lines = [str(output_header), 
        str('-'*len(output_header)), 
        str(f'Total Months: {Month_Count}'), 
        str(f'Net Profit/Loss: ${Net_Profit_Loss}'),
        str(f'Average Change: ${round(Average_Monthly_ProfitChange,2)}'), 
        str(f'Greatest Increase in Profits: {Greatest_ProfitIncreaseDate} (${Greatest_ProfitIncrease})'),
        str(f'Greatest Decrease in Profits: {Greatest_ProfitDecreaseDate} (${Greatest_ProfitDecrease})')]

# For each line in the lines list, write the line in the .txt file then move to the next row to add the next line. 
for line in lines:
    output.write(line)
    output.write('\n')