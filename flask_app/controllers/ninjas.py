from flask import render_template, redirect, request
from flask_app import app 
from flask_app.models.dojo import Dojo   #imports a file UPPER case is CLASSS
from flask_app.models.ninja import Ninja   

@app.route('/ninja')              #when clicking add ninja from survery template it would take it to this site/ninja html
def ninjas():
    return render_template('ninja.html', dojos = Dojo.get_all()) #displaying template
                                                                    # accessing the class dojo and classmethod dojo and renaming it dojos
@app.route('/create/ninja', methods=['POST']) 
def create_ninja():
    data = {
        "id" : request.form["id"],
        "first_name" : request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"]
    }
    Ninja.create(data) #accessing the classes from models ninja 
    return redirect('/')

@app.route('/dojo/edit/<int:id>')
def edit_dojo(id):
    data ={
        "id" : id
    }
    return render_template('edit_ninja.html', edit_one = Ninja.get_one(data))

@app.route('/dojo/update/<int:id>', methods=['POST'])
def update(id):
    data = {
        "id" :id,
        "first_name" : request.form["first_name"],
        "last_name":request.form["last_name"],
        "age": request.form["age"]
    }
    Ninja.update(data)
    return redirect('/dojos')

@app.route("/dojo/destroy/<int:id>")
def destroy(id):
    data ={
        "id":id
    }
    Ninja.destroy(data)
    return redirect('/dojos')
