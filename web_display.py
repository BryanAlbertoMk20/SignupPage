#!/usr/bin/env python3

import pymysql as mydb

print("Content-Type: text/html \n")

print("""
    <html>
    <head>
    <title>Displaying Data</title>
    </head>
    <body bgcolor="lightyellow"> 
    <h1><center>User Data Retrieved From The DataBase <center></h1>
""")

select = " SELECT * FROM game_signup"

try:
    dbConn = mydb.connect(host="localhost", user="alberto", password="alberto", database="alberto", port=3306)

except mydb.Error as e:
    print("Could not establish connection", e)
    print(e.errno + e.msg)

data = []

cursor = dbConn.cursor()

cursor.execute(select)

row = cursor.fetchone()
while row is not None:
    data.append(row)
    row = cursor.fetchone()

print('''
    <br>
    <table border=3 width=600 height=400 style="margin-left:auto; margin-right:auto;">
    <tr bgcolor=tan>
    <th>Player ID</th><th>Player Name</th><th>First Name</th><th>Last Name</th><th>D.O.B</th><th>Country</th><th>Email Address</th><th>Password</th>
''')
for row in data:
    print('<tr>', end="")
    for column in row:
        print('<td align=center>', column, '</td>',end="")
    print('</tr>')

print('''
    </table>
    </body>
    </html>
''')
