import sqlite3

# Forbind til databasen (filen bliver oprettet hvis den ikke findes)
conn = sqlite3.connect("bulk_data.db")
cursor = conn.cursor()

# Opret tabellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    age INTEGER,
    city TEXT,
    created TEXT
)
""")

# 100 INSERT INTO-statements genereret af en LLM
inserts = [
    "INSERT INTO users (username, email, age, city, created) VALUES ('ahmadnie4', 'ahmadnie4@mail.dk', 65, 'Vejle', '2026-04-08')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('mikkelkri14', 'mikkelkri14@mail.dk', 61, 'Billund', '2026-09-03')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('noahlar5', 'noahlar5@mail.dk', 19, 'Tjæreborg', '2026-04-08')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('williamjør4', 'williamjør4@mail.dk', 53, 'Varde', '2026-09-14')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('idasør76', 'idasør76@mail.dk', 35, 'Esbjerg', '2026-03-23')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('clarachr36', 'clarachr36@mail.dk', 27, 'Varde', '2026-06-04')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('larslar13', 'larslar13@mail.dk', 40, 'Kolding', '2026-10-09')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('mettekri59', 'mettekri59@mail.dk', 52, 'Tjæreborg', '2026-07-03')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('majaand81', 'majaand81@mail.dk', 57, 'Kolding', '2026-10-07')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('alinie6', 'alinie6@mail.dk', 60, 'Varde', '2026-05-03')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('idatho13', 'idatho13@mail.dk', 42, 'Vejle', '2026-08-21')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('frejahan48', 'frejahan48@mail.dk', 40, 'Varde', '2026-05-23')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('saramad10', 'saramad10@mail.dk', 56, 'Skive', '2026-03-18')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('noraped21', 'noraped21@mail.dk', 47, 'Aarhus', '2026-05-21')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('aliras29', 'aliras29@mail.dk', 61, 'Kolding', '2026-01-08')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('metteols41', 'metteols41@mail.dk', 43, 'Vejle', '2026-02-07')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('noahpou92', 'noahpou92@mail.dk', 38, 'Varde', '2026-08-13')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('ahmadsør19', 'ahmadsør19@mail.dk', 34, 'Ribe', '2026-04-24')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('majaras34', 'majaras34@mail.dk', 65, 'Herning', '2026-07-19')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('oliverchr29', 'oliverchr29@mail.dk', 26, 'København', '2026-08-03')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emiljen15', 'emiljen15@mail.dk', 27, 'Skive', '2026-03-26')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('saralar77', 'saralar77@mail.dk', 22, 'Aarhus', '2026-07-20')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('lucasras33', 'lucasras33@mail.dk', 53, 'Esbjerg', '2026-02-22')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('majaols35', 'majaols35@mail.dk', 59, 'Kolding', '2026-02-10')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('clarahan59', 'clarahan59@mail.dk', 18, 'Billund', '2026-05-17')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emilhan65', 'emilhan65@mail.dk', 24, 'Skive', '2026-05-27')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('ahmadras78', 'ahmadras78@mail.dk', 30, 'Ribe', '2026-06-25')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emmaras68', 'emmaras68@mail.dk', 18, 'Herning', '2026-06-16')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('andersnie47', 'andersnie47@mail.dk', 37, 'Varde', '2026-01-08')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('noahnie11', 'noahnie11@mail.dk', 64, 'Odense', '2026-02-25')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('majaols17', 'majaols17@mail.dk', 26, 'Skive', '2026-08-18')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emmaand68', 'emmaand68@mail.dk', 56, 'Aarhus', '2026-04-18')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emilkri89', 'emilkri89@mail.dk', 30, 'Billund', '2026-05-13')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('saramad48', 'saramad48@mail.dk', 46, 'København', '2026-08-04')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('idaped9', 'idaped9@mail.dk', 39, 'Esbjerg', '2026-10-18')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('idajør29', 'idajør29@mail.dk', 18, 'Tjæreborg', '2026-01-08')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('larspou5', 'larspou5@mail.dk', 39, 'Tjæreborg', '2026-09-08')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('frederikmad63', 'frederikmad63@mail.dk', 31, 'København', '2026-03-24')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('noahjør61', 'noahjør61@mail.dk', 33, 'Odense', '2026-07-07')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('sofienie85', 'sofienie85@mail.dk', 45, 'Kolding', '2026-07-14')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('lucastho94', 'lucastho94@mail.dk', 21, 'Skive', '2026-02-02')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('oliverkri44', 'oliverkri44@mail.dk', 24, 'Varde', '2026-04-07')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('majasør18', 'majasør18@mail.dk', 45, 'Ribe', '2026-05-15')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('idatho10', 'idatho10@mail.dk', 46, 'København', '2026-02-02')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('ahmadras2', 'ahmadras2@mail.dk', 23, 'Varde', '2026-03-14')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('annasør28', 'annasør28@mail.dk', 43, 'Esbjerg', '2026-03-13')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('anderslar34', 'anderslar34@mail.dk', 47, 'Vejle', '2026-07-23')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('noraols72', 'noraols72@mail.dk', 60, 'Billund', '2026-08-05')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('jonasand28', 'jonasand28@mail.dk', 21, 'Herning', '2026-09-02')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('norachr8', 'norachr8@mail.dk', 21, 'Herning', '2026-08-17')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('williamhan8', 'williamhan8@mail.dk', 50, 'Tjæreborg', '2026-03-03')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('julienie87', 'julienie87@mail.dk', 33, 'Aarhus', '2026-02-19')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('idajør77', 'idajør77@mail.dk', 20, 'Herning', '2026-02-14')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('sarajør73', 'sarajør73@mail.dk', 51, 'Kolding', '2026-05-07')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('sarakri41', 'sarakri41@mail.dk', 33, 'Vejle', '2026-07-05')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('saramad39', 'saramad39@mail.dk', 47, 'Kolding', '2026-02-01')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('lucasjør73', 'lucasjør73@mail.dk', 24, 'Tjæreborg', '2026-09-07')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('williamand17', 'williamand17@mail.dk', 40, 'Tjæreborg', '2026-04-12')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('laurahan57', 'laurahan57@mail.dk', 52, 'Billund', '2026-05-20')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('saratho71', 'saratho71@mail.dk', 37, 'Skive', '2026-02-05')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('frederiknie14', 'frederiknie14@mail.dk', 65, 'København', '2026-03-09')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('laurajør27', 'laurajør27@mail.dk', 63, 'Kolding', '2026-04-22')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('ahmadtho34', 'ahmadtho34@mail.dk', 50, 'Odense', '2026-05-28')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('mettenie82', 'mettenie82@mail.dk', 45, 'Vejle', '2026-01-01')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('mathiasols17', 'mathiasols17@mail.dk', 58, 'Vejle', '2026-03-24')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('lucasras91', 'lucasras91@mail.dk', 45, 'København', '2026-01-04')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('larspou89', 'larspou89@mail.dk', 27, 'København', '2026-01-27')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('frejajør71', 'frejajør71@mail.dk', 27, 'Aarhus', '2026-03-02')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('laurachr6', 'laurachr6@mail.dk', 40, 'Varde', '2026-04-22')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('sofiechr72', 'sofiechr72@mail.dk', 44, 'Herning', '2026-03-08')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emmaols23', 'emmaols23@mail.dk', 44, 'Esbjerg', '2026-03-24')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('mathiasols53', 'mathiasols53@mail.dk', 60, 'Billund', '2026-04-09')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emmaols90', 'emmaols90@mail.dk', 24, 'Aarhus', '2026-01-28')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('annaped26', 'annaped26@mail.dk', 47, 'Kolding', '2026-05-27')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('idaped4', 'idaped4@mail.dk', 60, 'Varde', '2026-07-11')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('frederiktho9', 'frederiktho9@mail.dk', 35, 'Kolding', '2026-09-13')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('saratho69', 'saratho69@mail.dk', 39, 'Esbjerg', '2026-02-09')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emmajør34', 'emmajør34@mail.dk', 20, 'Tjæreborg', '2026-10-14')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('frejakri41', 'frejakri41@mail.dk', 45, 'Herning', '2026-09-04')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('oliverpou74', 'oliverpou74@mail.dk', 30, 'Vejle', '2026-01-23')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('clarajen67', 'clarajen67@mail.dk', 52, 'Skive', '2026-04-12')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('claranie86', 'claranie86@mail.dk', 39, 'Herning', '2026-06-22')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('sofiekri39', 'sofiekri39@mail.dk', 50, 'Vejle', '2026-07-11')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('oliverkri38', 'oliverkri38@mail.dk', 53, 'Ribe', '2026-04-14')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('saralar87', 'saralar87@mail.dk', 65, 'Ribe', '2026-10-19')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('lauralar71', 'lauralar71@mail.dk', 18, 'Vejle', '2026-05-07')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('claraols75', 'claraols75@mail.dk', 56, 'Skive', '2026-06-15')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('lucassør87', 'lucassør87@mail.dk', 31, 'København', '2026-08-26')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('norahan85', 'norahan85@mail.dk', 23, 'Vejle', '2026-09-22')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('ahmadjør43', 'ahmadjør43@mail.dk', 23, 'Varde', '2026-05-08')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('jonashan4', 'jonashan4@mail.dk', 20, 'Varde', '2026-08-20')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emilnie59', 'emilnie59@mail.dk', 44, 'Skive', '2026-10-07')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('alikri50', 'alikri50@mail.dk', 49, 'Aarhus', '2026-04-05')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('ahmadkri1', 'ahmadkri1@mail.dk', 24, 'Aarhus', '2026-04-06')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('aliras60', 'aliras60@mail.dk', 21, 'København', '2026-04-28')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('sofiesør18', 'sofiesør18@mail.dk', 47, 'Skive', '2026-09-18')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('juliechr97', 'juliechr97@mail.dk', 46, 'Herning', '2026-09-14')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('majasør21', 'majasør21@mail.dk', 65, 'Odense', '2026-08-09')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('emilped82', 'emilped82@mail.dk', 35, 'København', '2026-08-21')",
    "INSERT INTO users (username, email, age, city, created) VALUES ('idaand57', 'idaand57@mail.dk', 22, 'Billund', '2026-05-08')",
]

# Kør alle statements med et loop
for statement in inserts:
    cursor.execute(statement)

conn.commit()

# Tjek at det virkede
cursor.execute("SELECT COUNT(*) FROM users")
antal = cursor.fetchone()
print("Antal rækker i users:", antal[0])

# Vis de første 5 rækker
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows[:5]:
    print(row)

conn.close()