class Utilisateur:
    def __init__(self, nom, email, mdp):
        self.__id = 1
        self.__nom = nom
        self.__email = email
        self.__mdp = mdp
        self.__forum_inscrit = []

    def __str__(self):
        return f"Utilisateur(id={self.id}, username={self.__nom})"
