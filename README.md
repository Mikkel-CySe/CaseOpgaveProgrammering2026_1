# Car Workshop Database

## Beskrivelse
Dette projekt er udviklet som et Python-projekt med SQLite, der simulerer
et databasesystem til et autoværksted.

Databasen indeholder oplysninger om forskellige værkstedsopgaver,
herunder opgavens navn, pris, bilmodel og kategori.

Formålet er at arbejde med SQL og databaser gennem Python samt lære
at oprette tabeller, indsætte data, læse data, filtrere resultater
og slette data.

## Funktioner
- **Script 1 – Oprettelse af database:** Opretter databasen og tabellen `workshop`.
- **Script 2 – Testdata:** Indsætter 500 testopgaver i databasen.
- **Script 3 – Slet data:** Sletter alle registrerede opgaver fra tabellen.
- **Script 4 – Vis data:** Henter og viser opgaver fra databasen i konsollen.
- **Script 5 – Filtrering:** Filtrerer opgaver efter kategori og prisinterval.
- **Script 6 – Tilføj opgave:** Gør det muligt at registrere nye værkstedsopgaver via brugerinput med validering.

## Teknologier
- Python
- SQLite


## Installation og brug
1. Sørg for, at Python er installeret.
2. Download eller klon repository'et.
3. Kør Script 1 for at oprette databasen.
4. Kør Script 2 for at indsætte testdata.
5. Kør de øvrige scripts for at vise, filtrere, slette eller tilføje opgaver.

**Bemærk:** Script 3 sletter alle data i tabellen `workshop`.
Kør det derfor kun, hvis du ønsker at rydde databasen.
