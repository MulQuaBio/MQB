import sqlite3

conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute("CrEATE TABLE tt (Val TEXT)")

conn.commit()

z = [('a',), ('ab',), ('abc',), ('b',), ('c',)]

c.executemany("INSErT INTO tt VALUES (?)", z)

conn.commit()

c.execute("SELECT * FrOM tt WHErE Val LIKE 'a%'").fetchall()

conn.close()
