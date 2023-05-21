import sqlite3
import os
import sys
import re

""" Sample
database = os.getcwd() + "/../dillbickle"
print(database)
db = sqlite3.connect(database)
c = db.cursor()
c.execute("create table if not exists login(username text primary key, password text not null);")
c.execute("insert into login values('hello', 'there')")
db.commit()
db.close()
"""

basePath = sys.path[0]
database = basePath + "/dillbickle"
csvFolder = basePath + "/csvs"
print(sys.path)

def colsString(listy): #Method for turning columns into a string to build a table
    string = ""
    for item in listy:
        string += f'\"{item}\" text'
        if (item != listy[-1]):
            string += ", "
    return string

def splitSplit( source, splitter):
    lst = []
    word = ""
    quoting = False
    for i in range(len(source)):
        if (source[i] == '"'):
            quoting = not quoting
            continue
        if (not quoting and (source[i] != ',')):
            word += source[i]
        elif (not quoting and (source[i] == ',')):
            lst.append(word)
            word = ''
        elif (quoting):
            word += source[i]
    if (len(word) > 0):
        lst.append(word)
    return lst

states = {
    "ALABAMA":"AL",
    "ALASKA": "AK",
    "ARIZONA": "AZ",
    "ARKANSAS": "AR",
    "CALIFORNIA": "CA",
    "COLORADO": "CO",
    "CONNECTICUT": "CT",
    "DELAWARE": "DE",
    "DISTRICT OF COLUMBIA": "DC",
    "FLORIDA": "FL",
    "GEORGIA": "GA",
    "HAWAII": "HI",
    "IDAHO": "ID",
    "ILLINOIS": "IL",
    "INDIANA": "IN",
    "IOWA": "IA",
    "KANSAS": "KS",
    "KENTUCKY": "KY",
    "LOUISIANA": "LA",
    "MAINE": "ME",
    "MARYLAND": "MD",
    "MASSACHUSETTS": "MA",
    "MICHIGAN": "MI",
    "MINNESOTA": "MN",
    "MISSISSIPPI": "MS",
    "MISSOURI": "MO",
    "MONTANA": "MT",
    "NEBRASKA": "NE",
    "NEVADA": "NV",
    "NEW HAMPSHIRE": "NH",
    "NEW JERSEY": "NJ",
    "NEW MEXICO": "NM",
    "NEW YORK": "NY",
    "NORTH CAROLINA": "NC",
    "NORTH DAKOTA": "ND",
    "OHIO": "OH",
    "OKLAHOMA": "OK",
    "OREGON": "OR",
    "PENNSYLVANIA": "PA",
    "RHODE ISLAND": "RI",
    "SOUTH CAROLINA": "SC",
    "SOUTH DAKOTA": "SD",
    "TENNESSEE": "TN", 
    "TEXAS": "TX",
    "UTAH": "UT",
    "VERMONT": "VT",
    "VIRGINIA": "VA",
    "WASHINGTON": "WA",
    "WEST VIRGINIA": "WV",
    "WISCONSIN": "WI",
    "WYOMING": "WY"
}

def loadElection():

# Setting up database interaction
    db = sqlite3.connect(database)
    c = db.cursor()

# Loading up the csv
    read = open(csvFolder + "/countypres_2000-2020.csv", "r")
    full = read.readlines()
#print(full)
# Creating the table based on the first row of the csv
    cols = full[0].strip().split(",")
    print(cols)
# print(colsString(cols))
    c.execute("create table if not exists ElectionResults2020(" + colsString(cols) + ");" )


# Checking if the table is empty
    c.execute("select * from ElectionResults2020")
    empty = c.fetchone()
#print(empty)
    if (empty == None):
        for row in full:
            if( row[0:4] == "2020"):
                line = row.strip().split(",")
#print(line)
                cmd = "insert into ElectionResults2020 values(?" + (", ?" *(len(line) - 1)) + ");"
#print(cmd)
                c.execute(cmd, tuple(line))

    db.commit()
    db.close()


def countyVoting(state, county): # Given a state and county, return the voting results of the election there
    db = sqlite3.connect(database)
    c = db.cursor()

    cmd = "select candidate, party, candidatevotes from ElectionResults2020 where state=? and county_name=?;"
    c.execute(cmd,(state, county))

    results = c.fetchall()
    if (results != None):
        db.commit()
        db.close()
        return results
    else:
        return "Give real county"

    db.commit()
    db.close()

def getCounties(): #Return a list of all counties with their state
    db = sqlite3.connect(database)
    c = db.cursor()

    lst = []
    c.execute("select state, county_name from ElectionResults2020")
    results = c.fetchall()
    for county in results:
        if (len(lst) == 0 or lst[-1] != county):
            lst.append(county)

    db.commit()
    db.close()
    return lst

