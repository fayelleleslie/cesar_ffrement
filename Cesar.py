def cesar_chiffrer(message, cle):
    resultat = ""
    for i in range(len(message)):
        char = message[i]
        # Chiffrement des majuscules
        if char.isupper():
            resultat += chr((ord(char) + cle - 65) % 26 + 65)
        # Chiffrement des minuscules
        elif char.islower():
            resultat += chr((ord(char) + cle - 97) % 26 + 97)
        else:
            resultat += char
    return resultat

def cesar_dechiffrer(message, cle):
    # Déchiffrer, c'est chiffrer avec l'inverse de la clé
    return cesar_chiffrer(message, -cle)


# --- Bonus : Interface Utilisateur ---
if __name__ == "__main__":
    print("--- Code César ---")
    choix = input("1: Chiffrer | 2: Déchiffrer : ")
    message = input("Message : ")
    cle = int(input("Clé (nombre entier) : "))

    if choix == "1":
        print("Résultat chiffré :", cesar_chiffrer(message, cle))
    elif choix == "2":
        print("Résultat déchiffré :", cesar_dechiffrer(message, cle))
    else:
        print("Choix invalide.")