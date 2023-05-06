import sqlite3
import os

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

database = os.getcwd() + "/../dillbickle"

def colsString(listy):
    string = ""
    for item in listy:
        string += f'\"{item}\" text'
        if (item != listy[-1]):
            string += ", "
    return string

def loadElection():

# Setting up database interaction
    db = sqlite3.connect(database)
    c = db.cursor()

# Loading up the csv
    read = open(os.getcwd() + "/../csvs/president_county_candidate.csv", "r")
    full = read.readlines()

# Creating the table based on the first row of the csv
    cols = full[0].strip().split(",")
    # print(colsString(cols))
    c.execute("create table if not exists PresidentElection2020(" + colsString(cols) + ");" )

# Checking if the table is empty
    c.execute("select * from PresidentElection2020")
    empty = c.fetchone()
    # print(empty)
    if (empty == None):
#Filling out the table
        for row in full:
            if( row != full[0]):
                line = row.strip().split(",")
                #print(line)
                cmd = "insert into PresidentElection2020 values(?" + (", ?" *(len(line) - 1)) + ");"
                #print(cmd)
                c.execute(cmd, tuple(line))

    db.commit()
    db.close()

def loadTable(tableName, csvName):

# Setting up database interaction
    db = sqlite3.connect(database)
    c = db.cursor()

# Loading up the csv
    read = open(os.getcwd() + f'/../csvs/{csvName}', "r")
    full = read.readlines()

# Creating the table based on the first row of the csv
    cols = full[0].strip().split(",")
    # print(colsString(cols))
    c.execute("create table if not exists " + tableName +"(" + colsString(cols) + ");" )

# Checking if the table is empty
    c.execute(f'select * from {tableName}')
    empty = c.fetchone()
    # print(empty)
    if (empty == None):
#Filling out the table
        for row in full:
            if( row != full[0]):
                line = row.strip().split(",")
                #print(line)
                cmd = "insert into " + tableName + " values(?" + (", ?" *(len(line) - 1)) + ");"
                #print(cmd)
                c.execute(cmd, tuple(line))

    db.commit()
    db.close()

def countyVoting(state, county):
    db = sqlite3.connect(database)
    c = db.cursor()

    cmd = "select candidate, party, total_votes, won from PresidentElection2020 where state=? and county=?;"
    c.execute(cmd,(state, county))
    results = c.fetchall()
    if (results != None):
        for answer in results:
            print(answer)
    else:
        return "Give real county"

    db.commit()
    db.close()

countyVoting("Delaware", "Sussex County")