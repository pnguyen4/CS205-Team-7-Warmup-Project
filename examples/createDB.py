import sqlite3 as sql
conn = sql.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE universities (name text, country text, age real)''')
query = "INSERT INTO universities VALUES ('University of Vermont', 'United States', 229)"
c.execute(query)

conn.commit()
conn.close()
