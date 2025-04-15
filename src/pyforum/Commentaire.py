import Utilisateur
import Publication

class Commentaire:
    def __init__(self, id, contenue, utilisateur_id, publication_id):
        self.__id = id
        self.__auteur_id = utilisateur_id
        self.__contenue = contenue
        self.__publication_id = publication_id