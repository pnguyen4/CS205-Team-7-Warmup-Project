import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("SELECT * FROM universities WHERE name='University of Vermont'")
print(c.fetchone())
conn.close()
