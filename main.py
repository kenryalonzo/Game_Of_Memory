import random
import time

# Fonction pour générer une séquence aléatoire de chiffres
def generer_sequence(longueur):
    sequence = []
    for _ in range(longueur):
        chiffre = random.randint(0, 9)
        sequence.append(chiffre)
    return sequence

# Fonction pour demander à l'utilisateur de mémoriser la séquence
def demander_sequence(longueur):
    print("Mémorisez la séquence suivante :")
    sequence = generer_sequence(longueur)
    print(sequence)
    time.sleep(3)  # Attendre 3 secondes pour permettre à l'utilisateur de mémoriser la séquence
    # Effacer la console pour masquer la séquence
    print("\033c")
    return sequence

# Fonction pour permettre à l'utilisateur de deviner la séquence
def deviner_sequence(sequence):
    print("Entrez la séquence que vous avez mémorisée (séparée par des espaces) :")
    reponse = input().split()
    reponse = [int(chiffre) for chiffre in reponse]
    if reponse == sequence:
        return True
    else:
        return False

# Boucle principale du jeu
def jouer_jeu():
    longueur = 4  # Commencer avec une séquence de 4 chiffres
    while True:
        sequence = demander_sequence(longueur)
        if deviner_sequence(sequence):
            print("Bravo ! Vous avez correctement mémorisé la séquence.")
            longueur += 1
        else:
            print("Dommage. Vous vous êtes trompé.")
            print("Votre score final est de", longueur-1)
            break

# Lancer le jeu
jouer_jeu()