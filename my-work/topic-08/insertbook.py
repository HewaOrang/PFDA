# This program inserts a book into the 'book' table in a SQLite database.
# Program by: Hewa orang

import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()

# check there is nothing in the database
result = cur.execute("select * from book")
print (result.fetchone())

# insert a book
sql = (
    """
    INSERT INTO book VALUES
        ('Harry Pothead', 'Just Kidding Really', '112344'),
        ('Harry Potter does something profound', 'JK Rowling', '123444')
    """
)
# DANGER DANGER this can lead to SQL injection
cur.execute(sql)
con.commit()

result = cur.execute("select * from book")
print (result.fetchone())
con.close()