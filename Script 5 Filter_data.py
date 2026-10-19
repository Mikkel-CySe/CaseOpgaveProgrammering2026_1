"""
Script 5: Et script til at filtrere data (lave en udvælgelse med SELECT).
Her vises alle reparationer, der koster over 1000 kr.
"""

import sqlite3

conn = sqlite3.connect('workshop.db')
cursor = conn.cursor()

print("\n--- Service Hvor pris 1000 < 1250 ---")
cursor.execute("""
    SELECT * FROM workshop
    WHERE category = 'Service'
    AND price BETWEEN 1000 AND 1250
""")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]} | Beskrivelse: {row[1]} | Pris: {row[2]} kr. | Bil: {row[3]} | Kategori: {row[4]}")


print("\n--- Motor Hvor pris 1000 < 1250---")
cursor.execute("""
    SELECT * FROM workshop
    WHERE category = 'Motor'
    AND price BETWEEN 1000 AND 1250
""")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]} | Beskrivelse: {row[1]} | Pris: {row[2]} kr. | Bil: {row[3]} | Kategori: {row[4]}")

conn.close()