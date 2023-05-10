from flask import Flask, render_template, request, redirect, url_for
import requests
import random
import os

import utl.tableHandler as table

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def main_page():
    base = app.root_path
    table.loadElection()
    
    if request.method == 'GET':
        randState = random.choice(table.getStates())
        randCounty = random.choice(table.getCountyfromState(randState))
        print(randState)
        print(randCounty)
        winner = table.countyWin(randState, randCounty)[0]
        print(winner)
        winnerIndex = random.randint(0,3)
        candidateArray = [0] * 4
        candidateArray[winnerIndex] = winner
        for i in range(len(candidateArray)):
            if candidateArray[i] == 0:
                candidateArray[i] = random.choice(table.getCandidates())[0]
        print(candidateArray)

        return render_template("game.html", countyName = randCounty, stateName = randState, a = candidateArray[0], b = candidateArray[1], c = candidateArray[2], d = candidateArray[3], winnerIndex = winnerIndex)#pass through the four answer choices and index of the correct answer 
    else:
       county = request.form.get("county") #gets hidden value of county name from form
       state = request.form.get("state") #gets hidden value of state name from form
       #winner = table.countyWin(state, county)
       #print(table.countyWin(state, county))
       #print(winner)
       print(state)
       print(county)
       return redirect(url_for("result", state=state, county=county))#pass through correct answer, county name, state name

@app.route("/result/<state>/<county>", methods=['GET', 'POST'])
def result(state, county):
    if request.method == 'GET':
        path = request.path.split("/")
        #path[2] is state
        state = path[2]
        #path[3] is county
        county = path[3]
        print(path)
        print(state)
        print(county)
        winner = table.countyWin(state, county)[0]
        return render_template("result.html", countyName = county, stateName = state)
    else:
        return redirect(url_for("main_page"))


if __name__ == "__main__":
    app.debug = True
    app.run()

