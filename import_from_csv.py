import sqlite3, csv

def create_database():
    conn = sqlite3.connect('StateUniversities.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE states (id integer PRIMARY KEY, name text, capital text, population integer, numberOfInstitutions integer)''')
    file1 = open('states.csv', 'r')

    rows = csv.reader(file1, delimiter=',', quotechar='"')
    for row in rows:
        c.execute('''INSERT INTO states(name, capital, population, numberofInstitutions) VALUES (?,?,?,?)''', row)
        conn.commit()
    file1.close()

    c.execute('''CREATE TABLE universities (id integer PRIMARY KEY, name text, population integer, city text, state integer,FOREIGN KEY (state) REFERENCES states (id) )''')

    file2 = open('universities.csv', 'r')
    rows = csv.reader(file2, delimiter=',', quotechar='"')
    for row in rows:
        c.execute('''INSERT INTO universities(name, population, city, state) VALUES(?,?,?, (SELECT id FROM states WHERE name = ?))''', row)
        conn.commit()
    file2.close()

    print("\nImported csv successfully!")
    return conn

def load_database():
    conn = sqlite3.connect('StateUniversities.db')
    print("Loading existing database.")
    return conn
