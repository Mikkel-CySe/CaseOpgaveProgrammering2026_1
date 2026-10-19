"""
Script 4: Et script til at læse og vise al data i tabellerne. Her bruges SELECT statementet.
Data skal udskrives pænt i konsollen.
"""

import sqlite3

conn = sqlite3.connect('workshop.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM workshop")
rows = cursor.fetchall()

for row in rows[0:10]:
    print(f"ID: {row[0]} | Beskrivelse: {row[1]} | Pris: {row[2]} kr. | Bil: {row[3]} | Kategori: {row[4]}")

conn.close()