import sqlite3
import functools

import functions

db_connection = sqlite3.connect('sqlite.db')
print(db_connection)

db_cursor = db_connection.cursor()
print(db_cursor)

query1 = "SELECT * FROM demo"
db_cursor.execute(query1)
print("Reading 1 rows")
rows = db_cursor.fetchone()
print(rows)

db_cursor.execute(query1)
# print("Reading 3 rows")
# rows = db_cursor.fetchmany(3)
# print(rows)
functions.query_responder(db_cursor, "fetchmany", 3)


print("Reading all rows")
# rows = db_cursor.fetchall()
# for r in rows:
#    print(r)
functions.query_responder(db_cursor, "fetchall")

query2 = "INSERT INTO demo (Name, Hint) VALUES ('Gabriel', 'Aparicio')"
db_cursor.execute(query2)
db_connection.commit()

id = int(input("Enter your id rn!: "))
query3 = "SELECT * FROM demo WHERE ID > ?"
db_cursor.execute(query3, (id))
functions.query_responder(db_cursor, "fetchall")