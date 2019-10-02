# Atelier SAGEO2019 : Télédétection avec MuseoToolBox
*Cet atelier ne nécessite pas de compétences avancées en python*

[MuseoToolBox](https://github.com/lennepkade/MuseoToolBox]) est une bibliothèque python développée par [Nicolas Karasiak](http://wwww.karasiak.net) dans le cadre de sa thèse sur la classification des essences forestières. Dans un soucis de reproductibilité de ses travaux (que ce soit tant pour lui, pour la fiabilité de ses travaux ou pour promouvoir les bonnes pratiques), cette bibliothèque permet d'automatiser et de faciliter de nombreuses opérations courantes dans notre domaine. En effet, plus besoin de gérer les nombreux à-côtés parfois longs et fastidieux de la gestion des rasters ou des vecteurs en python (lecture/écriture des images avec compression automatique, opération mathématique sur un raster, extraction des valeurs des pixels pour chaque polygone, apprentissage automatique à partir de raster ou de son indice généré à la volée...).

## Objectif de l'atelier

L'objectif principal de l'atelier et de réaliser, à partir d'une image géoréférencée ou d'une série temporelle, des opérations courantes mais en quelques lignes de codes seulement :

- calcul d'un indice spectral (de type NDVI)
- lissage d'un signal temporel
- sélection d'un algorithme et d'une validation croisée
- apprentissage automatique optimisé (avec standardisation des données et paramètres optimisés de l'algorithme)
- prédire un modèle sur sa zone d'étude
- estimer la qualité du modèle et générer des matrices de confusions évoluées (avec précision producteur et réalisateur, ou score F1)

L'idée de cet atelier est de vous familiariser avec MuseoToolBox en construisant ensemble une chaîne de traitements avec les nombreuses pratiques courantes dans notre domaine.

## Prérequis

Il n'y a pas de prérequis en programmation nécessaire, mais des connaissances en python vous aideront certainement à comprendre plus vite cet outil.

### Sous Windows

Le plus simple est de passer sous Ubuntu :) Plus sérieusement, je vous conseillerais d'installer un environnement anaconda, notamment pour avoir accès à GDAL depuis python.

- (Télécharger et installer Anaconda pour Python 3)[https://www.anaconda.com/distribution/]
- (Sauvegarder le fichier de configuration de l'environnement python) [https://raw.githubusercontent.com/lennepkade/atelier_SAGEO2019/master/py3mtbenv.yml]
- Ouvrir `Anaconda Navigator`
- Cliquer sur l'onglet `Environments`
- Cliquer sur l'icône `Import`
- Nommer l'environnement `MuseoToolBox` et choisissez le fichier précédemment enregistré (`py3mtbenv.yml`).
- Retourner sur l'onglet `Accueil`, choisissez bien MuseoToolBox et installer Spyder ainsi que Notebook.

### Sous Ubuntu

#### Installation de GDAL

Dans le terminal, ajouter les dépôts ubuntugis et installer les dépendances (gdal et spyder3 pour programmer python) :
```
sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update

sudo apt update

sudo apt install spyder3 gdal-bin=2.2.3* libgdal-dev=2.2.3* python3-gdal=2.2.3*
```

#### Installation de MuseoToolBox
Dans le terminal, taper la commande suivante pour installer museotoolbox :
```
python3 -m pip install museotoolbox --user
```

Ensuite, vérifier si museotoolbox est bien installé en tapant la commande suivante :
`python3 -c 'import museotoolbox'
