"""
Script 4: Et script til at læse og vise al data i tabellerne. Her bruges SELECT statementet.
Data skal udskrives pænt i konsollen.
"""

import sqlite3
conn = sqlite3.connect('workshop.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM workshop")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()