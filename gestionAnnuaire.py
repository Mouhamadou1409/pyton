#1ére parie:    Gestion annuaire
def Gestion_annuaire():
    annuaire = []
    while True:
        personne = {}
        personne["nom"] = input("Nom : ")
        personne["prenom"] = input("Prénom : ")
        personne["numero"] = input("Numéro  : ")
        personne["nom_rue"] = input("Nom de la rue : ")
        personne["telephone"] = input("Numéro de téléphone : ")
        personne["code_postal"] = input("Code postal : ")
        personne["ville"] = input("Ville : ")
        annuaire.append(personne)
    
    return annuaire


def critere_recherche():
    print("Critères de recherche disponibles : ")
    print("1. Nom")
    print("2. Prénom")
    print("3. Nom de la rue")
    print("4. Numéro de téléphone")
    print("5. Code postal")
    print("6. Ville")
    
    choix = int(input("Choisissez le critère de recherche (1-6) : "))
    return choix


def recherche(annuaire, critere):
    valeur_recherche = input("Entrez la valeur de recherche : ")
    resultat = []
    
    if critere == 1:  # Recherche par nom
        for personne in annuaire:
            if personne["nom"] == valeur_recherche:
                resultat.append(True)
            else:
                resultat.append(False)
    elif critere == 2:  # Recherche par prénom
        for personne in annuaire:
            if personne["prenom"] == valeur_recherche:
                resultat.append(True)
            else:
                resultat.append(False)
    elif critere == 3:  # Recherche par nom de rue
        for personne in annuaire:
            if personne["nom_rue"] == valeur_recherche:
                resultat.append(True)
            else:
                resultat.append(False)
    elif critere == 4:  # Recherche par numéro de téléphone
        for personne in annuaire:
            if personne["telephone"] == valeur_recherche:
                resultat.append(True)
            else:
                resultat.append(False)
    elif critere == 5:  # Recherche par code postal
        for personne in annuaire:
            if personne["code_postal"] == valeur_recherche:
                resultat.append(True)
            else:
                resultat.append(False)
    elif critere == 6:  # Recherche par ville
        for personne in annuaire:
            if personne["ville"] == valeur_recherche:
                resultat.append(True)
            else:
                resultat.append(False)
    
    return resultat


def affiche_tab(annuaire, resultat_recherche):
    print("Résultats de la recherche :")
    for personne, resultat in zip(annuaire, resultat_recherche):
        if resultat:
            print("Nom :", personne["nom"])
            print("Prénom :", personne["prenom"])
            print("Numéro dans la rue :", personne["numero"])
            print("Nom de la rue :", personne["nom_rue"])
            print("Numéro de téléphone :", personne["telephone"])
            print("Code postal :", personne["code_postal"])
            print("Ville :", personne["ville"])
            print()


annuaire = saisie_tab()
critere = critere_recherche()
resultat_recherche = recherche(annuaire, critere)
affiche_tab
