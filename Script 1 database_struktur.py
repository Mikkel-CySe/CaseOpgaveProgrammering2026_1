"""
Script #1
Et script til at definere databasens tabelstruktur –
 hvis I har f.eks. to tabeller så også med en
fremmednøgle. I skal bruge CREATE TABLE-kommandoen
"""
import sqlite3
conn = sqlite3.connect('workshop.db')
cursor = conn.cursor()

# Databasen laves herved:
cursor.execute("""
CREATE TABLE IF NOT EXISTS workshop (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price integer,
    vehiclemodel TEXT,
    category TEXT
)
""")

conn.commit()
conn.close()

print("Databasen er oprettet!")