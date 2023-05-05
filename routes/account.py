from flask import session, render_template, redirect, url_for, request
import sqlite3, hashlib
import config

def account():

    # if the user is not connected
    if 'name' not in session:
        return redirect(url_for('login'))

    # connect to database
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    # get user's information
    user: tuple = cur.execute("SELECT * FROM users WHERE id = ?", [session['name']]).fetchone()

    # close connection
    con.close()

    # return the page
    return render_template("account/account.html", **locals())

def change_mail():

    # is user is not connected
    if 'name' not in session or session['name'] is None:
        return redirect(url_for('home'))
    
    # get mail and password from form
    password: str = request.form['password']
    new_mail: str = request.form['new_mail']
    
    # connect to database
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    # check password
    m: hashlib._Hash = hashlib.sha256()
    m.update(password.encode())
    password = m.hexdigest()

    user: tuple = cur.execute("SELECT * FROM users WHERE id = ?", [session['name']]).fetchone()
    if password != user[2]:
        session['error'] = "Your password is not correct."
        return redirect(url_for('account'))
    
    # check if mail isn't already taken (users and temp db)
    if cur.execute("SELECT * FROM users WHERE mail = ?", [new_mail]).fetchone() is not None or cur.execute("SELECT * FROM temp WHERE mail = ?", [new_mail]) is not None:
        session['error'] = "This email is already taken."
        return redirect(url_for('account'))

    # change mail
    cur.execute("UPDATE users SET mail = ? WHERE id = ?", [new_mail, session['name']])

    # save changes and close connection
    con.commit()
    con.close()

    # return to account page
    session['info'] = "Your mail has been changed successfully !"
    return redirect(url_for('account'))

def change_password(password: str, new_password: str):
    return 1