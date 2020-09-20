import sqlite3, csv
from io import StringIO

# Read database to tempfile
con = sqlite3.connect('StateUniversities.db')
c = conn.cursor()

tempfile = StringIO()
for line in con.iterdump():
    tempfile.write('%s\n' % line)
    
con.close()
tempfile.seek(0)
