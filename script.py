import pandas as pd
import glob
import os
import os.path
import numpy as np
import datetime
from numpy import nan as Nan

print "\nStarting \n"
lst = glob.glob("./schedule*")

print "Glob is "+ str(lst)
for element in lst:
    if os.path.isdir("./" +element[0]):
        print("Found a match " + element)
        os.rename(element,"schedule.xls")
print "Done with file change \n"



# file_name = "./American Directions Phone List.xls"
# df = pd.read_excel(file_name,skip_blank_lines=True) #Read Excel file as a DataFrame
# df['Pay Id'] = df["First"].map(str) +" " +df["Last"]
# #Display top 5 rows to check if everything looks good
# #df.head(5)
# df.to_excel(file_name) #Write DateFrame back as Excel file

## schedule_2018-06-24-to-2018-06-30 (1).xls
#Second workbook
formula = "=VLOOKUP(A5,'[American Directions Phone List.xls]Sheet1'!$B:$G,4,FALSE)"

file_name_schedule = "schedule.xls"
df1 = pd.read_excel(file_name_schedule, header=0) #Read Excel file as a DataFrame
print "Opened File \n"
#Display top 5 rows to check if everything looks good

# print "DF "+ str(df1)
teamShifts = {}
daysOfWeek = [None] * 7
totalshifts = {}
listofTeams = {}
firstTeam = list(df1)[0]
print "First Team "+ str(firstTeam)
current_team = str(firstTeam)
df1.append(pd.Series([Nan], index=["Unnamed: 2"]), ignore_index=True)
print "DF1 is" + str(df1)
for i,row in df1.iterrows():

    try:
        if row[0].startswith("Team"):
            print "Row 0 has a team: "+ row[0]
            current_team = row[0]
    except:
        print ""
        #  and not pd.isnull(df1.iloc[i,1])
    if not row[0] == np.datetime64('NaT')  and not row[0] == "Name":
        # print "First " + str(row[0])
        temp  = {}
        if True:
            if type(row["Unnamed: 2"]) == pd.Timestamp and not row[0] == "":

                dates = pd.to_datetime(row["Unnamed: 2"], format = '%Y%m%d')
                date = dates.strftime('%Y-%m-%d')
                print "Switching Teams" + current_team
                listofTeams[i] = current_team
                if row[0] == firstTeam:
                    print "First team  appeared\n"
                    teamShifts[0] = firstTeam
            
                # print "Time Found " + date + "\n" 
                print "Current Team" + current_team
                for number,day in enumerate(row):
                    
                    if number == 0:
                        continue
                    dates = pd.to_datetime(day, format = '%Y%m%d')
                    date = dates.strftime('%Y-%m-%d')
                    daysOfWeek[number-1] = date
                #print "Time " , row["Unnamed: 1"],row["Unnamed: 2"], row["Unnamed: 3"], "\n"
                # print "Days of Week "+ str(daysOfWeek)
            else:
                if pd.isnull(row[0]):
                    print "Adding into totalshift: "+ current_team + ": "+ str(teamShifts)
                    
                    print " \nTotal Shifts up to team:" + str(totalshifts)
                    print " \n Breaking! \n"
                    temp = {}
                    teamShifts = {}
                    continue
                print "Day " + str(row[0]) +": "+ str(current_team)
                for num,day in enumerate(row):
                    if not day == "Off" and not day == row[0]: 
                        # print "Num -1:"+ str(daysOfWeek[num-1]) + " Index: "+str(num)
                        # print "Days of Week " + str(daysOfWeek[0])
                        temp[daysOfWeek[num-1]] = day
                        teamShifts[row[0]] = temp
                totalshifts[current_team + "Eyal"] = teamShifts
                # daysOfWeek[0] = ""
                # teamShifts[row[0]] = daysOfWeek[0]
                # print "Current Team" + current_team
                # print row[0],row["Unnamed: 1"],row["Unnamed: 2"], row["Unnamed: 3"]
                #For each shift block   
print "\nTeamShifts: " + str(totalshifts)
df1.head(8)
df1.to_excel(file_name_schedule) #Write DateFrame back as Excel file