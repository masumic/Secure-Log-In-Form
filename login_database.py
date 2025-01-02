import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS username
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,
                   password TEXT)''')

# Insert data into the table
#PART 1 = 7 hardcoded username/password
cursor.execute("INSERT INTO username (username, password) VALUES (?, ?)", ("rachels10", "password123"))
cursor.execute("INSERT INTO username (username, password) VALUES (?, ?)", ("asmi_is_cool", "123456"))
cursor.execute("INSERT INTO username (username, password) VALUES (?, ?)", ("mariokartwinner", "bowser#sucks"))
cursor.execute("INSERT INTO username (username, password) VALUES (?, ?)", ("queenPeach", "ILoveMario123"))
cursor.execute("INSERT INTO username (username, password) VALUES (?, ?)", ("masumi99", "2005"))
cursor.execute("INSERT INTO username (username, password) VALUES (?, ?)", ("mari4life", "m@r!@"))
cursor.execute("INSERT INTO username (username, password) VALUES (?, ?)", ("xX_Legend_Xx", "dress2impressRulez"))

# Commit the changes and close the connection
conn.commit()
conn.close()

# Retrieve data from the table
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM username")
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print(f"ID: {row[0]}, UserName: {row[1]}, Password: {row[2]}")

# Close the connection
conn.close()
