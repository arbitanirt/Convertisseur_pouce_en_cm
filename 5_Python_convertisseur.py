"""
Voici comment votre programme doit se comporter :
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
- fin du programme

1 pouce = 2.54 cm
1 cm = 0.394 pouces

"""
def demande():
    print("(a) : convertir de pouces vers cm")
    print("(b) : convertir de cm vers pouces")
    choix = input("CHOISE QUEL CONVERTION VOULEZ VOUS (a) ou (b) ? : ")
    return choix

def quitter():
    exit = input("Veuillez vous continuer (c) ou quitter (q) ? : ")
    if(exit == "c"):
        choix = demande()
        return choix
    elif (exit == "q"):
        return exit        
    else:
        print("Erreur Veillez entrer le valeur (c) pour continuer et la valeur (q) pour quitter")
        exit = input("Veuillez vous continuer (c) ou quitter (q) ? : ")


# fonction permet de convertir le pouce vers le cm
def converter_pouce_vers_cm():
    valeur = float(input("Entrer la valeur en pouce : "))
    print("Votre valeur est : ", valeur, " pouce")
    resultat_converte = valeur * 2.54
    return resultat_converte

# fonction permet de convertir le cm vers le pouce
def converter_cm_vers_pouce():
    valeur = float(input("Entrer la valeur en cm : "))
    print("Votre valeur est : ", valeur, " cm")
    resultat_converte = valeur * 0.394
    return resultat_converte

def Calculer(choix):
    # Application de choix choisi
    while(choix == "a" or choix == "b" or ex == "c"):  
        if(choix == "a"):
            print("la Valeur en cm est : ", converter_pouce_vers_cm(), " cm")
            ex = quitter()
            if(ex == "q"):
                print("Fin de Programme")
                break

        elif(choix == "b"):
            print("la Valeur en pouce est : ", converter_cm_vers_pouce(), " pouce")
            ex = quitter()
            if(ex == "q"):
                print("Fin de Programme")
                break
            


choix = demande()
while(choix != "a" or choix != "b"):
    choix = demande()
    print("veuillez choisir soit 'a' ou 'b' : ")
    if(choix == "a" or choix == "b"):
        choix = Calculer(choix)






