import sqlite3

connection_bdd = sqlite3.connect("album2.db")

sql_table_artist = """CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);"""

sql_table_album = """
CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    annee_sortie INTEGER);

"""

cursor = connection_bdd.cursor()

cursor.execute(sql_table_artist)
cursor.execute(sql_table_album)
cursor.execute("INSERT INTO artiste (nom) VALUES (\"Michael Jackson\")")
mj_id = cursor.lastrowid
cursor.execute("INSERT INTO artiste (nom) VALUES (\"Celine Dion\")")
cd_id = cursor.lastrowid
cursor.execute("INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (" + str(mj_id) + " , \"Thriller\", 1983);")
cursor.execute(
    "INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (" + str(cd_id) + ",\"Falling into You\", 1996);")
cursor.execute(
    "INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (" + str(cd_id) + ",\"Let's Talk About Love\", 1997);")

connection_bdd.commit()

connection_bdd.close()
