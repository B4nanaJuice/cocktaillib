from markupsafe import escape
from flask import Flask, redirect, render_template, request, url_for, abort, session
from markupsafe import escape
import json
import sqlite3

from classes.Cocktail import Cocktail
from classes.Ingredient import Ingredient

app = Flask(__name__)

# import os
# os.urandom(64)
app.secret_key = b'C\x9dt.\x9d\x8b\x05\xdfC\x8en \x7f\xdd\x15\xf7t\xde\xdc\xb6\xdf\xcc\x1f\xb0\xfa\xb4\xea1\x0cE(\xfe\xef@qL\x1cOA\xb8\xa1H\x9c\x057E\x0f@L\x82\x84\xfa\x98):\xbeo\x90\x10\xb9\x1e\xf2T\xd0'

@app.route("/")
def home():
    
    # Get all cocktails from the json file
    file = open("cocktails.json")
    cocktails = json.load(file)["cocktails"]
    
    # Return the template with the variables
    return render_template('home.html', **locals())

@app.route("/newCocktail", methods = ['GET', 'POST'])
def newCocktail():
    
    # See the page
    if request.method == 'GET':
        return render_template('newCocktail.html', **locals())
    
    # When the user submits the form
    elif request.method == 'POST':
        # Name of the cocktail
        cocktailName = request.form["cocktailName"]
        
        # Get all inputs with the same name
        ingredientNames = request.form.getlist("ingredientName")
        ingredientQuantities = request.form.getlist("ingredientQuantity")
        
        # Get the drink type
        drinkType = request.form["drinkType"]
        
        # Get the instructions
        instructions = request.form["instructions"]
        
        # Group the ingredients into a list
        ingredients = []
        for i in range(len(ingredientNames)):
            ingredients.append(
                Ingredient(
                    ingredientNames[i], 
                    ingredientQuantities[i]
                )
            )
            
        # Create the cocktail
        cocktail = Cocktail(cocktailName, ingredients, drinkType, instructions)
        
        # Save the cocktail into the file cocktails.json
        data = {}

        with open('cocktails.json', 'r', encoding = 'utf-8') as file:
            data = json.loads(file.read())
            
        data["cocktails"].append(cocktail.toJSON())

        with open('cocktails.json', 'w', encoding = 'utf-8') as file:
            file.write(json.dumps(data))
        
        # Redirect the user on the home page
        return redirect(url_for('home'))
    
@app.route("/<string:name>")
def cocktail(name: str):
    name = escape(name)
    with open('cocktails.json', 'r', encoding = 'utf-8') as file:
        data = json.loads(file.read())
        for cocktail in data["cocktails"]:
            if cocktail["name"] == name:
                return render_template('cocktail.html', cocktail = cocktail)
    abort(404)
    
@app.route("/removeCocktail/<string:name>")
def removeCocktail(name: str):
    name = escape(name)
    
    with open('cocktails.json', 'r', encoding = 'utf-8') as file:
        data = json.loads(file.read())
            
    for cocktail in data["cocktails"]:
        if cocktail["name"] == name:
            data["cocktails"].remove(cocktail)

    with open('cocktails.json', 'w', encoding = 'utf-8') as file:
        file.write(json.dumps(data))
        
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", **locals()), 404

@app.route("/login", methods = ['GET', 'POST'])
def login():
    # see the login form
    if request.method == 'GET':
        # is user is connected: redirect to his page
        if "name" in session:
            return redirect(url_for('home'))
        
        # else: show the login form
        else:
            return render_template("login.html", **locals())

    # if the form is sent, get inputs information
    elif request.method == 'POST':
        # get inputs information
        username: str = request.form["name"]
        password: str = request.form["password"]

        print(f"{username}: {password}")

        # check if username is registered

        # check if password is correct

        # open a session witht he username

        return redirect(url_for('login'))

        

@app.route("/register", methods = ['GET', 'POST'])
def register():
    # see the register form
    if request.method == 'GET':
        return render_template("register.html", **locals())

    # if the form is sent, get inputs information
    elif request.method == 'POST':
        # get inputs information
        print('')

        # check if username is available

        # check if password is correct

        # put username and hashed password in the user's db

        # create a new table for the user

app.run(host = '0.0.0.0', port = 5500, debug = True)