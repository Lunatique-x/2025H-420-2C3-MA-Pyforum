class Utilisateur:
    def __init__(self, id, nom, email, mdp):
        self.__id = id
        self.__nom = nom
        self.__email = email
        self.__mdp = mdp
        self.__forum_inscrit = []

    def create_forum(self):
        
        