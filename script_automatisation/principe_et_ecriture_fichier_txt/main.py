# f = open("mon_fichier.txt", "a")
#
# f.write("Bonjour \n")
#
# f.close


# f = open("nombres.txt", "w")
#
# for i in range(10):
#     f.write(f"{i + 1}\n")
#
# # f.close()
#
# f = open("mon_fichier.txt", "r")
#
# txt = f.read()
#
#
# # txt = f.readlines()  # renvoie une collections
# # -> [' Bonjour\n', 'Bonjour \n', 'Bonjour \n', 'Bonjour \n', 'Bonjour \n', 'Bonjour \n', 'Bonjour \n']
#
#
# print(txt)

import os.path

if not os.path.exists("newrep"):
    os.mkdir("newrep")

if os.path.exists("nexrep"):
    os.rmdir("nexrep")


filename = os.path.join("rep", "mon_fichier.txt")

print(filename)

print(os.path.exists(filename))

