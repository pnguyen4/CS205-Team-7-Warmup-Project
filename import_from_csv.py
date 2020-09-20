import sqlite3, csv

conn = sqlite3.connect('StateUniversities.db')
c = conn.cursor()

c.execute('''CREATE TABLE universities (name text, population integer, city text, state text)''')

with open('universities.csv','r') as inflie:
    records = 0;
    for row in inflie:
        c.execute("INSERT INTO universities VALUES (?,?,?,?)", row.split(","))
        conn.commit()
        records+=1
inflie.close()

c.execute('''CREATE TABLE states (name text, capital text, population integer, numberOfInstitutions integer)''')
with open('states.csv','r') as flie:
    records = 0;
    for row in flie:
        c.execute("INSERT INTO states VALUES (?,?,?,?)", row.split(","))
        conn.commit()
        records+=1
flie.close()

conn.close()
print("\n imported successfully")
