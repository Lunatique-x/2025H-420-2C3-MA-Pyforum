import Utilisateur
import Forum

class Publication:
    def __init__(self, id, titre, contenue, u):
        self.__id = id
        self.__titre = titre
        self.__contenu = contenue
        self.__auteur_id = Utilisateur.__id
        self.__forum_id = Forum.__id
        self.__commentaire = []