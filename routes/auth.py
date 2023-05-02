from flask import request, session, redirect, url_for, render_template
import sqlite3, hashlib
import threading, time

def login():
    
    # see the login form
    if request.method == 'GET':
        # is user is connected: redirect to his page
        if "name" in session:
            session.pop('info', default = None)
            session.pop('error', default = None)
            return redirect(url_for('home'))
        
        # else: show the login form
        else:
            return render_template("auth/login.html", **locals())

    # if the form is sent, get inputs information
    elif request.method == 'POST':

        # remove error message from the session
        session.pop('info', default = None)
        session.pop('error', default = None)
        
        # get inputs information
        username: str = request.form["name"]
        password: str = request.form["password"]

        # connect to database
        con = sqlite3.connect("users.db")
        cur = con.cursor()

        # check if username is registered
        res = cur.execute("SELECT * FROM users WHERE id = ? COLLATE NOCASE", [username])
        user = res.fetchone()
        if user is None:
            session['error'] = "The given username is unknown. Please check if you spelled it correctly."
            return redirect(url_for("login"))

        # check if password is correct
        m = hashlib.sha256()
        m.update(password.encode())
        hashed_password = m.hexdigest()

        if hashed_password != user[2]:
            session['error'] = "The password is incorrect."
            return redirect(url_for("login"))
    
        # open a session witht he username
        session['name'] = username

        # redirect to home page (not for the moment)
        session['info'] = "You successfully connected !"
        return redirect(url_for('home')) 
    
def lougout():

    # if the user is not connected
    if "name" not in session:
        return redirect(url_for("login"))
    
    # remove name from session
    session.pop('name', default = None)

    # redirect to login page saying you're disconnected from your account
    session['info'] = "You successfully logged out."
    return redirect(url_for("login"))

def register():

    # if the user is already connected, go back to home page
    if 'name' in session:
        return redirect(url_for('home'))

    # see the register form
    if request.method == 'GET':
        return render_template("auth/register.html")

    # if the form is sent, get inputs information
    elif request.method == 'POST':

        # get inputs information
        username: str = request.form["name"]
        mail: str = request.form["mail"]
        password: str = request.form["password"]
        password_repeat: str = request.form["password-repeat"]

        # check if passwords are correct
        conditions: list[bool] = [
            any(x.isupper() for x in password),
            any(x.islower() for x in password),
            any(x.isdigit() for x in password),
            any(not x.isalnum() for x in password),
            len(password) >= 8,
            password == password_repeat
        ]

        if False in conditions:
            session['error'] = "Your password doesn't fill the requirements."
            return render_template("auth/register.html", **locals())

        # connect to database
        con = sqlite3.connect("users.db")
        cur = con.cursor()

        # check if username is available (get from table, if exists, then not available)
        res = cur.execute("SELECT * FROM users WHERE id = ? COLLATE NOCASE", [username])
        if (res.fetchone() is not None):
            session['error'] = "The username is already used."
            return render_template("auth/register.html", **locals())
        
        # check if also available in the temp database
        res = cur.execute("SELECT * FROM temp WHERE name = ? COLLATE NOCASE", [username])
        if (res.fetchone() is not None):
            session['error'] = "The username is not available for the moment."
            return render_template("auth/register.html", **locals())
        
        # check if username is "correct"
        if username in ["users", "temp"]:
            session['error'] = "You can't use that username."
            return render_template("auth/register.html", **locals())

        # check if mail is available
        res = cur.execute("SELECT * FROM users WHERE mail = ? COLLATE NOCASE", [mail])
        if (res.fetchone() is not None):
            session['error'] = "The mail is already used."
            return render_template("auth/register.html", **locals())
        
        # check if also available in the temp database
        res = cur.execute("SELECT * FROM temp WHERE mail = ? COLLATE NOCASE", [mail])
        if (res.fetchone() is not None):
            session['error'] = "The mail is not available for the moment."
            return render_template("auth/register.html", **locals())

        # SEE TO SEND A CONFIRMATION EMAIL

        # hash the password
        m: hashlib._Hash = hashlib.sha256()
        m.update(password.encode())
        password = m.hexdigest()

        # hash the username (this will be the token)
        m.update(username.encode())
        hashed_username: str = m.hexdigest()

        # put the name, mail and hashed password into the database
        cur.execute("INSERT INTO temp VALUES (?, ?, ?, ?)", (hashed_username, username, mail, password))

        # create a new table for the user
        print(f"http://localhost:5500/confirm/{hashed_username}")

        # make the url not usable after a delay
        threading.Thread(target = delete_temp_user, args = (hashed_username, )).start()

        # save the database
        con.commit()
        con.close()

        # redirect to the login page, saying that a mail has been sent to confirm the account
        session['info'] = f"A mail have been sent the following email: {mail}. You have 4 hours to confirm your mail."
        return render_template("auth/login.html", **locals())
    
def delete_temp_user(id: str):

    # the url will be usable for 4 hours
    time.sleep(14400)

    # connect to the database
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    # delete the temp user from the temp table
    cur.execute("DELETE FROM temp WHERE id = ?", [id])

    # commit changes
    con.commit()

    # close the connection
    con.close()

def confirm(token: str):

    # connect to the database
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    # look for the temp account with the token
    res = cur.execute("SELECT * FROM temp WHERE id = ?", [token])
    user = res.fetchone()

    # if the temp user is not found, return the login page and an error saying the token is unknown
    if user is None:
        session.pop('info', default = None)
        session["error"] = "The given token is unknown."
        return redirect(url_for("login"))

    # if found: put the account in the users table
    cur.execute("INSERT INTO users VALUES (?, ?, ?)", user[1:])

    # delete the temp user
    cur.execute("DELETE FROM temp WHERE id = ?", [token])

    # save the database
    con.commit()
    con.close()

    # return to login page with message saying that the account was verified
    session.pop('error', default = None)
    session["info"] = "Your account has been verified successfully ! You can now login."
    return redirect(url_for("login"))