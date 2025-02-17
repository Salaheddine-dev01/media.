from abc import ABC, abstractmethod

class Media(ABC):
    compteur_media = 0

    def __init__(self, id: int, titre: str, annee: int):
        self._id = id
        self._titre = titre
        self._annee = annee
        Media.compteur_media += 1  # Increment the media counter here

    @abstractmethod
    def afficher_details(self):
        pass

    @staticmethod
    def nombre_de_medias():
        return Media.compteur_media


class Livre(Media):
    def __init__(self, id: int, titre: str, annee: int, auteur: str, isbn: str):
        super().__init__(id, titre, annee)
        self._auteur = auteur
        self._isbn = isbn

    def afficher_details(self):
        print(f"Livre - Titre: {self._titre}, Auteur: {self._auteur}, ISBN: {self._isbn}, Année: {self._annee}")


class Magazine(Media):
    def __init__(self, id: int, titre: str, annee: int, editeur: str, periodicite: str):
        super().__init__(id, titre, annee)
        self._editeur = editeur
        self._periodicite = periodicite

    def afficher_details(self):
        print(f"Magazine - Titre: {self._titre}, Éditeur: {self._editeur}, Périodicité: {self._periodicite}, Année: {self._annee}")


class DVD(Media):
    def __init__(self, id: int, titre: str, annee: int, realisateur: str, duree: int):
        super().__init__(id, titre, annee)
        self._realisateur = realisateur
        self._duree = duree

    def afficher_details(self):
        print(f"DVD - Titre: {self._titre}, Réalisateur: {self._realisateur}, Durée: {self._duree} min, Année: {self._annee}")


class Telechargeable:
    def __init__(self, taille_fichier: float, format_fichier: str):
        self.taille_fichier = taille_fichier
        self.format_fichier = format_fichier

    def afficher_details(self):
        print(f"Taille du fichier: {self.taille_fichier} Mo")
        print(f"Format du fichier: {self.format_fichier}")


class LivreNumerique(Livre, Telechargeable):
    def __init__(self, id: int, titre: str, annee: int, auteur: str, isbn: str, taille_fichier: float, format_fichier: str):
        Livre.__init__(self, id, titre, annee, auteur, isbn)
        Telechargeable.__init__(self, taille_fichier, format_fichier)

    def afficher_details(self):
        Livre.afficher_details(self)
        Telechargeable.afficher_details(self)


# Corrected instantiations
livre = Livre(1, "Python 101", 2023, "Alice", "12345")
magazine = Magazine(2, "Tech Today", 2023, "TechPublisher", "Monthly")
dvd = DVD(3, "Python Basics", 2021, "John", 120)
livre_numerique = LivreNumerique(4, "Digital Python", 2023, "Alice", "54321", 10.5, "pdf")

media_list = [livre, magazine, dvd, livre_numerique]  # Add the instance of LivreNumerique here

# Display details of each media item
for media in media_list:
    media.afficher_details()

# Display the total number of media items
print(f"Nombre total de médias: {Media.nombre_de_medias()}")