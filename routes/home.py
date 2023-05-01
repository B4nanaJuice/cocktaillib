from flask import render_template, session
import json

def home():

    if 'info' in session:
        print("df")

    if 'name' in session:
        print("coucou")
    
    # Get all cocktails from the json file
    file = open("cocktails.json")
    cocktails = json.load(file)["cocktails"]
    
    # Return the template with the variables
    return render_template('home.html', **locals())