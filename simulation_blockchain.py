import hashlib
import datetime

class Bloc:
    def __init__(self, index, donnees, empreinte_precedente):
        self.index = index
        self.horodatage = str(datetime.datetime.now())
        self.donnees = donnees
        self.empreinte_precedente = empreinte_precedente
        self.empreinte = self.calculer_empreinte()

    def calculer_empreinte(self):
        contenu = f"{self.index}{self.horodatage}{self.donnees}{self.empreinte_precedente}"
        return hashlib.sha256(contenu.encode("utf-8")).hexdigest()

class Blockchain:
    def __init__(self):
        self.chaine = [self.creer_bloc_genese()]

    def creer_bloc_genese(self):
        return Bloc(0, "Bloc Genèse", "0")

    def ajouter_bloc(self, donnees):
        dernier_bloc = self.chaine[-1]
        nouveau_bloc = Bloc(len(self.chaine), donnees, dernier_bloc.empreinte)
        self.chaine.append(nouveau_bloc)

    def verifier_integrite(self):
        for i in range(1, len(self.chaine)):
            bloc_actuel = self.chaine[i]
            bloc_precedent = self.chaine[i - 1]
            if bloc_actuel.empreinte != bloc_actuel.calculer_empreinte():
                return False, f"Altération détectée au bloc #{bloc_actuel.index}"
            if bloc_actuel.empreinte_precedente != bloc_precedent.empreinte:
                return False, f"Rupture de chaînage entre bloc #{bloc_precedent.index} et #{bloc_actuel.index}"
        return True, "Chaîne valide et intègre."

if __name__ == "__main__":
    bc = Blockchain()
    bc.ajouter_bloc("Transaction 1 : Saad envoie 10 unités à Meriem")
    bc.ajouter_bloc("Transaction 2 : Meriem envoie 4 unités à Ali")

    for bloc in bc.chaine:
        print(f"Bloc #{bloc.index} | Prev: {bloc.empreinte_precedente[:12]}... | Hash: {bloc.empreinte[:12]}...")

    print("Vérification initiale :", bc.verifier_integrite())

    # Simulation d'une fraude sur le bloc 1
    bc.chaine[1].donnees = "Transaction 1 : Saad envoie 1000 unités à Meriem"
    print("Après modification du bloc 1 :", bc.verifier_integrite())
