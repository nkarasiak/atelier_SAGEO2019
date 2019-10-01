# Atelier SAGEO2019 : Télédétection avec MuseoToolBox
*Cet atelier ne nécessite pas de compétences avancées en python*

[MuseoToolBox](https://github.com/lennepkade/MuseoToolBox]) est une bibliothèque python développée par [Nicolas Karasiak](http://wwww.karasiak.net) dans le cadre de sa thèse sur la classification des essences forestières. Dans un soucis de reproductibilité de ses travaux (que ce soit tant pour lui, pour la fiabilité de ses travaux ou pour promouvoir les bonnes pratiques), cette bibliothèque permet d'automatiser et de faciliter de nombreuses opérations courantes dans notre domaine. En effet, plus besoin de gérer les nombreux à-côtés parfois longs et fastidieux de la gestion des rasters ou des vecteurs en python (lecture/écriture des images avec compression automatique, opération mathématique sur un raster, extraction des valeurs des pixels pour chaque polygone, apprentissage automatique à partir de raster...).

## Objectif de l'atelier

L'objectif principal de l'atelier et de réaliser, à partir d'une image géoréférencée ou d'une série temporelle, des opérations courantes mais en quelques lignes de codes seulement :

- calcul d'un indice spectral (de type NDVI)
- lissage d'un signal temporel
- apprentissage automatique optimisé (avec standardisation des données et paramètres optimisés de l'algorithme)
- prédire un modèle sur sa zone d'étude
- estimer la qualité du modèle et générer des matrices de confusions évoluées (avec précision producteur et réalisateur, ou score F1)

L'idée de cet atelier est de vous montrer les bases de MuseoToolBox qui vous permettront de vous sentir libre et de vous faciliter par la suite de nombreux traitements courants dans notre domaine.

## Prérequis
Il n'y a pas de prérequis en programmation nécessaire, mais des connaissances en python vous aideront certainement à comprendre plus vite cet outil.

### Sous Windows

Le plus simple est de passer sous Ubuntu :) Plus sérieusement, je vous conseillerais d'installer un environnement Conda, notamment pour avoir accès à GDAL depuis python.

Petit guide pour installer un environnement python avec conda : [https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/](https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/)

Puis déployer l'environnement CONDA suivant :
**TODO** fournir fichier environnement conda avec dépendences à installer.

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
