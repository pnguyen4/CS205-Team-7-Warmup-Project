import sqlite3, csv
from io import StringIO

import import_from_csv as db

# new test for loading data from database
def test():
    conn = db.load_database()
    print("Running test cases")
    # Tests for example 1 and 2
    assert get_num_institutions_state(conn, "Vermont") == 32
    assert get_state_university(conn, "Cornell University") == "New York"
    assert get_population_university(conn, "Cornell University") == 23449
    assert get_city_university(conn, "Cornell University") == "Ithaca"
    assert get_population_state(conn, "Vermont") == 625741
    assert get_capital_state(conn, "Vermont") == "Montpelier"
    assert list_university_state(conn, "Virginia") == "University of Virginia"
    assert in_state_capital_university(conn, "Columbia university") == '1'
    print("Passed all test cases")
    conn.close()

# Example 1: query one value from one row
def get_num_institutions_state(conn, arg):
    c = conn.cursor()
    # arg must be in a tuple, or else each letter is interpreted as an arg
    c.execute('''SELECT numberOfInstitutions FROM states WHERE name=?''', (arg,))
    # execute() returns a list of tuples but we know that this query should
    # only return one row with only one value. Not true for all queries!
    return c.fetchall()[0][0]

# Example 2: query one value that depends on both rows
def get_state_university(conn, arg):
    c = conn.cursor()
    # universities.state is the foreign key linking to
    # states.id, the row index and primary key in states table
    c.execute('''SELECT states.name
              FROM (universities JOIN states ON universities.state = states.id)
              WHERE universities.name = ?''', (arg,))
    return c.fetchall()[0][0]

def get_population_university(conn, arg):
    c = conn.cursor()
    c.execute('''SELECT population FROM universities WHERE name=?''', (arg,))
    return c.fetchall()[0][0]

def get_city_university(conn, arg):
    c = conn.cursor()
    c.execute('''SELECT city FROM universities WHERE name=?''', (arg,))
    return c.fetchall()[0][0]

def get_population_state(conn, arg):
    #raise NotImplementedError
    c = conn.cursor()
    c.execute('''SELECT population FROM states WHERE name=?''', (arg,))
    return c.fetchall()[0][0]

def get_capital_state(conn, arg):
    c = conn.cursor()
    c.execute('''SELECT capital FROM states WHERE name=?''', (arg,))
    return c.fetchall()[0][0]
    #raise NotImplementedError

def list_university_state(conn, arg):
    #raise NotImplementedError
    result = ""
    c = conn.cursor()
    c.execute('''SELECT universities.name
                FROM (universities JOIN states ON universities.state = states.id)
                WHERE states.name = ?''', (arg,))
    rows = c.fetchall()[0][0]
    for row in rows:
        result += rows[0]
    return result
        
def in_state_capital_university(conn, arg):
    #c = conn.cursor()
    #c.execute('''SELECT 
     #           CASE WHEN city = capital 
      #              THEN '1' 
       #             ELSE '0' 
        #        END 
         #       FROM (universities JOIN states ON universities.state = states.id)
          #      WHERE universities.name = ?''', (arg,))
    #return c.fetchall()
    raise NotImplementedError

test()

# old test for loading data from database
#########################
# Read database to tempfile
# con = sqlite3.connect('StateUniversities.db')
# c = con.cursor()
#
# tempfile = StringIO()
# for line in con.iterdump():
#     tempfile.write('%s\n' % line)
#
# con.close()
# tempfile.seek(0)
