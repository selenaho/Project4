from flask import Flask, render_template, request
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
        winner = table.countyWin(randState, randCounty)[0]
        winnerIndex = random.randint(0,3)
        candidateArray = [0] * 4
        candidateArray[winnerIndex] = winner
        for i in range(len(candidateArray)):
            if candidateArray[i] == 0:
                candidateArray[i] = random.choice(table.getCandidates())[0]
        print(candidateArray)

        return render_template("game.html", countyName = randCounty, stateName = randState, a = candidateArray[0], b = candidateArray[1], c = candidateArray[2], d = candidateArray[3], winnerIndex = winnerIndex)#pass through the four answer choices and index of the correct answer 
    else:
       return redirect(url_for("result"))#pass through correct answer, county name, state name

@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template("result.html")
    else:
        return redirect(url_for("main_page"))


if __name__ == "__main__":
    app.debug = True
    app.run()

