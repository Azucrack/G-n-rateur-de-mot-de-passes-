import random #j'importe les bibliothèques random et string pour pas avoir á le coder
import string
# Je demande á ce que de 1 : il crée un mot de passe et de 2: á ce que le mot de passe fasse au moins 4 characters 
def generate_password(lengh):
    if lengh < 4:
        print("Le mot de passe doit être d'au moins de 4")

   #grace a l'importe string, je peut dire á mon logiciel que    
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digits = random.choice(string.digits)
    punctuaction = random.choice(string.punctuation)

    all_characters = string.ascii_letters + string.digits + string.punctuation
    rest = [random.choice(all_characters) for _ in range(lengh -4)]
    
    #Je fait en sorte que les 4 type de caractères soit dans la generation + rest pour dire que il remplie jusqu'au nombre demander part la personne 
    password_list = [lowercase, uppercase, digits, punctuaction] + rest

    #je met cette commande pour que quand la liste soit vraiment aléatoire
    random.shuffle(password_list)
    
    return "".join(password_list)


if __name__ == '__main__':
    length  = int(input("password length :"))
    password = generate_password(length)

    if password !="":
        print("password generate :", password)
        input("Press Enter to close...")


