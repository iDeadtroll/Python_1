
# Mirar una guia para comprender como funciona una agenda básica.
    # Consulter un guie pour comprendre le fonctionnement d'un agenda de base.

# Hacer funciones básicas para el funcionamiento de una agenda.
    # Effectuer de fonctions de base pour le fonctionnement d'un agenda.

# Implementar funciones haciendo uso de conjuntos.
    # Implémenter des fonctions en utilisant des ensembles

# Seguir un planteamiento similar al modulo 'ejmplo1.py'
    # Suivre une approche similaire au module précédent.
import time

jours = ('Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche')
numJour = (1,2,3,4,5,6,7)
jourSemaine={'Lundi':1,'Mardi':2,'Mercredi':3,'Jeudi':4,'Vendredi':5,'Samedi':6,'Dimanche':7}

# Exemple: fonctions pour imprimer des ensembles
def exemple():
    def montrer_jours1():
        for index, jour in enumerate(jours):
            print(f"{index}: {jour}")


    def montrer_jours2():
        liste1=tuple(zip(numJour,jours))
        for i, t in liste1:
            print(f"{i}: {t}")

    def montrer_jours3():
        for jour,num in jourSemaine.items():
            print(f"{jour} jour {num} du semaine")

    montrer_jours1()
    print("")
    montrer_jours2()
    print("")
    montrer_jours3()
    print("")

# Agenda

agenda={}

def ajouter_des_contacts():
    a=True
    while a:
    
        nombre=input("Nom du contact: ")
        if nombre in agenda:
            print(f"Le nom {nombre} est déjà enregistré, et son numéro est {agenda[nombre]}")
        else:
            agenda[nombre]=input("Entrez un numero: ")

        print("Voulez-vous ajouter un autre contact? (oui/non)")
        other=input("Appuyez sur 'o' (oui), appuyez sur une autre touche (non)\n")
        o="o"

        if other:
            if other.lower == o.lower:
                a=True
            else:
                a=False
        else:
            a = False



def afficher_les_contacts():
    for nombre, numero in agenda.items():
        print(f"{nombre}: {numero}")
    print("")
# Menu

def main_fonction_2():

    op=0
    while op != 3:
        print("\t\tMenu Agenda")
        print("1. Ajouter des contacts","\n2. Lister les contacts","\n3. Retourner au menu principal\n")
        try:
            op=int(input("Choisissez une option: "))
        except ValueError:
            print("Erreur: Entrez une valeur entière (1-3)")
            continue
        if op == 1:
            print("\t\tAjouter des contacts")
            ajouter_des_contacts()
        elif op == 2 :
            print("\t\tLister les contacts")
            afficher_les_contacts()
        elif op == 3:
            print("Retour au menu principal...")
            time.sleep(2)
        else:
            print("Entrez un numéro valide (1-3)")
