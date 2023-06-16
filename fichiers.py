# 3eme parite: Fichiers

def nbMotsAvecVoyelle(nomf):
    voyelles = ['i', 'u', 'o', 'a', 'e']
    nb_mots = 0

    with open(nomf, 'r') as fichier:
        for mots in fichier:

            if mots[0] in voyelles:
                nb_mots += 1

    return nb_mots 

#3.2
def CompterChaqueMot(nomf1, nomf2):
    mots_occurrences = {}

    with open(nomf1, 'r') as fichier1:
        for ligne in fichier1:
            mot = ligne.strip()
            mots_occurrences[mot] = mots_occurrences.get(mot, 0) + 1

    with open(nomf2, 'w') as fichier2:
        for mot, occurrences in mots_occurrences.items():
            fichier2.write(f"{mot} {occurrences}\n")


        

