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

def loadElection():

# Setting up database interaction
    db = sqlite3.connect(database)
    c = db.cursor()

# Loading up the csv
    read = open(csvFolder + "/president_county_candidate.csv", "r")
    full = read.readlines()

# Creating the table based on the first row of the csv
    cols = full[0].strip().split(",")
    # print(colsString(cols))
    c.execute("create table if not exists ElectionResults2020(" + colsString(cols) + ");" )

# Checking if the table is empty
    c.execute("select * from ElectionResults2020")
    empty = c.fetchone()
    # print(empty)
    if (empty == None):
#Filling out the table
        for row in full:
            if( row != full[0]):
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

    cmd = "select candidate, party, total_votes, won from ElectionResults2020 where state=? and county=?;"
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
    c.execute("select state, county from ElectionResults2020")
    results = c.fetchall()
    for county in results:
        if (len(lst) == 0 or lst[-1] != county):
            lst.append(county)

    db.commit()
    db.close()
    return lst

def getCandidates(): #Get a list of all people who participated in the election
    db = sqlite3.connect(database)
    c = db.cursor()

    lst = []
    c.execute("select candidate from ElectionResults2020")
    results = c.fetchall()
    for person in results:
        if (not person in lst):
            lst.append(person)
    db.commit()
    db.close()
    return lst

def countyWin(state, county): #Given a state and county, return who won the election there
    db = sqlite3.connect(database)
    c = db.cursor()

    cmd = "select candidate, party, total_votes from ElectionResults2020 where state=? and county=? and won='True';"

    c.execute(cmd,(state, county))
    return c.fetchone()

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
    cmd = "select county from ElectionResults2020 where state=?;"
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