# Scrapping_Project
Pour réaliser ses manipulations, il est nécessaire d'installer python et gitbash sur votre ordinateur

Avant, il faut télécharger le projet:

1. ouvrir gitbash
2. dans le dossier de votre choix, exécuter git clone "lienduprojet"

Pour créer et activer l'environnement virtuel:

1. exécuter la commande virtualenv -p python3 venv.
   venv est le nom de dossier. Dans le cas où l'on ne precise pas de chemin, le dossier sera créer dans le dans votre emplacement actuel. Vous pouvez aussi mettre un chemin ("C:/exemple/nomdudossier") à la palce de venv.
2. Dans la racine du dossier de votre environnement virtuel, éxecuter la commande source Scripts/activate
3. Retourner dans la racine du dossier du projet puis lancez la commande "python -m pip install -r requirements.txt"

Pour lancer l'application:

1. Dans la racine du dossier de votre projet, exécuter python main.py
