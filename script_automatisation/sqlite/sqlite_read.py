import sqlite3

connection_bdd = sqlite3.connect("album2.db")

cursor = connection_bdd.cursor()

# cursor.execute('SELECT * FROM artiste')
# artistes = cursor.fetchall()
# print(artistes)
#
# cursor.execute('SELECT * FROM album')
# albums = cursor.fetchall()
# print(albums)
#
# for artiste in cursor.execute('SELECT * FROM artiste'):
#     print(artiste)

album_cd = cursor.execute(
    'SELECT titre FROM album a JOIN artiste ar ON a.artiste_id = ar.artiste_id AND ar.nom = "Celine Dion"').fetchall()
print(album_cd)
connection_bdd.close()
