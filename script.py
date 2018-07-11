import pandas as pd
import glob
import os
import os.path
import numpy as np
import datetime

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

firstTeam = list(df1)[0]
print "First Team "+ str(firstTeam)
current_team = str(firstTeam)
for i,row in df1.iterrows():

    try:
        if row[0].startswith("Team"):
            print "Row 0 has a team: "+ row[0]
            current_team = row[0]
    except:
        print ""
    if not row[0] == np.datetime64('NaT') and not row[0] == "" and not pd.isnull(df1.iloc[i,1]) and not row[0] == "Name":
        # print "First " + str(row[0])
        if True:
            if type(row["Unnamed: 2"]) == pd.Timestamp:
                dates = pd.to_datetime(row["Unnamed: 2"], format = '%Y%m%d')
                date = dates.strftime('%Y-%m-%d')

                # print "Time Found " + date + "\n" 
                print "Current Team" + current_team
                for number,day in enumerate(row):
                    
                    if number == 0:
                        continue
                    dates = pd.to_datetime(day, format = '%Y%m%d')
                    date = dates.strftime('%Y-%m-%d')
                    print "Number "+ str(date)
                    daysOfWeek[number-1] = date
                #print "Time " , row["Unnamed: 1"],row["Unnamed: 2"], row["Unnamed: 3"], "\n"
                print "Days of Week "+ str(daysOfWeek)
            else:
                
                teamShifts[row[0]] = "Hello"
                print "Current Team" + current_team
                print row[0],row["Unnamed: 1"],row["Unnamed: 2"], row["Unnamed: 3"]
                #For each shift block   
        print "\n TeamShofts: "+ str(teamShifts)
        day
df1.head(8)
df1.to_excel(file_name_schedule) #Write DateFrame back as Excel file