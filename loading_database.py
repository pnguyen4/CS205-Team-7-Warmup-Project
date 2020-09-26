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
    assert list_university_state(conn, "Virginia") == ['University of Virginia']
    assert in_state_capital_university(conn, "Columbia university") == 'FALSE'
    print("Passed all test cases")
    conn.close()

# Example 1: query one value from one row
def get_num_institutions_state(conn, arg):
    c = conn.cursor()
    # arg must be in a tuple, or else each letter is interpreted as an arg
    c.execute('''SELECT numberOfInstitutions FROM states WHERE name=?''', (arg,))
    # execute() returns a list of tuples but we know that this query should
    # only return one row with only one value. Not true for all queries!
    result = c.fetchall()
    if len(result) != 0:
        return result[0][0]
    else:
        return "No result for argument: " + arg

# Example 2: query one value that depends on both rows
def get_state_university(conn, arg):
    c = conn.cursor()
    # universities.state is the foreign key linking to
    # states.id, the row index and primary key in states table
    c.execute('''SELECT states.name
              FROM (universities JOIN states ON universities.state = states.id)
              WHERE universities.name = ?''', (arg,))
    result = c.fetchall()
    if len(result) != 0:
        return result[0][0]
    else:
        return "No result for argument: " + arg


def get_population_university(conn, arg):
    c = conn.cursor()
    c.execute('''SELECT population FROM universities WHERE name=?''', (arg,))
    result = c.fetchall()
    if len(result) != 0:
        return result[0][0]
    else:
        return "No result for argument: " + arg

def get_city_university(conn, arg):
    c = conn.cursor()
    c.execute('''SELECT city FROM universities WHERE name=?''', (arg,))
    result = c.fetchall()
    if len(result) != 0:
        return result[0][0]
    else:
        return "No result for argument: " + arg

def get_population_state(conn, arg):
    #raise NotImplementedError
    c = conn.cursor()
    c.execute('''SELECT population FROM states WHERE name=?''', (arg,))
    result = c.fetchall()
    if len(result) != 0:
        return result[0][0]
    else:
        return "No result for argument: " + arg

def get_capital_state(conn, arg):
    c = conn.cursor()
    c.execute('''SELECT capital FROM states WHERE name=?''', (arg,))
    result = c.fetchall()
    if len(result) != 0:
        return result[0][0]
    else:
        return "No result for argument: " + arg

def list_university_state(conn, arg):
    #raise NotImplementedError
    result = []
    c = conn.cursor()
    c.execute('''SELECT universities.name
                FROM (universities JOIN states ON universities.state = states.id)
                WHERE states.name = ?''', (arg,))
    rows = c.fetchall()
    for row in rows:
        result.append(row[0])
    if len(result) == 0:
       result = ["No data found"]
    return result

def in_state_capital_university(conn, arg):
    c = conn.cursor()
    c.execute('''SELECT
                CASE WHEN city = capital
                    THEN 'TRUE'
                    ELSE 'FALSE'
                END
                FROM (universities JOIN states ON universities.state = states.id)
                WHERE universities.name = ?''', (arg,))
    result = c.fetchall()
    if len(result) != 0:
        return result[0][0]
    else:
        return "No result for argument: " + arg

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
