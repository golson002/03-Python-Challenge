# PyBank and PyPoll Python Exercises

## **Motivation/Reason for Analysis:**

The motivation for the analysis of the budget data in the PyBank exercise and the election data in the PyPoll exercise was to assess proficiency with Python and to understand my ability to use the programming language to evaluate large data sets and generate a concise and informative report about the data in a consumable/readable format.

* In the PyBank exercise, I took the position/perspective of someone in my company's accounting department looking to quickly analyze several years of financial records.
* In the PyPoll exercise, I took the position/perspective of an individual trying to help a small, rural town modernize its vote counting process.

## **Approach:**

I wrote two separate Python programs for the PyBank and PyPoll exercises. In both cases, I used the os and csv modules to read in the data sets. I then opened the csv files and with the files open, stored contents in variables, lists, and dictionaries and used addition assignment, for loops, f-strings, and function definition to generate my output reports.

In the PyBank exercise, my program reads through the 87 rows in the budget data set containing financial records for my company and outputs:

* The number of months recorded in the data set.
* The Net Profit/Loss over the time period of the data set.
* The change in profit/loss each month and the average of those changes.
* The month with the greatest increase in profit and the corresponding profit amount.
* The month with the greatest decrease in profit (loss) and the corresponding loss amount.

In the PyPoll exercise, my program reads through the 300,000+ rows in the election data set containing information about the candidates and their votes and outputs:

* The total number of votes cast in the election.
* A list of the candidate names, the number of votes they received, and the percentage of those votes relative to the total.
* The winner of the election.

## **Takeaways/Lessons Learned:**

* Python is a great tool for analyzing large data sets and I now understand why so many company's today use it to inform their decision making. In these exercises, I experienced the efficiency of the program and the addtional avenues/paths it offers for analyzing large data sets that, in some cases, make it a superior tool over Excel.

* Learning the syntax is a work in progress and takes time, as learning any new langauge does, but I found once I understood the foundational elements, I was able to build off of them to ultimately tell a story with the data (the essence of data analysis/science).

* Commenting out colloquial langauge or writing sentences on a notepad to make sense of what we want our program to do sometimes helps to inform how our syntax should read. This is a practice I will take into other modules of the course as we write programs in different langauges.

## **Further Analysis/Work:**

* The data sets used in this assignment were mostly stripped down and cleaned to only include the rows and columns of data we needed to generate output reports requested. I would be interested in getting some experience with other data sets that need to be cleaned before we can do the level of data analysis we did in this assignment. (Cleaning data in Python rather than Pandas, for example).

* Additionally, I would like to get more experience thinking through analysis requests similar to ones designed for this assignment because it is one thing to know the syntax/language and another to know how to apply it, when to use a list vs. a dictionary, when to define a function, etc. I know this will, of course, come with time though! :)