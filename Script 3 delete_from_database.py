"""
Script 3: Et script til at tømme tabellerne for data. Her bruges DELETE FROM kommandoen.
"""

import sqlite3
conn = sqlite3.connect('workshop.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM workshop")
conn.commit()

conn.close()
print("Alt data fra databasen workshop.db er blevet ryddet!")