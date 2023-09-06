# LES FONCTIONS : PROJET QUESTIONNAIRE
#
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse
#
# Question : Quelle est la capitale de l'Italie ?
#
# 4 questions
questionnaire = (
    ("Quel est le symbole utilisé pour assigner une valeur à une variable en Python ?", ("=", "+", "*", "/"), "="),
    ("Quel est le mot-clé utilisé pour définir une fonction en Python ?", ("def", "class", "function", "var"), "def"),
    ("Quel est le résultat de l'expression '5 % 2' en Python ?", ("2", "3", "4", "1"), "1"),
    ("Quel est le résultat de l'expression 'len('Hello World')' en Python ?", ("5", "10", "11", "2"), "11")

)


def demander_reponse_numerique_utilisateur(min, max):
    user_response_str = input(f"Entrez une réponse (entre {min} et {max}) : ")
    try:
        user_response_int = int(user_response_str)
        if min <= user_response_int <= max:
            return user_response_int
        print(f"ERREUR: Vous devez entrez un nombre entre {min} et {max}")
    except:
        print("ERREUR: Veuillez entrer uniquement une valeur numérique")
    return demander_reponse_numerique_utilisateur(min, max)


def poser_question(questions):
    titre_question = questions[0]
    choix = questions[1]
    good_response = questions[2]
    reponse_correcte = False
    print(f"Question : {titre_question}")
    for i in range(len(choix)):
        print(f"{i + 1}- {choix[i]}")
    response_int = demander_reponse_numerique_utilisateur(1, len(choix))
    if choix[response_int - 1].lower() == good_response.lower():
        print("Bonne réponse")
        reponse_correcte = True
    else:
        print("Mauvaise réponse")
    print()
    return reponse_correcte


def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print(f"Score final : {score} sur {len(questionnaire)}")


lancer_questionnaire(questionnaire)

# question("Quel est le symbole utilisé pour assigner une valeur à une variable en Python ?", "=", "+", "*", "/", "a")
# question("Quel est le mot-clé utilisé pour définir une fonction en Python ?", "def", "class", "function", "var", "a")
# question
#
# question("Quel est le résultat de l'expression 'len('Hello World')' en Python ?", "5", "10", "11", "2", "c")
#
