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
def demander_sequence(sequence):
    print("Mémorisez la séquence suivante :")
    print("".join(map(str, sequence)))
    time.sleep(3)  # Attendre 3 secondes pour permettre à l'utilisateur de mémoriser la séquence
    # Effacer la console pour masquer la séquence
    print("\033c")

# Fonction pour permettre à l'utilisateur de deviner la séquence
def deviner_sequence(sequence):
    print("Entrez la séquence que vous avez mémorisée (sans espaces) :")
    reponse = input()
    reponse = [int(chiffre) for chiffre in reponse]
    if reponse == sequence:
        return True
    else:
        return False

# Boucle principale du jeu
def jouer_jeu():
    sequence_base = generer_sequence(4)
    sequence = sequence_base.copy()
    longueur = 4
    score = 0
    while True:
        demander_sequence(sequence)
        if deviner_sequence(sequence):
            chiffre = random.randint(0, 9)
            sequence.append(chiffre)
            longueur += 1
            score += 1
        else:
            print("Dommage. Vous vous êtes trompé.")
            print("Votre score final est de", score)
            print("La dernière séquence était :", "".join(map(str, sequence)))
            break

# Lancer le jeu
jouer_jeu()