"""
Script 2: Bulk-insert af testdata i bilværksted-databasen.

Læser INSERT INTO-statements fra filen data.sql (genereret med en LLM)
og kører dem mod databasen. Kræver at tabellerne allerede er oprettet
med script 1 (create_tables).
"""

import sqlite3
import os

# Navnet på databasefilen og SQL-filen med testdata
DATABASE_FIL = "vaerksted.db"
DATA_FIL = "data.sql"


def laes_sql_fil(filsti):
    """Læser hele SQL-filen og returnerer indholdet som tekst."""
    with open(filsti, "r", encoding="utf-8") as fil:
        return fil.read()


def bulk_insert():
    """Indsætter alle testdata fra data.sql i databasen."""

    # Tjek at databasen og datafilen findes, før vi går i gang
    if not os.path.exists(DATABASE_FIL):
        print(f"Fejl: Databasen '{DATABASE_FIL}' findes ikke. Kør først script 1.")
        return
    if not os.path.exists(DATA_FIL):
        print(f"Fejl: Datafilen '{DATA_FIL}' blev ikke fundet.")
        return

    sql_kommandoer = laes_sql_fil(DATA_FIL)

    forbindelse = sqlite3.connect(DATABASE_FIL)
    cursor = forbindelse.cursor()

    try:
        # Slå fremmednøgler til, så en reparation ikke kan pege på en bil der ikke findes
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Kør alle INSERT-statements som én transaktion,
        # så enten kommer alle data ind, eller ingen af dem
        cursor.executescript("BEGIN;\n" + sql_kommandoer + "\nCOMMIT;")
        forbindelse.commit()

        # Tæl hvor mange rækker der nu er i hver tabel
        antal_biler = cursor.execute("SELECT COUNT(*) FROM biler").fetchone()[0]
        antal_reparationer = cursor.execute("SELECT COUNT(*) FROM reparationer").fetchone()[0]

        print("Bulk-insert gennemført!")
        print(f"  Biler i databasen:        {antal_biler}")
        print(f"  Reparationer i databasen: {antal_reparationer}")

    except sqlite3.IntegrityError as fejl:
        # Sker fx hvis en nummerplade allerede findes (UNIQUE), eller hvis tabellerne ikke er tømt
        forbindelse.rollback()
        print(f"Fejl ved indsættelse: {fejl}")
        print("Tip: Kør script 3 (tøm tabeller) og prøv igen.")

    except sqlite3.Error as fejl:
        forbindelse.rollback()
        print(f"Databasefejl: {fejl}")

    finally:
        forbindelse.close()


if __name__ == "__main__":
    bulk_insert()