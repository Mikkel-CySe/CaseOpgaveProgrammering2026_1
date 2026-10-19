# Script #6
# Et script til at tilføje én ny opgave i workshop-databasen,
# baseret på input fra brugeren. Hvert felt bliver valideret,
# så man fx ikke kan skrive tekst i prisen.

import sqlite3

conn = sqlite3.connect("workshop.db")
cursor = conn.cursor()

# De kategorier man må vælge imellem (de samme som i vores testdata)
kategorier = ["Service", "Bremser", "Dæk", "Olieskift", "Motor", "El", "Syn", "Karosseri", "Aircondition"]

print("=== Tilføj ny opgave til værkstedet ===")

# --- Felt 1: name (navnet på opgaven) ---
# Må ikke være tomt og må ikke kun bestå af tal
name = input("Navn på opgaven (fx Skift bremseklodser): ").strip()
while name == "" or name.isdigit():
    print("Fejl: Navnet må ikke være tomt og må ikke kun være tal.")
    name = input("Navn på opgaven: ").strip()

# --- Felt 2: price (pris i kr.) ---
# Må kun være et helt tal, og det skal være mellem 1 og 100000
price = input("Pris i kr. (kun hele tal): ").strip()
while not price.isdigit() or int(price) < 1 or int(price) > 100000:
    print("Fejl: Prisen skal være et helt tal mellem 1 og 100000 (ingen bogstaver).")
    price = input("Pris i kr.: ").strip()
price = int(price)  # laver teksten om til et tal

# --- Felt 3: vehiclemodel (bilmodel) ---
# Må ikke være tom og må ikke kun være tal
vehiclemodel = input("Bilmodel (fx VW Golf): ").strip()
while vehiclemodel == "" or vehiclemodel.isdigit():
    print("Fejl: Bilmodellen må ikke være tom og må ikke kun være tal.")
    vehiclemodel = input("Bilmodel: ").strip()

# --- Felt 4: category (kategori) ---
# Skal være en af kategorierne i listen
print("Mulige kategorier:", ", ".join(kategorier))
category = input("Kategori: ").strip().capitalize()
while category not in kategorier:
    print("Fejl: Kategorien findes ikke. Vælg en fra listen.")
    print("Mulige kategorier:", ", ".join(kategorier))
    category = input("Kategori: ").strip().capitalize()

# Vis hvad der bliver gemt, og spørg om brugeren vil gemme
print()
print("Du er ved at gemme:")
print("  Navn:     ", name)
print("  Pris:     ", price, "kr.")
print("  Bilmodel: ", vehiclemodel)
print("  Kategori: ", category)

svar = input("Vil du gemme? (j/n): ").strip().lower()
while svar != "j" and svar != "n":
    svar = input("Skriv j for ja eller n for nej: ").strip().lower()

if svar == "j":
    # Vi bruger ? i stedet for at sætte input direkte ind i SQL'en.
    # Det beskytter mod SQL-injection.
    cursor.execute("INSERT INTO workshop (name, price, vehiclemodel, category) VALUES (?, ?, ?, ?)",
                   (name, price, vehiclemodel, category))

    # ændringen skrives til vores db
    conn.commit()

    print("Opgaven er gemt med id", cursor.lastrowid)
else:
    print("Intet blev gemt.")

conn.close()