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
#   Merci infiniment – Michisimas gracias
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
nom_fichier=""


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
    extension = '.py'
    fichiers = (fichier for fichier in os.listdir(chemin) if not fichier.endswith(extension) and os.path.isfile(os.path.join(chemin, fichier)))

# Fonction normale
    # for fichier in fichiers:
    #     listeDeFichiers.append(fichier)
    # for i in listeDeFichiers:
    #     print(i)
# Fonctionnalité avancée 1 (fonction: .extend)
    global listeDeFichiers
    listeDeFichiers.extend(fichiers)
    for index,fichier in enumerate(listeDeFichiers):
# Fonctionnalité avancée 2 (fonction: .split('.')[0])
        global nom_fichier
        nom_fichier = fichier.split('.')[0]
        print(f"{index}: {nom_fichier}")
    
    
    

# Lire les mots/phrases du fichier
def read_le_fichier():
    listes_de_fichers()
    global listeDeFichiers
    limit=len(listeDeFichiers)
    option=0
    while option != limit:
        print(f"\nNuméro du fichier que vous voulez lire ou (",limit,") pour sortir: ",end='')
        try:
            option=int(input())
        except ValueError:
            print(f"Error: Ingrese un valor entero (0-{limit-1})")
            continue
        if option>=0 and option<=limit-1:
        
            fichier=listeDeFichiers[option]
            chemin_complet=os.path.join(chemin,fichier)
            
            with open(chemin_complet,'r') as f:
                    global nom_fichier
                    nom_fichier=fichier.split('.')[0]
                    print(f"\n\t\t{nom_fichier}")
                    for linea in f:
                        print(f"{linea}",end='')
                    print("")
                    f.close()
                    
                    listeDeFichiers=[]
                    option=limit
                    

        elif option == limit:
            listeDeFichiers=[]
            print("Saliendo...")

        else:
            print(f"Error: Ingrese un valor entero (0-{limit-1})")
            




# Entrez l'expression et le nom du fichier où l’expression sera enregistrée
def introduire_le_expression():
    phrase=input("Introduire le mot/phrase:\n")
    
    

    op = 0
    while op != 3:
        print("\nOpciones para guardar la palabra/frase:\n")
        print("1. Guardar en archivo existente","\n2. Guardar en nuevo archivo","\n3. Volver al menu anterior")
        try:
            op=int(input("\nElije una opción: "))
        except ValueError:
            print("Error: Ingrese un valor entero (0-3)")
            continue
        if op == 1:

            print("\t\tFichiers disponibles")
            listes_de_fichers()
            global listeDeFichiers
            option=-1
            limit=len(listeDeFichiers)
            while option != limit:
                print("\nNuméro du fichier que vous voulez écrire ou la touche (",limit,") pour sortir: ",end='')
                try:
                    option=int(input())
                except ValueError:
                    print(f"Error: Ingrese un valor entero (0-{limit-1})")
                    continue
                if option>=0 and option<=limit-1:

                    fichier=listeDeFichiers[option]
                    chemin_complet=os.path.join(chemin,fichier)
                    write_le_fichier(phrase,chemin_complet)
                    listeDeFichiers=[]
                    option=limit
                    op=3
                    input("Preione una tecla para salir al menu enterior")
                    
                elif option == limit:
                    op=3
                    print("Saliendo")
                else:
                    print(f"Error: Ingrese un valor entero (0-{limit-1})")
            
            listeDeFichiers=[]


        elif op == 2:

            fichier=input("Nom du fichier auquel vous souhaitez ajouter le mot/phrase: ")
            chemin_complet=os.path.join(chemin,fichier)
            if os.path.exists(chemin_complet):
                print("El archivo ya existe: ","\n1. Guardar","\n2. Salir")
                option=0
                while option != 2:
                    print("Selecciona la opcion (1-2): ",end="")
                    try:
                        option=int(input())
                    except ValueError:
                        print("Error: Ingrese un valor entero (1-2)")
                        continue
                    if option == 1:
                        write_le_fichier(phrase,chemin_complet)
                        option=2
                        op=3
                        input("Preione una tecla para salir al menu enterior")
                    elif option == 2:
                        option=2
                        op=3
                    else:
                        print("Error: Ingrese un valor entero (1-2)")

                    
            else:
            
                write_le_fichier(phrase,chemin_complet)
                op=3
                input("Preione una tecla para salir al menu enterior")

        elif op== 3:
            print("Volviendo al menu anterior\n")

        else:
            print("Error: Ingrese un valor entero (0-3)")




# Fonction principal
def main_fonction_1():
    op = 0
    while op != 3:
        print("\n\t\tMenu Diccionario\n")
        print(f'1. Ajouter une nouvelle phrase au dictionnaire',"\n2. Listes d'expressions",'\n3. Quitter le menu principale')
        try:
            op = int(input('\nElije una opción (1-3): '))
        except ValueError:
            print('Ingresa un número entero (1-3)')
            continue
        if op == 1:
            print("\n\tAjouter une nouvelle mot/phrase\n")
            introduire_le_expression()
        elif op == 2:
            print("\n\t\tLista de Expresiones")
            read_le_fichier()
        elif op == 3:
            print("\nVolviendo al menu principal\n")
        else:
            print('Ingresa una opción válida (1-3)')