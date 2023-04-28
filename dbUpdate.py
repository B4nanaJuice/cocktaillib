import sqlite3

db = "users.db"

# connect to db
con = sqlite3.connect(db)

# create cursor that will execute SQL commands
cur = con.cursor()

# create table users
cur.execute("""CREATE TABLE users (
    id VARCHAR(100) PRIMARY KEY NOT NULL,
    mail VARCHAT(100),
    password VARCHAR(100)
)""")

# save data
con.commit()

# close connection with db
con.close()