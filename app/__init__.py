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
        #print(randState)
        #print(randCounty)
        winner = table.countyWin(randState, randCounty)[0]
        print(winner)
        winnerIndex = random.randint(0,3)
        choiceArray = [0] * 4
        choiceArray[winnerIndex] = winner
        print("____")
        print(table.getCandidates())
        print(table.getCandidates()[0][0])
        print(len(table.getCandidates()))

        candidateArray = table.getCandidates()
        for i in range(len(candidateArray)-1):
            print(candidateArray[i][0])
            if(candidateArray[i][0] == winner):
                candidateArray.pop(i)
        print(candidateArray)
        
        #check if pop works!!!!!

        for i in range(len(choiceArray)):
            if choiceArray[i] == 0:
                choiceArray[i] = random.choice(table.getCandidates())[0]
        print(choiceArray)

        stateNameValue = randState.replace(" ", "|")
        countyNameValue = randCounty.replace(" ", "|")

        return render_template("game.html", countyName = randCounty, stateName = randState, stateNameValue = stateNameValue, countyNameValue = countyNameValue, a = choiceArray[0], b = choiceArray[1], c = choiceArray[2], d = choiceArray[3], winnerIndex = winnerIndex)#pass through the four answer choices and index of the correct answer 
    else:
       county = request.form.get("county") #gets hidden value of county name from form
       state = request.form.get("state") #gets hidden value of state name from form
       #winner = table.countyWin(state, county)
       #print(table.countyWin(state, county))
       #print(winner)
       print(state)
       print(county)
       #state = state.replace(" ", "|")
       #county = county.replace(" ", "|")
       print("________")
       print(state)
       print(county)
       return redirect(url_for("result", state=state, county=county))#pass through correct answer, county name, state name

@app.route("/result/<state>/<county>", methods=['GET', 'POST'])
def result(state, county):
    if request.method == 'GET':
        path = request.path.split("/")
        #path[2] is state
        stateName = path[2].replace("|", " ")
        #path[3] is county
        countyName = path[3].replace("|", " ")
        print(path)
        print(stateName)
        print(countyName)
        winner = table.countyWin(stateName, countyName)[0]
        #pass the data into the render template through here using stateName and countyName to get data first
        return render_template("result.html", countyName = countyName, stateName = stateName, winner = winner)
    else:
        return redirect(url_for("main_page"))


if __name__ == "__main__":
    app.debug = True
    app.run()

