#Archivo de ejemplo 1 (Fichier d’exemple 1)

#   Bonjour: Hola/Buenos días
#   Salut: Hola (informal)
#   Bonsoir: Buenas tardes/Buenas noches
#   Coucou: Hola (informal y cariñoso)
#   Allô: Hola (se usa principalmente al contestar el teléfono)

#   Adieu – adiós (muy formal)
#   Au revoir – Adiós/ hasta la vista
#   À demain – hasta mañana
#   Salut!- ¡chao!
#   À plus tard – hasta luego
#   À plus! – hasta luego (más informal)
#   Je me tire! – ¡me piro!

#   Merci – Gracias
#   Merci beaucoup – Muchas gracias
#   Merci bien – Muchas gracias
#   Merci de tout coeur – Gracias de todo corazón
#   Merci infiniment – Infinitas gracias
#   C’est gentil – Eres muy amable
#   C`est vraiment très gentil de votre part – Es muy amable de tu parte 

#   S’il vous plaît – Por favor
#   Pourriez-vous répéter, s’il vous plaît? – ¿Podría repetir, por favor1
#   Pourriez-vous parler plus lentement, s’il vous plaît? – ¿Podría hablar más lentamente, por favor1
import os.path

listeSalutations=[]
listeAu_revoirs=[]
listeRemercier=[]
listeDemanderFaveur=[]

def write_le_mot(phrase):
    if os.path.exists('salutations.txt'):
        with open('salutations.txt','a') as f:
            f.writelines(f"{phrase}\n")
    else:
        with open('salutations.txt','w') as f:
            f.writelines(f"{phrase}\n")

def read_le_mot():
    if os.path.exists('salutations.txt'):
        with open('salutations.txt','r') as f:
            for linea in f:
                print(linea)
            f.close()
    else:
        print("Erreur: le fichier n'existe pas")

def introduire_salutation():
    phrase=input("Introduire une salutation: ")
    write_le_mot(phrase)


introduire_salutation()

def introduire_Au_revoir():
    return 0

def introduire_Remercier():
    return 0

def introduire_DemanderFaveur():
    return 0

def montrer_salutation():
    return 0

def montrer_Au_revoir():
    return 0

def montrer_Remercier():
    return 0

def montrer_DemanderFaveur():
    return 0

# def salutation():

#     print("Bonjour le monde")

# listeQuelquesMots1=('Bonjour','Au revoir','Merci',"S'il vous plaît")


# def montrer_le_mot(index):
    
#     print(listeQuelquesMots1[index])