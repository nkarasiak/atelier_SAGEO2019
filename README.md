# Atelier SAGEO2019 : Télédétection avec MuseoToolBox
*Cet atelier ne nécessite pas de compétences avancées en python*

[MuseoToolBox](https://github.com/lennepkade/MuseoToolBox]) est une bibliothèque python développée par [Nicolas Karasiak](http://wwww.karasiak.net) lors de sa thèse sur la classification des essences forestières. Dans un soucis de reproductibilité de ses travaux (que ce soit tant pour lui, pour la fiabilité de ses travaux ou pour promouvoir les bonnes pratiques), cette bibliothèque permet de se soucier que ce qu'il vous importe le plus.

Plus besoin de gérer les nombreux à-côtés parfois longs et fastidieux de la gestion des rasters ou des vecteurs en python (lecture/écriture et traitement des images, opération mathématique sur un raster, extraction des valeurs des pixels pour chaque polygone...).

## Objectif de l'atelier

L'objectif principal de l'atelier et de réaliser, à partir d'images géoréférencées, de nombreuses opérations sous python :

- calcul d'un indice spectral (de type NDVI)
- lissage d'un signal temporel (filtre moyen)
- apprentissage automatique optimisé (avec standardisation des données et paramètres optimisés de l'algorithme)
- prédire un modèle sur une autre zone d'étude
- réduire la dimension de la donnée

L'idée est de vous montrer les bases de MuseoToolBox qui vous permettront de vous sentir libre plus tard et ainsi de l'utiliser afin de vous faciliter de nombreux traitements.

## Prérequis
Il n'y a pas de prérequis en programmation nécessaire, mais des connaissances en python vous aideront certainement à comprendre plus vite cet outil.

### Sous Windows

Le plus simple est de passer sous Ubuntu :) Plus sérieusement, je vous conseillerai d'installer un environnement CONDA, notamment pour avoir accès à GDAL depuis python.

Petit guide pour installer un environnement python avec conda : [https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/](https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/)

### Sous Ubuntu

#### Installation de GDAL

```
sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update

sudo apt update

sudo apt install spyder3 gdal-bin=2.2.3* libgdal-dev=2.2.3* python3-gdal=2.2.3*
```

#### Installation de MuseoToolBox
```
python3 -m pip install museotoolbox --user
```
