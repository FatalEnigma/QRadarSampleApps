__author__ = 'IBM'
import json
from app import app
from qpylib import qpylib
from flask import render_template, request

#build a Flask app route, this route will build a Json construct, of which there is a 'html' attribute to contain a html string
@app.route('/getExampleDashboardItem', methods=['GET'])
def getExampleDashboardItem():
    try:
        qpylib.log("getExampleDashboardItem>>>")
        return json.dumps({'id':'ExampleDashBoardItem','title':'Example Dashboard','HTML':render_template('dashboard.html') })
    except Exception as e:
        qpylib.log( "Error "  + str(e) )
        raise

