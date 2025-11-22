# This program reads in book details and puts them into the database.
# Program by: Hewa orang

import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()

book ={}
book['title'] = input("please enter book title: ")
book['author'] = input("please enter book author: ")
book['ISBN'] = input("please enter book ISBN: ")
#print (book)

data = [book] 

sql = "insert into book values (:title, :author, :ISBN)"
cur.executemany(sql, data)
con.commit()

for row in cur.execute("select * from book"):
    print(f"row{row}")