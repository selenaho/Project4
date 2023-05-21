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
        print(randState)
        randCounty = random.choice(table.getCountyfromState(randState))
        #print(randState)
        #print(randCounty)
        winner = table.countyWin(randState, randCounty)[0].title()
        #print(table.countyWin("OKLAHOMA", "SEQUOYAH"))
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
        other = "Donald J Trump"
        if(winner == "Donald J Trump"):
            other = "Joseph R Biden Jr"
        choiceArray[otherIndex] = other


        candidateArray = table.getCandidates()
        removeRepeat(candidateArray, "Joe Biden")
        removeRepeat(candidateArray, "Donald J Trump")
        print(candidateArray)


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


        return render_template("game.html", countyName = randCounty.title(), stateName = randState.title(), stateNameValue = stateNameValue, countyNameValue = countyNameValue, a = choiceArray[0], b = choiceArray[1], c = choiceArray[2], d = choiceArray[3], winnerIndex = winnerIndex)#pass through the four answer choices and index of the correct answer
    else:
       
        county = request.form.get("county").upper() #gets hidden value of county name from form
        state = request.form.get("state").upper() #gets hidden value of state name from form
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
       
        #print(type(winnerIndex))
        if 'a' in request.form: #if user pressed on button choice a
            #print("presssed")
            #print(winnerIndex)
           
            if winnerIndex == "0":
                #print("0 yup")
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
        #print(won)
        if won:
            bool="y"
        else:
            bool="n"
        return redirect(url_for("result", state=state, county=county, bool=bool))#pass through correct answer, county name, state name


#function to help make sure the answer choices have no repeats
def removeRepeat(array, choice):
    for i in range(len(array)):
        #print(i)
        #print(array[i][0])
        if(array[i][0] == choice):
            array.pop(i)
            #print(array)
            break


@app.route("/result/<state>/<county>/<bool>", methods=['GET', 'POST'])
def result(state, county, bool):
    if request.method == 'GET':
        path = request.path.split("/")
        #path[2] is state
        stateName = path[2].replace("|", " ")
        #path[3] is county
        countyName = path[3].replace("|", " ")
        #print(path)
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
       
        winner = table.countyWin(stateName, countyName)[0].title()


        #UNEMPLOYMENT
        print(stateName, countyName.title())
        #print(table.getUnemployment("SOUTH DAKOTA", "Jones County"))
        print("_____")
        #print(table.getUnemployment("South Dakota", "Jones County"))
        #print(countyName.title() + " County")
        unemployment = table.getUnemployment(stateName, countyName.title() + " County")
       
       
        if (not unemployment): #doing this because counties in louisiana end in parish not county
            unemployment = table.getUnemployment(stateName, countyName.title() + " Parish")
        if (not unemployment): #for virginia
            unemployment = table.getUnemployment(stateName, countyName.capitalize())
        print(stateName)
        print(countyName)
        print("unemployment:")
        print(unemployment)
        #order of the returned array:
        #0: rate2000
        #1: rate2004
        #2: rate2008
        #3: rate2012
        #4: rate2016
        #5: employed2020
        #6: unemployed2020
        #7: rate2020


        rate2000 = unemployment[0][4]
        rate2004 = unemployment[1][4]
        rate2008 = unemployment[2][4]
        rate2012 = unemployment[3][4]
        rate2016 = unemployment[4][4]
        employed2020 = unemployment[5][4]
        unemployed2020 = unemployment[6][4]
        rate2020 = unemployment[7][4]


        #poverty section
        poverty = table.getPoverty(stateName, countyName.title() + " County")
        if (not poverty):
            poverty = table.getUnemployment(stateName, countyName.title() + " Parish")
        if(not poverty):
            poverty = table.getUnemployment(stateName, countyName.capitalize())
        #print(poverty)
       
        countyPercentPovAll = poverty[1][4]
        #print(countyPercentPovAll)
        countyMedianHHIncome = poverty[2][4]
        #print(countyMedianHHIncome)


        #print("Connecticut:")
        #print(table.getPoverty("Connecticut", "Madison"))
        #NEED TO ADD SMTH TO HANDLE CASES LIKE THIS WHERE MADISONE EXISTS IN ONE TABLE AND NOT THE OTHER
        #ALSO COUNTIES NAMED DIFFERENTLY IN ALASKA


        statePov = table.getPoverty(stateName, stateName.title())
        #print(statePov)
        statePovRate = statePov[1][4]
        #print(statePovRate)


        USPov = table.getPoverty("United States", "United States")
        #print(USPov)
        USPovRate = USPov[1][4]
        #print(USPovRate)
        USMedianHHIncome = USPov[2][4]


        education = table.getEducation(stateName, countyName.title() + " County")
        if (not education):
            education = table.getUnemployment(stateName, countyName.title() + " Parish")
        if (not education):
            education = table.getUnemployment(stateName, countyName.capitalize())
        #print(education)


        #[('39085', 'OH', 'Lake County', 'Less than a high school diploma, 2017-21', '11693'), ('39085', 'OH', 'Lake County', 'High school diploma only, 2017-21', '52584'), ('39085', 'OH', 'Lake County', "Some college or associate's degree, 2017-21", '55194'), ('39085', 'OH', 'Lake County', "Bachelor's degree or higher, 2017-21", '48445'), ('39085', 'OH', 'Lake County', 'Percent of adults with less than a high school diploma, 2017-21', '6.963600848'), ('39085', 'OH', 'Lake County', 'Percent of adults with a high school diploma only, 2017-21', '31.31565783'), ('39085', 'OH', 'Lake County', "Percent of adults completing some college or associate's degree, 2017-21", '32.87000643'), ('39085', 'OH', 'Lake County', "Percent of adults with a bachelor's degree or higher, 2017-21", '28.85073489')]


        #EDUCATION
        educationArray = []
        for i in range(len(education)):
            dataTuple = (education[i][3], education[i][4])
            educationArray.append(dataTuple)
        #print("EDUCATION")
        #print(educationArray)


       
        return render_template("result.html",\
        countyName = countyName.title(), \
        stateName = stateName.title(), \
        winner = winner, \
        message=message, \
        CountyPovertyRate = countyPercentPovAll, \
        medianHouseIncome = countyMedianHHIncome, \
        StatePovertyRate = statePovRate, \
        USPovertyRate = USPovRate, \
        USMedianHouseIncome = USMedianHHIncome, \
        edu_data = educationArray,\
        edu0 = educationArray[0][1], \
        edu1 = educationArray[1][1], \
        edu2 = educationArray[2][1], \
        edu3 = educationArray[3][1], \
        edu4 = educationArray[4][1], \
        edu5 = educationArray[5][1], \
        edu6 = educationArray[6][1], \
        edu7 = educationArray[7][1], \
        job0 = rate2000, \
        job1 = rate2004, \
        job2 = rate2008, \
        job3 = rate2012, \
        job4 = rate2016, \
        job5 = rate2020, \
        employed2020 = employed2020, \
        unemployed2020 = unemployed2020, \
        bool = bool)
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