def getCandidates(): #Get a list of all people who participated in the election
    return [('Joe Biden',), ('Donald J Trump',), ('Jo Jorgensen',), ('Howie Hawkins',), (' Write-ins',), ('Gloria La Riva',), ('Brock Pierce',), ('Rocky De La Fuente',), ('Don Blankenship',), ('Kanye West',), ('Brian Carroll',), ('Ricki Sue King',), ('Jade Simmons',), ('President Boddie',), ('Bill Hammons',), ('Tom Hoefling',), ('Alyson Kennedy',), ('Jerome Segal',), ('Phil Collins',), (' None of these candidates',), ('Sheila Samm Tittle',), ('Dario Hunter',), ('Joe McHugh',), ('Christopher LaFontaine',), ('Keith McCormic',), ('Brooke Paige',), ('Gary Swing',), ('Richard Duncan',), ('Blake Huber',), ('Kyle Kopitke',), ('Zachary Scalf',), ('Jesse Ventura',), ('Connie Gammon',), ('John Richard Myers',), ('Mark Charles',), ('Princess Jacob-Fambro',), ('Joseph Kishore',), ('Jordan Scott',)]

def countyWin(state, county): #Given a state and county, return who won the election there
    db = sqlite3.connect(database)
    c = db.cursor()


    cmd = "select candidate, party, candidatevotes from ElectionResults2020 where state=? and county_name=?"


    c.execute(cmd,(state, county))
    poss = c.fetchall()
    best = poss[0]
    for row in poss:
        if (row[2] > best[2]):
            best = row


    return best
    db.commit()
    db.close()


def getStates(): #list of all states
    db = sqlite3.connect(database)
    c = db.cursor()

    lst = []
    c.execute("select state from ElectionResults2020;")
    results = c.fetchall()
    for state in results:
        if (len(lst) == 0 or lst[-1] != state[0]):
            lst.append(state[0])
    db.commit()
    db.close()  
    return lst
    

def getCountyfromState(state): #given a state, get all the counties in the state
    db = sqlite3.connect(database)
    c = db.cursor()

    lst = []
    cmd = "select county_name from ElectionResults2020 where state=?;"
    c.execute(cmd, (state,))
    results = c.fetchall()
    for place in results:
        if (len(lst) == 0 or lst[-1] != place[0]):
            lst.append(place[0])

    db.commit()
    db.close()  
    return lst   

def loadTableBasic(csvName, tableName):
# Setting up database interaction
    db = sqlite3.connect(database)
    c = db.cursor()

# Loading up the csv
    read = open(csvFolder + f'/{csvName}', "r")
    full = read.readlines()

# Creating the table based on the first row of the csv
    cols = full[0].strip().split(",")
    # print(colsString(cols))
    c.execute("create table if not exists " + tableName + "(" + colsString(cols) + ");" )

# Checking if the table is empty
    c.execute(f"select * from {tableName}")
    empty = c.fetchone()
    # print(empty)
    if (empty == None):
#Filling out the table
        for row in full:
            if( row != full[0]):
                line = splitSplit(row.strip(), '"')
                #print(line)
                cmd = "insert into " + tableName +" values(?" + (", ?" *(len(line) - 1)) + ");"
                #print(cmd)
                c.execute(cmd, tuple(line))

    db.commit()
    db.close()

def getEducation(state, county):
    # Setting up database interaction
    db = sqlite3.connect(database)
    c = db.cursor()

    cmd = "select * from Education where State=? and Area=?"
    c.execute(cmd, (states[state], county))

    splurge = c.fetchall()
    lst = []
    for result in splurge:
    	if ("2017-21" in result[3]):
    		lst.append(result)
    return lst

def getPopulation(state, county):
    # Setting up database interaction
    db = sqlite3.connect(database)
    c = db.cursor()

    cmd = "select * from CountyPopulation where State=? and Area=?"
    c.execute(cmd, (states[state], county))

    return c.fetchall()

def getUnemployment(state, county):
    # Setting up database interaction
    db = sqlite3.connect(database)
    c = db.cursor()
    countyin = county + ", " + states[state]

    cmd = "select * from UnemploymentAndIncome where State=? and Area=?"
    c.execute(cmd, (states[state], countyin))

    something = c.fetchall()
    lst = []
    for row in something:
        if ("Unemployment_rate_2000" in row[3] \
        or "Unemployment_rate_2004" in row[3] \
        or "Unemployment_rate_2008" in row[3] \
        or "Unemployment_rate_2012" in row[3] \
        or "Unemployment_rate_2016" in row[3] \
        or "Unemployment_rate_2020" in row[3] \
        or "Employed_2020" in row[3] \
        or "Unemployed_2020" in row[3]):
            lst.append(row)
    return lst

def getPoverty(state, county):
    # Setting up database interaction
    db = sqlite3.connect(database)
    c = db.cursor()

    cmd = "select * from Poverty where State=? and Area=?"
    c.execute(cmd, (states[state], county))

    something = c.fetchall()
    lst = []
    for row in something:
        if ("POVALL" in row[3] or "PCTPOVALL" in row[3] or "MEDHHINC" in row[3]):
            lst.append(row)
    return lst

loadElection()
loadTableBasic("PopulationEstimates.csv", "CountyPopulation")
loadTableBasic("PovertyEstimates.csv", "Poverty")
loadTableBasic("Education.csv", "Education")
loadTableBasic("Unemployment.csv", "UnemploymentAndIncome")

"""
print(countyVoting("New Jersey", "Sussex County"))
print(getCounties())
print("\n\n")
print(getCandidates())
print("\n\n")

someList = getCounties()
for county in someList:
    print(county)
    print(countyWin(county[0], county[1]))
print("\n\n\n")

otherList = getStates()
print(otherList)
for state in otherList:
    print(getCountyfromState(state))
"""
