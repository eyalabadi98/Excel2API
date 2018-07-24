import pandas as pd
import glob
import os
import os.path
import numpy as np
import datetime
from numpy import nan as Nan
import requests
import random
from base64 import b64encode

API_ENDPOINT = "https://api.slicktext.com/v1/contacts/"

userAndPass = b64encode(b"****").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass }

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
allpeople = {}
teamShifts = {}
daysOfWeek = [None] * 7
totalshifts = {}
listofTeams = {}
firstTeam = list(df1)[0]
iterator = 0
allEmployees = {}

print "First Team "+ str(firstTeam)
current_team = str(firstTeam)
df1.append(pd.Series([Nan], index=["Unnamed: 2"]), ignore_index=True)
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
                # print "Current Team" + current_team
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
                    
                    # print " \nTotal Shifts up to team:" + str(totalshifts)
                    # print " \n Breaking! \n"
                    temp = {}
                    teamShifts = {}
                    continue
                # print "Day " + str(row[0]) +": "+ str(current_team)
                userbelongsto = ""
                group = {}
                shifts = {}
                for num,day in enumerate(row):
                    if not day == "Off" and not day == row[0]: 
                        # print "Num -1:"+ str(daysOfWeek[num-1]) + " Index: "+str(num)
                        # print "Days of Week " + str(daysOfWeek[0])
                       
                        allpeople[row[0]+ "" + str(iterator)] = group
                        # print "EveryGroup: " + str(everygroup[row[0]])
                        temp[daysOfWeek[num-1]] = day
                        teamShifts[row[0]] = temp
                        iterator +=1
                        # userbelongsto = "[" +userbelongsto + " & " + day + "]"
                        team = str(current_team).replace(" ", "")
                        teamNew = team.replace('"', '')
                        # print "Team is: " +teamNew
                        today = str(daysOfWeek[num-1]).replace(" ", "")
                        time = str(day).replace(" ", "")
                        userbelongsto = userbelongsto + "" + teamNew +"|"+ today + "|" + time + ","
                        # print "User Belongs: " +userbelongsto + "\n"
                        
                        # group[num] = str(current_team) + " | " +str(daysOfWeek[num-1]) + "|" + str(day) +" | " +str(userbelongsto)
                # callAPIforUser()
                # allpeople[row[0]] = userbelongsto
                
                #shifts[i] = userbelongsto
                if not allEmployees.get(row[0]):
                    print "User does not exist"
                    allEmployees[row[0]] = userbelongsto
                
                allEmployees[row[0]] = allEmployees[row[0]] + "," + userbelongsto
                print "\n User is " + row[0] + " Group is: " + str(userbelongsto)
                totalshifts[current_team] = teamShifts
                # daysOfWeek[0] = ""
                # teamShifts[row[0]] = daysOfWeek[0]
                # print "Current Team" + current_team
                # print row[0],row["Unnamed: 1"],row["Unnamed: 2"], row["Unnamed: 3"]
                #For each shift block   
# print "All Group: " + str(everygroup)
# print "\nTeamShifts: " + str(totalshifts)
for user in allEmployees:
    eachUser = allEmployees[user]
    print "\n Each user "+ user + ": " + eachUser
    x= eachUser.strip().split(",")
    print "\n x is " + str(x)
    group0 = ""
    group1 = ""
    group2 = ""
    group3 = ""
    group4 = ""
    try:
        if not x[0] == "" or not x[0] == None:
            group0= x[0]
        if not x[1] == "" or not x[1] == None:
            group1= x[1]
        if not x[2] == "" or not x[2] == None:
            group2= x[2]
        if not x[3] == "" or not x[3] == None:
            group3= x[3]
        if not x[4] == "" or not x[4] == None:
            group4= x[4]
    except:
        print "Ignore"
    

    print "Group 0 is:  "+ group0
    phoneNumFake = "34523443"+ str(random.randint(1,9)) + str(random.randint(1,9))
    print "Phone number : " + phoneNumFake
    data = {'action':"OPTIN",
        'textword':'1102413',
        'number':phoneNumFake,
        "firstName": row[0],
        'group0':group0,
        'group1':group1,
        'group2':group2,
        'group3':group3,
        'group0':group4,
    
        }
 
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data, headers=headers)
    
    # extracting response text 
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)


def print_dict(v, prefix=''):
    if isinstance(v, dict):
        for k, v2 in v.items():
            p2 = "{}['{}']".format(prefix, k)
            print_dict(v2, p2)
    elif isinstance(v, list):
        for i, v2 in enumerate(v):
            p2 = "{}[{}]".format(prefix, i)
            print_dict(v2, p2)
    else:
        print('{} = {}'.format(prefix, repr(v)))



df1.to_excel(file_name_schedule) #Write DateFrame back as Excel file