# Mirar una guia de como funciona una agenda básica.
# Hacer funciones básicas para el funcionamiento de una agenda.
# Implementar funciones haciendo uso de conjuntos.
# Seguir un planteamiento similar al modulo 'ejmplo1.py'

jours = ('Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche')
numJour = (1,2,3,4,5,6,7)
jourSemaine={'Lundi':1,'Mardi':2,'Mercredi':3,'Jeudi':4,'Vendredi':5,'Samedi':6,'Dimanche':7}

# Exemple: fonctions pour imprimer des ensembles
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
