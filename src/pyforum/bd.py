from pyforum.Utilisateur import Utilisateur
from pyforum.Forum import Forum
from pyforum.Publication import Publication


class BD:
    def __init__(self):
        self.utilisateurs: list[Utilisateur] = []
        self.forums = []
        self.publications = []
        self.commentaires = []
        self.utilisateurs_forums = {}
        print("Base de données initialisée.")
    
    def creer_utilisateur(self, username: str, email, mdp) -> Utilisateur:
        #                     ^^^^^^^^^^^^^^
        #TODO:    Vous devez ajouter les autres paramètres requis

        # Vérifier si l'utilisateur existe déjà
        if username in [u.username for u in self.utilisateurs]:
            print(f"[Simulé] L'utilisateur {username} existe déjà.")
            return

        # Créer un nouvel identifiant pour l'utilisateur
        new_id = max([u.id for u in self.utilisateurs], default=0) + 1

        # Instancier un nouvel utilisateur et l'ajouter à la liste
        u = Utilisateur(new_id, username, email, mdp) 
        self.utilisateurs.append(u)
        print(f"[Simulé] Sauvegarde de l'utilisateur: {u}")

        # Retourner l'utilisateur créé
        return u
    
    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.username == nom_utilisateur:
                return u

    def creer_forum(self, nom, description = "") -> Forum:

        if nom in [f.name for f in self.forums]:
            print(f"Le forum {nom} existe déja")

        # Création d'un nouvel id
        new_id = len([l.id for l in self.forums] + 1)

        # TODO: Implanter la logique pour créer un forum
        u = Forum(nom, description = "")
        self.forums.append(u)
        print(f"Votre Forum {nom} à été crée")
        pass

    def creer_publication(self, titre, contenue):
        #Création d'un nouvel id
        new_id = max([u.id for u in self.publications], default= 0) + 1

        # Ne pas avoir deux Publications avec le même nom sur le même Forum
        if titre in [f.titre for f in Forum.__publication]:
            good_title = titre 

        # TODO: Implanter la logique pour créer une publication
        u = Publication(titre, contenue)
        self.publications.append(u)
        print(f"Votre Publication est en ligne")
        pass

    def creer_commentaire(self, commentaire):
        #                       ^^^^^^^^^^^
        #                       Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer un commentaire
        pass

    def obtenir_forum_par_nom(self, nom_forum):
        # TODO: Implanter la logique pour chercher un forum à partir de son nom
        pass
    
    def obtenir_publication_par_titre(self, titre_publication):
        # TODO: Implanter la logique pour chercher une publication à partir de son titre
        pass

    def mettre_a_jour_forum(self, forum):
        #                         ^^^^^^
        #                         Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour mettre à jour le forum et retourner le forum mis à jour
        pass



    