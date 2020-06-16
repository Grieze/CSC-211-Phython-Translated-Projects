import numpy as np
import pandas as pd
#Print the heading of our data table
print("Name\tEmpil\tExam1\tExam2\tExam3\tExam4\tExam5\tAverage\tLetter Grade")

#Pandas method of opening data file
filepath = "/Users/Aaron/Dropbox/CSC 211 Python Versions/Data.txt"
#set file as a database with all of their respective locations
file = pd.read_csv(filepath, delimiter= '\t', header = None)

#input each column with their respective variable
name = file.iloc[:][0]
empil = file.iloc[:][1]
exam1 = file.iloc[:][2]
exam2 = file.iloc[:][3]
exam3 = file.iloc[:][4]
exam4 = file.iloc[:][5]
exam5 = file.iloc[:][6]
i = 0
#create average and lettergrade variable
average = []
lettergrade = []
while i < name.size:
    average.append((exam1[i] + exam2[i] + exam3[i] + exam4[i] + exam5[i]) / 5)
    if (exam1[i] == 0 or exam2[i] == 0 or exam3[i] == 0 or exam4[i] == 0 or exam5[i] == 0):
        lettergrade.append('W')
    if (average[i] > 90):
        lettergrade.append('A')
    if (average[i] >= 80 and average[i]<90):
        lettergrade.append('B')
    if (average[i] >= 70 and average[i]<80):
        lettergrade.append('C')
    if (average[i] >= 65 and average[i]<70):
        lettergrade.append('D')
    if (average[i] < 65):
        lettergrade.append('F')
    i += 1
#loop was giving an error when I had the previous print statement in it
#reset i to 0
i = 0
#create new loop to print all the values out into a table
while i < name.size:
    print(name[i], '\t', empil[i], '\t', exam1[i], '\t', exam2[i], '\t', exam3[i], '\t',
          exam4[i], '\t', exam5[i], '\t', average[i], '\t', lettergrade[i])
    i += 1
