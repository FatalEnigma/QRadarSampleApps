__author__ = 'IBM'

from flask import render_template, request
from app import app
from qpylib import qpylib
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title = "MultiComponent App!")

@app.route('/offenseListFunction', methods=['GET'])     
def offenseListFunction():
    qpylib.log("offenseListFunction", "info")
    offense = request.args.get("context")
    qpylib.log("context=" + offense, "info")

    #You can process the data and return any value here, that will be passed into javascript
    return json.dumps({'context_passed_to_python_route':offense})