# Projet PyForum – Développement du MVP

## Introduction au MVP

Un **MVP (Minimal Viable Product)** est une version simplifiée d'un produit,
qui contient uniquement les fonctionnalités essentielles pour valider les
hypothèses de base et permettre une première utilisation. Le but du MVP est de
démontrer que l'application fonctionne avec un ensemble limité de
fonctionnalités, tout en laissant place à des évolutions futures.

## Objectifs

Dans cette première étape du projet PyForum, vous allez développer un **MVP**
qui comprend les fonctionnalités de base suivantes :

- Un seul type d'utilisateur, qui pourra :
  - Créer un forum
  - Créer une publication dans un forum
  - Ajouter un commentaire à une publication
  - Joindre un forum

## Fonctionnalités à développer

Cette section présente les fonctionnalités de base à développer pour le MVP de
PyForum. La section [À vous de jouer !](#à-vous-de-jouer) contient les
instructions détaillées de ce que vous devez réaliser.

### 1. Création d'un utilisateur

Un utilisateur pourra s'inscrire en créant un compte. Chaque utilisateur doit
contenir :
- Un identifiant unique
- Un nom d'utilisateur
- Une adresse email
- Un mot de passe (dans cette première phase, vous pouvez ignorer la gestion
  sécurisée des mots de passe)
- Une liste vide de forums auxquels il est inscrit

### 2. Création d'un forum

L'utilisateur pourra créer un forum. Chaque forum doit contenir :
- Un identifiant unique
- Un nom
- Une description (optionnelle)
- Une liste vide de publications (initialisée à une liste vide)

### 3. Création d'une publication

L'utilisateur pourra créer une publication dans un forum. Chaque publication
doit contenir :
- Un identifiant unique
- Un titre
- Un contenu
- L'identifiant de l'auteur 
- L'identifiant du forum auquel elle appartient
- Une liste de commentaires (qui est initialisée à une liste vide)

### 4. Ajout d'un commentaire

L'utilisateur pourra ajouter un commentaire à une publication. Chaque
commentaire doit contenir :
- Un identifiant unique
- L'identifiant de l'auteur
- Le contenu du commentaire
- L'identifiant de la publication à laquel il appartient

### 5. Joindre un forum

L'utilisateur pourra rejoindre un forum existant. Chaque utilisateur pourra
s'ajouter à un ou plusieurs forums. Lorsqu'un utilisateur rejoint un forum, ce
forum est rajouté a sa liste de forums.

## Classe BD

La classe **BD** (Base de Données) représente la base de données de
l'application. À terme, les données seront stockées dans des fichiers
JSON et CSV. Mais pour l'instant, dans le **MVP**, la base de données
retient les informations en mémoire.

Une partie de la classe **BD** est déjà implémentée dans le fichier
`src/pyforum/bd.py`. Dans cette première étape, vous devez compléter
les fonctions existantes.

Notez que c'est le rôle de la classe **BD** de gérer les identifiants
uniques. Ainsi, pour créer par exemple un utilisateur, vous fournirez à la
classe **BD** les champs nécessaires et c'est elle qui se chargera de
générer l'identifiant unique. Autrement dit, c'est la base de donnée qui 
vous retourne un objet `Utilisateur` et non l'inverse.

## Fichier main.py - Description et utilisation

Le fichier `__main__.py` représente l'interface principale de l'application
PyForum, permettant de simuler le fonctionnement de base de l'application à
travers un menu interactif dans le terminal.

Ce fichier contient une boucle principale qui affiche un menu et permet à
l'utilisateur de choisir une action parmi plusieurs options disponibles. Vous
devrez rajouter du code à ce fichier afin d'utiliser les classes et méthodes
que vous avez créés.

## À vous de jouer !

## Étape 1 : Diagramme UML

Vous devez commencer par créer des diagramme UML pour modéliser le MVP. Le
fichier [Mermaid.md](./Mermaid.md) contient une introduction à la syntaxe
Mermaid pour créer des diagrammes UML.

Créez les diagrammes dans le fichier `src/pyforum/UML/mvp.md`.

#### Diagramme de cas d'utilisation

Créer un diagramme de cas d'utilisation pour l'utilisateur en fonction
de la description donnée à la section [Objectifs](#objectifs).

#### Diagramme de classes

En fonction de la description à la section [Fonctionnalités à développer](#fonctionnalités-à-développer),
créez un diagramme de classes pour modéliser les classes et les relations entre
elles. Les classes à modéliser sont :

- Utilisateur
- Forum
- Publication
- Commentaire

N'oubliez pas de modéliser les attributs et les méthodes de chaque classe,
ainsi que les relations d'agrégation et de composition.

## Étape 2 : Implémentation des classes

Créez les classes `Utilisateur`, `Forum`, `Publication`, et `Commentaire` dans
le dossier `src/pyforum` en fonction du diagramme de classes que vous avez
créé. Faite un fichier par classe.

Astuces:
- N'oubliez pas d'implémenter la méthode `__str__` pour chacune des classes pour permettre leur affichage à l'écran.

## Étape 3 : Compléter le fichier MVP et la classe BD

Complétez le fichier `src/pyforum/mvp.py` et `src/pyforum/bd.py` pour permettre
à l'utilisateur d'interagir avec l'application. La partie à compléter est
indiquée par des commentaires `TODO` dans la fonction `main()` et dans la
la clasee `BD`.

Le cas de l'utilisateur est presque complet. Vous pouvez vous en inspirer.


> [!NOTE]
> Vous n'avez pas besoin d'écrire de tests unitaires pour le MVP.
