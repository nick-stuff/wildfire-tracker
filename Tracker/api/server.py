#Imports from Python libraries
#Not tested yet - March 6th, 2024
from flask import Flask
from CurrHistMath import CurrHistMath

CurrHistMath = CurrHistMath()
pieChart = CurrHistMath.display_graph()

app = Flask(__name__)

@app.route("chart")
def index():
    return pieChart


