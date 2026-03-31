def chiffrer(texte, clé):
    
    resultat = ""
    for chat in texte:
        if chat.isalpha():
            # Décalage pour les lettres majuscules
            if chat.isupper():
                base = ord('A')
            # Décalage pour les lettres minuscules
            else:
                base = ord('a')
            # Appliquer le décalage
            resultat += chr((ord(chat) - base + clé) % 26 + base)
        else:
            # Si ce n'est pas une lettre, on la laisse inchangée
            resultat += chat
    return resultat
# Exemple d'utilisation
texte = input("Entrez le texte à chiffrer : ")
clé = int(input("Entrez la clé de chiffrement : "))
print("resultat :", chiffrer(texte, clé))
