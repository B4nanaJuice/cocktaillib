from flask import session, render_template, redirect, url_for
import sqlite3
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
    print(user)

    # return the page
    return render_template("account/account.html", **locals())