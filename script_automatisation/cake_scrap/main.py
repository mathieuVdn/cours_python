from bs4 import BeautifulSoup

f = open("recette.html", "r")
html_content = f.read()
f.close()
body = BeautifulSoup(html_content, "html.parser")

titre_h1 = body.find("h1")

print(f"Titre de la page : {titre_h1.text}")

p_description = body.find("p", "description")

print(f"Description de la page : {p_description.text}")

img_src = body.find("img", "centre")

print(f"La source de l'image de la page : {img_src['src']}")
