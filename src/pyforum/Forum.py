class Forum:
    def __init__(self, id, nom, description = ""):
        self.__id = id
        self.__nom = nom
        self.__description = description
        self.__publication = []
        