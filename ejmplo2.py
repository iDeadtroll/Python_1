jours = ('Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche')
numJour = (1,2,3,4,5,6,7)
# Fonctions pour imprimer des listes
def montrer_jours1():
    for i, t in enumerate(jours):
        print(f"{i}: {t}")

def montrer_jours2():

    liste1=tuple(zip(numJour,jours))
    for i, t in liste1:
        print(f"{i}: {t}")

# montrer_jours1()
# print("") 
# montrer_jours2()