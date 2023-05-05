"""
Silly Ramen Obliterates Frog
"""

import sqlite3
import csv
import os

def makeTables():
    return 0
    
def loadElection():
    election = open(os.getcwd() + "/../csvs/president_county_candidate.csv", "r")
    fullText = election.readlines()
    for row in fullText:
    #    print(row)
        if (row != fullText[0]):
            line = row.split("<")
        #Here is where we need to start the Database stuff



loadElection()