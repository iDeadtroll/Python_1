
import os.path
import os
import time

listeDeFichiers=[]
chemin = 'C:/Users/joni-/Documents/GitHub/Python_1/ejemplo1'
#chemin = '/home/developer/Git-Repos/Git-Basic/ejemplo1'
nom_fichier=""


# Écrire le mot/phrase dans le fichier
def write_le_fichier(phrase,chemin_complet):
    if os.path.exists(chemin_complet):
        with open(chemin_complet,'a',encoding='utf-8') as f:
            f.writelines(f"{phrase}\n")
    else:
        with open(chemin_complet,'w',encoding='utf-8') as f:
            f.writelines(f"{phrase}\n")




# Afficher les fichier avec l'extension '.txt' d'un chemin
# Afficher les fichier sans l'extension '.py' d'un chemin
# Afficher uniquement les fichiers d'un chemin sauf les fichiers avec l'extension ‘.py’
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
            print(f"Erreur: Entrez une valeur entière (0-{limit-1})")
            continue
        if option>=0 and option<=limit-1:
        
            fichier=listeDeFichiers[option]
            chemin_complet=os.path.join(chemin,fichier)
            
            with open(chemin_complet,'r',encoding='utf-8') as f:
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
            print("Quitter...")

        else:
            print(f"Entrez un numéro valide (0-{limit-1})")
            




# Entrez l'expression et le nom du fichier où l'expression sera enregistrée
def introduire_le_expression():
    phrase=input("Introduire le mot/phrase:\n")
    
    

    op = 0
    while op != 3:
        print("\nOptions pour enregistrer le mot/phrase:\n")
        print("1. Enregistrer dans le fichier existant","\n2. Enregistrer dans un nouveau fichier","\n3. Revenir au menu précédent")
        try:
            op=int(input("\nChoisissez une option: "))
        except ValueError:
            print("Erreur: Entrez une valeur entière (0-3)")
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
                    print(f"Erreur: Entrez une valeur entière (0-{limit-1})")
                    continue
                if option>=0 and option<=limit-1:

                    fichier=listeDeFichiers[option]
                    chemin_complet=os.path.join(chemin,fichier)
                    write_le_fichier(phrase,chemin_complet)
                    listeDeFichiers=[]
                    option=limit
                    op=3
                    input("Appuyez sur 'entrer' pour revenir au menu précédent")
                    
                elif option == limit:
                    op=3
                    print('Quitter...')
                    time.sleep(2)
                else:
                    print(f"Entrez un numéro valide (0-{limit-1})")
            
            listeDeFichiers=[]


        elif op == 2:

            fichier=input("Nom du fichier auquel vous souhaitez ajouter le mot/phrase: ")
            chemin_complet=os.path.join(chemin,fichier)
            if os.path.exists(chemin_complet):
                print("Le fichier existe déjà: ","\n1. Enregistrer","\n2.  Quitter")
                option=0
                while option != 2:
                    print("Choisissez une option (1-2): ",end="")
                    try:
                        option=int(input())
                    except ValueError:
                        print("Erreur: Entrez une valeur entière (1-2)")
                        continue
                    if option == 1:
                        write_le_fichier(phrase,chemin_complet)
                        option=2
                        op=3
                        input("Appuyez sur 'entrer' pour revenir au menu précédent")
                    elif option == 2:
                        option=2
                        op=3
                    else:
                        print("Entrez un numéro valide (1-2)")

                    
            else:
            
                write_le_fichier(phrase,chemin_complet)
                op=3
                input("Appuyez sur 'entrer' pour revenir au menu précédent")

        elif op== 3:
            print("Retour au menu principal\n")

        else:
            print("Entrez un numéro valide (1-3)")




# Fonction principal
def main_fonction_1():
    op = 0
    while op != 3:
        print("\n\t\tMenu Dictionnaire\n")
        print(f'1. Ajouter une nouvelle phrase au dictionnaire',"\n2. Listes d'expressions",'\n3. Quitter le menu principale')
        try:
            op = int(input('\nChoisissez une option (1-3): '))
        except ValueError:
            print('Erreur: Entrez une valeur entière (1-3)')
            continue
        if op == 1:
            print("\n\tAjouter une nouvelle mot/phrase\n")
            introduire_le_expression()
        elif op == 2:
            print("\n\t\tListes d'expressions")
            read_le_fichier()
        elif op == 3:
            print("\nRetour au menu principal...\n")
        else:
            print('Entrez un numéro valide (1-3)')