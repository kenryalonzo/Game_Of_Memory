import random
import time
import os

# Fonction pour effacer les informations à l'écran
def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def generer_sequence():
    sequence = ""
    for _ in range(4):
        chiffre = random.randint(0, 9)
        sequence += str(chiffre)
    return sequence

def afficher_sequence(sequence):
    clear_screen()
    print("Retenez la séquence :")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()

def demander_reponse():
    sequence_user = input("Votre réponse : ")
    return sequence_user

def afficher_resultat(score):
    clear_screen()
    print("Bonne réponse, votre score est :", score)
    time.sleep(1)

def afficher_score_final(sequence_correcte, score):
    clear_screen()
    print("Mauvaise réponse, la séquence était :", sequence_correcte)
    print("Votre score final :", score)

score = 0
rejouer = True

while rejouer:
    sequence_initiale = generer_sequence()
    sequence = sequence_initiale
    score = 0

    while True:
        afficher_sequence(sequence)
        sequence_user = demander_reponse()

        if sequence_user == sequence:
            score += 1
            sequence += str(random.randint(0, 9))
            afficher_resultat(score)
        else:
            afficher_score_final(sequence, score)
            break

    rejouer_input = input("Voulez-vous rejouer ? (oui/non) : ")
    if rejouer_input.lower() != "oui":
        rejouer = False
    else:
        continue
