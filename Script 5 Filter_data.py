"""
Script 5: Et script til at filtrere data (lave en udvælgelse med SELECT).
Her vises reparationer i kategorierne Service og Motor,
hvor prisen er mellem 1000 og 1250 kr.
"""

import sqlite3

# Opretter forbindelse til databasen
conn = sqlite3.connect('workshop.db')
cursor = conn.cursor()

# Udskriver en overskrift for Service-kategorien
print("\n--- Service Hvor pris 1000 < 1250 ---")

# Henter alle reparationer i kategorien Service,
# hvor prisen er mellem 1000 og 1250 kr.
cursor.execute("""
    SELECT * FROM workshop
    WHERE category = 'Service'
    AND price BETWEEN 1000 AND 1250
""")

# Henter alle rækker, som matcher forespørgslen
rows = cursor.fetchall()

# Gennemgår og udskriver hver reparation
for row in rows:
    print(f"ID: {row[0]} | Beskrivelse: {row[1]} | Pris: {row[2]} kr. | Bil: {row[3]} | Kategori: {row[4]}")


# Udskriver en overskrift for Motor-kategorien
print("\n--- Motor Hvor pris 1000 < 1250 ---")

# Henter alle reparationer i kategorien Motor,
# hvor prisen er mellem 1000 og 1250 kr.
cursor.execute("""
    SELECT * FROM workshop
    WHERE category = 'Motor'
    AND price BETWEEN 1000 AND 1250
""")

# Henter alle rækker, som matcher forespørgslen
rows = cursor.fetchall()

# Gennemgår og udskriver hver reparation
for row in rows:
    print(f"ID: {row[0]} | Beskrivelse: {row[1]} | Pris: {row[2]} kr. | Bil: {row[3]} | Kategori: {row[4]}")


# Lukker forbindelsen til databasen
conn.close()