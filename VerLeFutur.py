
class Personne:
    def __init__(self, nom, annee, temps):
        self.nom = nom
        self.annee = annee
        self.temps = temps
def saisie():
    t = []
    while True:
        nom = input("Entrez le nom de la personne : ")
    
        personne = Personne(nom)
        t.append(personne)
    return t

def calculAnnee(t, annee_min, annee_max):
    for personne in t:
        periode = input(f"{personne.nom}, Quelle periode {annee_min} et {annee_max}) : ")
        annee_debut = random.randint(annee_min, annee_max)
        personne.annee = annee_debut
        print(f"{personne.nom}   {periode} ans.")

