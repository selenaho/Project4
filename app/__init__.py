from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template("game.html")#pass through the four answer choices, id of the correct answer 
    else:
        return redirect(url_for("result"))#pass through correct answer and 

@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template("result.html")
    else:
        return redirect(url_for("main_page"))


if __name__ == "__main__":
    app.debug = True
    app.run()

