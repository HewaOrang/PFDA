# This program creates a table named 'books' in a SQLite database.
# Program by: Hewa orang

import sqlite3
con = sqlite3.connect("pfda.db") # I will calll this database pdfa.db
cur = con.cursor()
#sql = "DROP TABLE IF EXISTS book"
#cur.execute(sql)

cur.execute("CREATE TABLE book(tiitle, author, ISBN)")
# no errors? we should write some code to test this exists
# or even a print to sya "done"
con.close()
