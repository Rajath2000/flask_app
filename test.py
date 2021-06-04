# import sqlite3

# conn = sqlite3.connect("DepartmentSite.db")
# cur = conn.cursor()
# username="rajathmr2000@gmail.com"
# pas="1234"
# try:
#     rows=cur.execute("""SELECT * FROM User WHERE username=(?) AND pass=(?)""",(username,pas))
#     rows=rows.fetchall()
#     print(len(rows))
#     for i in rows:
#         print(i)
# except Exception as err:
#     print(err)
# finally:
#     conn.close()

import sqlite3

conn = sqlite3.connect("DepartmentSite.db")
cur = conn.cursor()
cur.execute("""DROP TABLE FacultyDetails """)
conn.commit()
conn.close()