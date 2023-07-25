from ejemplo1.ejmplo1 import *
from ejmplo2 import *

# Menu des fonctions principales

def main_fonction_3():
    op = 1
    while op != 3:
        print("\t\tMenu Principal")
        print('1. Diccionario','\n2. Agenda','\n3. Salir')
        try:
            op = int(input('\nElije una opción: '))
        except ValueError:
            print('Ingresa un número válido')
            continue
        if op == 1:
            main_fonction_1()
        elif op == 2:
            main_fonction_2()
        elif op == 3:
            print('Saliendo...')
        else:
            print('Ingresa una opción válida')

main_fonction_3()