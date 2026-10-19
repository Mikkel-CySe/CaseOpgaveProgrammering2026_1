"""
Script 4: Et script til at læse og vise al data i tabellerne.
Her bruges SELECT statementet.
Data udskrives pænt i konsollen.
"""

import sqlite3

# Opretter forbindelse til databasen workshop.db
conn = sqlite3.connect('workshop.db')
cursor = conn.cursor()

# Henter alle data fra tabellen workshop
cursor.execute("SELECT * FROM workshop")
rows = cursor.fetchall()

# Gennemgår og udskriver de første 10 rækker fra databasen
for row in rows[0:10]:
    # Udskriver oplysningerne om hver reparation
    print(f"ID: {row[0]} | Beskrivelse: {row[1]} | Pris: {row[2]} kr. | Bil: {row[3]} | Kategori: {row[4]}")

# Lukker forbindelsen til databasen
conn.close()