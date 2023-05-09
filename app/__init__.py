from flask import Flask, render_template, request
import requests
import random

import utl.tableHandler as table

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        randState = random.choice(table.getStates())
        randCounty = random.choice(table.getCountyfromState(randState))
        winner = table.countyWin(randState, randCounty)
        winnerIndex = random.randInt(0,3)
        candidateArray = [0] * 4
        candidateArray[winnerIndex] = winner
        for i in range(len(candidateArray)):
            if candidateArray[i] == 0:
                candidateArray[i] = random.choice(table.getCandidates)
        print(candidateArray)
                

        return render_template("game.html")#pass through the four answer choices and index of the correct answer 
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

