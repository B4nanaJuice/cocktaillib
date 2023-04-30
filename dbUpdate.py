import sqlite3

db = "users.db"

# connect to db
con = sqlite3.connect(db)

# create cursor that will execute SQL commands
cur = con.cursor()

# create table users
# cur.execute("""CREATE TABLE users (
#     id VARCHAR(100) PRIMARY KEY NOT NULL,
#     mail VARCHAT(100),
#     password VARCHAR(100)
# )""")

# cur.execute("INSERT INTO users VALUES ('B4nanaJuice', 'griesmaxime2@gmail.com', 'c9592af4ed5c338f2e2bc86568c42cf081c35f2103c9f56e63026906699a41be')")
# save data
con.commit()

res = cur.execute("SELECT * FROM users")
print(res.fetchall())

# close connection with db
con.close()