# Installer PyForum


## Cloner le dépôt

Suivez les [instructions git](../tutos_git/README.md) pour configurer votre espace de travail.

## Créer un environnement virtuel

Pour créer un environnement virtuel sur Windows, vous pouvez utiliser la commande suivante :

```bash
py -m venv .venv
```
ou le créer depuis VSCode directement.

Vous pouvez ensuite activer l'environnement virtuel en utilisant la commande
suivante sur Windows :

```bash
.venv\Scripts\Activate
```


## Installer les dépendances de développement

Pour installer les dépendances de développement, une fois votre environnement
virtuel activé, vous pouvez utiliser la commande suivante :

```bash
python -m pip install -r requirements-dev.txt
```

Cette commande appelle l'interpréteur Python de l'environnement virtuel pour
lancer le module `pip` qui installera les dépendances listées dans le fichier
`requirements-dev.txt`.

## Installer PyForum

Ce projet est en fait un paquet (package) Python à part entière. Pour l'installer
dans votre environnement virtuel, vous pouvez utiliser la commande suivante :

```bash
python -m pip install -e .
```

L'option `-e` permet d'installer le paquet en mode *editable*, ce qui signifie
que vous pourrez modifier le code source du paquet et ces modifications seront
prises en compte automatiquement. Le point `.` signifie que le paquet à installer
se trouve dans le répertoire courant, c'est-à-dire le répertoire du projet.

Une fois le paquet installé, vous pourrez utiliser le fait que PyForum possède
un fichier `__main__.py` pour lancer l'application en utilisant la commande
suivante :

```bash
python -m pyforum
```

>[!CAUTION]
> Attention, il existe vraiment un paquet nommé pyforum sur PyPI. Ainsi, si vous
> faites `python -m pip install pyforum`, vous installerez un autre paquet qui n'a rien à
> voir avec notre projet. C'est pourquoi nous utilisons `python -m pip install -e .` pour
> installer notre paquet en mode *editable*.