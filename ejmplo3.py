from ejemplo1.ejmplo1 import *
from ejmplo2 import *
import time

# Menu des fonctions principales

def main_fonction_3():
    op = 1
    while op != 3:
        print("\t\tMenu Principal")
        print('1. Dictionnaire','\n2. Agenda','\n3. Sortir')
        try:
            op = int(input('\nChoisissez une option: '))
        except ValueError:
            print('Erreur: Entrez une valeur entière (1-3)')
            continue
        if op == 1:
            main_fonction_1()
        elif op == 2:
            main_fonction_2()
        elif op == 3:
            print('Quitter...')
            time.sleep(2)
        else:
            print('Entrez un numéro valide (1-3)')

main_fonction_3()
