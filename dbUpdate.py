import sqlite3

db = "users.db"

# connect to db
con = sqlite3.connect(db)

# create cursor that will execute SQL commands
cur = con.cursor()

# create table temp
# cur.execute("""CREATE TABLE users (
#     id VARCHAR(100) PRIMARY KEY NOT NULL,
#     mail VARCHAT(100),
#     password VARCHAR(100)
# )""")
            
# create table temp
# cur.execute("""CREATE TABLE temp (
#     id VARCHAR(100) PRIMARY KEY NOT NULL,
#     name VARCHAR(100),
#     mail VARCHAT(100),
#     password VARCHAR(100)
# )""")

# cur.execute("INSERT INTO users VALUES ('B4nanaJuice', 'griesmaxime2@gmail.com', 'c9592af4ed5c338f2e2bc86568c42cf081c35f2103c9f56e63026906699a41be')")
# save data
# con.commit()

# cur.execute("INSERT INTO temp VALUES (?, ?, ?, ?)", ["abc", "hjhjh", "d", "lkujlkj"])
res = cur.execute("SELECT * FROM users")
print(res.fetchall())

res = cur.execute("SELECT * FROM temp")
print(res.fetchall())

con.commit()
con.close()
