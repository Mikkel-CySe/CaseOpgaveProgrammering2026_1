"""
Script 5: Et script til at filtrere data (lave en udvælgelse med SELECT). Det kunne f.eks. være alle students der
bor i Esbjerg.
"""

import sqlite3
conn = sqlite3.connect('workshop.db')
cursor = conn.cursor()