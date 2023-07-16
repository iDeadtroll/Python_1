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
import os

listeSalutations=[]
listeAu_revoirs=[]
listeRemercier=[]
listeDemanderFaveur=[]

def write_le_mot(phrase,fichier):
    if os.path.exists(fichier):
        with open(fichier,'a') as f:
            f.writelines(f"{phrase}\n")
    else:
        with open(fichier,'w') as f:
            f.writelines(f"{phrase}\n")

def read_le_mot():
    fichier=input("Nom du fichier que vous souhaitez lire: ")
    if os.path.exists(fichier):
        with open(fichier,'r') as f:
            for linea in f:
                print(linea)
            f.close()
    else:
        print("Erreur: le fichier n'existe pas")

def introduire_le_mot():
    phrase=input("Introduire le mot: ")
    fichier=input("Nom du fichier auquel vous souhaitez ajouter le mot: ")
    write_le_mot(phrase,fichier)

def listes_de_mots():
    chemin = '/ruta/del/directorio'
    fichiers = os.listdir(chemin)

    for fichier in fichiers:
        print(fichier)

introduire_le_mot()


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