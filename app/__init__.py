from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        #need db method to get an array [choice a, choice b, choice c, choice d, index of correct choice, county, state]
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

