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
        #print(winner)
        winnerIndex = random.randint(0,3)
        choiceArray = [0] * 4
        choiceArray[winnerIndex] = winner
        #print("____")
        #print(table.getCandidates())
        #print(table.getCandidates()[0][0])
        #print(len(table.getCandidates()))

        #otherIndex is the index of either Trump or Biden depending on who the winner is
        #makes it so that Trump and Biden are always together or if there's another winner (did that happen?) then there will be at least Trump or Biden
        otherIndex = random.randint(0,3)
        while(otherIndex == winnerIndex):
            otherIndex = random.randint(0,3)
        other = "Donald Trump"
        if(winner == "Donald Trump"):
            other = "Joe Biden"
        choiceArray[otherIndex] = other

        candidateArray = table.getCandidates()
        removeRepeat(candidateArray, winner) #removes the winner from the candidate array so no repeats in mc
        removeRepeat(candidateArray, other) #removes the other opponent

        #populating the other choices
        for i in range(len(choiceArray)):
            if choiceArray[i] == 0:
                #set to a random candidate if there's not a value in the array
                choiceArray[i] = random.choice(candidateArray)[0]
                #remove the newly put in candidate from the array of options
                removeRepeat(candidateArray, choiceArray[i])
        #print(choiceArray)

        #using replace to deal with the spaces in some of the county and state names
        stateNameValue = randState.replace(" ", "|")
        countyNameValue = randCounty.replace(" ", "|")

        return render_template("game.html", countyName = randCounty, stateName = randState, stateNameValue = stateNameValue, countyNameValue = countyNameValue, a = choiceArray[0], b = choiceArray[1], c = choiceArray[2], d = choiceArray[3], winnerIndex = winnerIndex)#pass through the four answer choices and index of the correct answer 
    else:
        
        county = request.form.get("county") #gets hidden value of county name from form
        state = request.form.get("state") #gets hidden value of state name from form
        #winner = table.countyWin(state, county)
        #print(table.countyWin(state, county))
        #print(winner)
        #print(state)
        #print(county)
        #state = state.replace(" ", "|")
        #county = county.replace(" ", "|")
        #print("________")
        #print(state)
        #print(county)
        winnerIndex = request.form.get("winnerIndex")
        won = False
        
        print(type(winnerIndex))
        if 'a' in request.form: #if user pressed on button choice a
            print("presssed")
            print(winnerIndex)
            
            if winnerIndex == "0":
                print("0 yup")
                won = True
        elif 'b' in request.form:
            if winnerIndex == "1":
                won = True
        elif 'c' in request.form:
            if winnerIndex == "2":
                won = True
        elif 'd' in request.form:
            if winnerIndex == "3":
                won = True
        print(won)
        if won:
            bool="y"
        else:
            bool="n"
        return redirect(url_for("result", state=state, county=county, bool=bool))#pass through correct answer, county name, state name

#function to help make sure the answer choices have no repeats
def removeRepeat(array, choice):
    for i in range(len(array)):
        print(i)
        print(array[i][0])
        if(array[i][0] == choice):
            array.pop(i)
            print(array)
            break

@app.route("/result/<state>/<county>/<bool>", methods=['GET', 'POST'])
def result(state, county, bool):
    if request.method == 'GET':
        path = request.path.split("/")
        #path[2] is state
        stateName = path[2].replace("|", " ")
        #path[3] is county
        countyName = path[3].replace("|", " ")
        print(path)
        #print(stateName)
        #print(countyName)
        
        #selecting win/loss message
        won = path[4]
        message = ""
        winMessages = ["Congrats!", "Good job!", "You passed gov!"]
        loseMessages = ["Wrong :(", "Not quite", "Close enough I guess", "You certainly tried!"]
        if won == "y":
            message = random.choice(winMessages)
        if won == "n":
            message = random.choice(loseMessages)
        
        winner = table.countyWin(stateName, countyName)[0]
        #html for hidden unemployment value: <input type="hidden" name="unemploymentData" id="job_data" value={{job_data}}>

        #html for hidden education value: <input type="hidden" name="educationData" id="edu_data" value={{edu_data}}>

        #pass the data into the render template through here using stateName and countyName to get data first
        return render_template("result.html", countyName = countyName, stateName = stateName, winner = winner, message=message)
    else:
        return redirect(url_for("main_page"))

@app.route("/ignoreTesting")
def testing():
    table.loadTableBasic("PopulationEstimates.csv", "CountyPopulation")
    table.loadTableBasic("PovertyEstimates.csv", "Poverty")
    table.loadTableBasic("Education.csv", "Education")
    table.loadTableBasic("Unemployment.csv", "UnemploymentAndIncome")
    return ("Lets lookasee")
    

if __name__ == "__main__":
    app.debug = True
    app.run()

