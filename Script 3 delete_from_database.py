"""
Script 3: Et script til at tømme tabellerne for data.
Her bruges DELETE FROM-kommandoen.
"""

import sqlite3

# Opretter forbindelse til databasen workshop.db
conn = sqlite3.connect('workshop.db')
cursor = conn.cursor()

# Sletter alle rækker fra tabellen workshop
cursor.execute("DELETE FROM workshop")

# Gemmer ændringerne i databasen
conn.commit()

# Lukker forbindelsen til databasen
conn.close()

# Udskriver en besked, når dataene er blevet slettet
print("Alt data fra databasen workshop.db er blevet ryddet!")