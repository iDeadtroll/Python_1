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
#   Pourriez-vous répéter, s’il vous plaît? – ¿Podría repetir, por favor?
#   Pourriez-vous parler plus lentement, s’il vous plaît? – ¿Podría hablar más lentamente, por favor?
import os.path
import os


listeSalutations=[]
listeAu_revoirs=[]
listeRemercier=[]
listeDemanderFaveur=[]
listeDeFichiers=[]
chemin = '/home/developer/Git-Repos/Git-Basic/ejemplo1'
# chemin_complet=""
# écrire le mot/phrase dans le fichier
def write_le_fichier(phrase,chemin_complet):
    if os.path.exists(chemin_complet):
        with open(chemin_complet,'a') as f:
            f.writelines(f"{phrase}\n")
    else:
        with open(chemin_complet,'w') as f:
            f.writelines(f"{phrase}\n")



# Afficher les fichier avec l'extension '.txt' d'un chemin
def listes_de_fichers():
    extension = '.txt'
    fichiers = (fichier for fichier in os.listdir(chemin) if fichier.endswith(extension))
# Fonction normale
    # for fichier in fichiers:
    #     listeDeFichiers.append(fichier)
    # for i in listeDeFichiers:
    #     print(i)
# Fonctionnalité avancée 1 (fonction: .extend)
    listeDeFichiers.extend(fichiers)
    for index,fichier in enumerate(listeDeFichiers):
# Fonctionnalité avancée 2 (fonction: .split('.')[0])
        nom_fichier = fichier.split('.')[0]
        print(f"{index}: {nom_fichier}")



# lire les mots/phrases du fichier
def read_le_fichier():
    # fichier=input("Nom du fichier que vous souhaitez lire: ")
    listes_de_fichers()
    option=int(input("Numéro du fichier que vous voulez lire: "))
    fichier=listeDeFichiers[option]
    chemin_complet=os.path.join(chemin,fichier)
    if os.path.exists(chemin_complet):
        with open(chemin_complet,'r') as f:
            for linea in f:
                print(linea)
            f.close()
    else:
        print("Erreur: le fichier n'existe pas")




# Entrez l'expression et le nom du fichier où l’expression sera enregistrée
def introduire_le_expression():
    phrase=input("Introduire le mot/phrase: ")
    fichier=input("Nom du fichier auquel vous souhaitez ajouter le mot/phrase: ")
    chemin_complet=os.path.join(chemin,fichier)
    write_le_fichier(phrase,chemin_complet)



# Fonction principal
def main_fonction_1():
    op = 0
    while op != 3:
        print(f'1. Agregar nueva frase/palabra al diccionario','\n2. Listas de expresiones','\n3. Salir al menu principal')
        try:
            op = int(input('Elije una opción: '))
        except ValueError:
            print('Ingresa un número válido')
            continue
        if op == 1:
            introduire_le_expression()
        elif op == 2:
            read_le_fichier()
        elif op == 3:
            print("\nVolviendo al menu principal\n")
        else:
            print('Ingresa una opción válida')