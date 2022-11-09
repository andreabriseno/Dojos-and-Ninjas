from flask import render_template, redirect, request
from flask_app import app 
from flask_app.models.dojo import Dojo #adding the class Dojo to dojos.py

@app.route('/')
def process_dojo():
    return redirect('/dojos')         #when opening page is going to go straight to url /dojo

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()                                      #getting the data from from dojo.py Dojo and query get_all
    return render_template("survey.html", places_dojos = dojos)    #renaming the dojos from model to all_dojos

@app.route('/dojo/create', methods=["POST"])  #creating new cities names 
def create():
    Dojo.create(request.form)        #getting the information from model dojo and query create since the name attribute is name does not need dictionary
    return redirect('/dojos')        #redirecting to mainpage 

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_one_all_ninjas(data))
    print(results)





