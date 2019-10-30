---
marp: true
title : Démonstration de museotoolbox
paginate : true
author : nicolas karasiak
theme: gaia
---
<!-- Global style -->
<style> img[alt~="center"] { display: block; margin: 0 auto; } </style>


## Démonstration de MuseoToolBox

![right 100%](https://github.com/nkarasiak/MuseoToolBox/raw/master/metadata/museoToolBox_logo_128.png)

Comment faciliter les principaux traitements de la télédétection ?

###### Par [Nicolas Karasiak](https://www.karasiak.net/)

----

## Atelier télédétection python

:dart: L'objectif de cet atelier est :

- d'extraire les valeurs spectrales d'une image à partir d'un vecteur (point/polygone)
- de générer un indice spectral (type NDVI)  :chart_with_upwards_trend:
- créer un modèle à partir d'un algorithme de votre choix
- évaluer la qualité d'un modèle 👩‍💻
- prédire un modèle (raster, ou en générant à la volée un indice de type NDVI)

---

## Qu'est-ce que MuseoToolBox ?
MuseoToolBox est une bibliothèque dévelopée en python3 par [Nicolas Karasiak](https://www.karasiak.net).

![center](figures/mtb_uml.png)

---


## Installer MuseoToolBox
### Linux

```bash
python3 -m pip install museotoolbox --user
```
Pour mettre à jour:
```bash
python3 -m pip install museotoolbox --user -U
```

### Windows
Voir le tutorial ici : https://github.com/nkarasiak/atelier_SAGEO2019

---
## Principe de rasterMath
rasterMath est la clé de voute de MuseoToolBox. Cette classe est utilisée pour lire et écrire sur les images de manière optimisée.

La plupart des utilisations d'un raster dans notre domaine se fait pixel par pixel, c'est-à-dire que l'on n'a pas besoin de l'information des pixels voisins, mais que l'on traite la plupart du temps un pixel avec l'ensemble de ses bandes. C'est par exemple le cas quand on calcule l'indice NDVI.

---

**rasterMath** permet donc de lire une image et de ne recevoir que l'information par lot de pixels :

![center](figures/raster_math_3dto2d.png)

 
 ---

 Ainsi, vous n'avez plus besoin de gérer :
 - la projection géographique 🗺️
 - l'ouverture et la fermeture de l'image 
 - la gestion des no-data ou encore la compression 🗜️
 - la lecture et l'écriture en parcourant l'image bloc par bloc 
 - le type de données GDAL (conversion automatique depuis le type de données de numpy)

:bulb: Vous vous concentrez uniquement sur votre traitement.
 
 
 ---

 ### Calcul d'un NDVI
 
 Supposons que nous voulons calculer un NDVI avec les bandes 3 et 4 (donc comme en python commence à compter à partir de 0, il s'agira des bandes 2 et 3) :

```python
 def calcul_ndvi(x):
 	    ndvi = np.divide((x[:,3]-x[:,2]),(x[:,3]+x[:,2]))
     return ndvi
```
Il ne reste plus qu'à donner cette fonction à rasterMath. Le seul argument obligatoire dans votre fonction est le premier argument qui est le tableau numpy qui vous sera donné par rasterMath.

---

### Tester votre code
Après avoir écrit votre fonction `calcul_ndvi`, il faut donc la tester.
Pour cela, on va demander à rasterMath un bloc de l'image source.

```python
rM = rasterMath('monimage.tif')

# x est un bloc de mon image
x = rM.getRandomBlock()

# Je peux donc le donner à la fonction calcul_ndvi
calcul_ndvi(x)
```
---

### Calculer et écrire le NDVI

```python
rM = rasterMath('monimage.tif')

# Ajoute une fonction et un chemin pour écrire le résultat (fichier tif)
rM.addFunction(ajout_ndvi,'/tmp/ndvi.tif')

# Je lance le calcul et l'écriture
rM.run()
```
 Plus d'exemples sur : https://museotoolbox.readthedocs.io/en/latest/modules/raster_tools/museotoolbox.raster_tools.rasterMath.html
 
---

## Principes de learnAndPredict

Permet de faire de l'apprentissage automatique depuis un raster ou un vecteur. Vous choisissez : 
- l'algorithme et ses paramètres
- la validation croisée
- l'indice de qualité (accord global, kappa)

---

### learnAndPredict gèrera 
- la standardisation des données
- la sauvegarde du modèle
- le calcul des indices de qualité de chaque pli (issu des validations croisées)
- le calcul de la matrice de confusion de chaque pli
- l'entrainement et la prédiction à partir d'une image ou d'un vecteur

---

```python
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(random_state=12,n_jobs=1)

from museotoolbox.learn_tools import learnAndPredict

# initialisation de la classe avec 4 coeurs pour les validations croisées
mymodel = learnAndPredict(n_jobs=4,verbose=1)

# entrainement à partir d'un raster
mymodel.learnFromRaster(raster,vector,field,cv=5,
                    classifier=classifier,param_grid=dict(n_estimators=[100,200]))

# prédiction d'un raster
mymodel.predictRaster(raster,'classification.tif')
```

Plus d'exemples sur : https://museotoolbox.readthedocs.io/en/latest/modules/learn_tools/museotoolbox.learn_tools.learnAndPredict.html#museotoolbox.learn_tools.learnAndPredict

---

## Estimer la qualité du modèle

```python
CM = []
OA = []
for statsPerCv in mymodel.getStatsFromCV(kappa=True,OA=True):
    CM.append(statsPerCv['confusionMatrix'])
    OA.apppend(statsPerCv['OA'])

# Accord global moyen
print(np.mean(OA))
```
---

## Calculer la matrice de confusion moyenne et le F1

```python

from museotoolbox import charts
from matplotlib.pyplot import cm as colorMap
# average cm
meanCM = np.mean(CM,axis=0).astype(np.int16)
# Translate for Y = prediction and X = truth
pltCM = charts.plotConfusionMatrix(meanCM.T) 
# add value for each cell
pltCM.addText()
# add F1
pltCM.addF1()
```
---
# Résultat
![center](figures/cm_f1.png)

---

## Extraire les valeurs spectrales et les labels d'un vecteur

```python
from museotoolbox.raster_tools import getSamplesFromROI

# extraire uniquement les valeurs spectrales
X =  getSamplesFromROI(raster,vector)

# extraire les valeurs spectrales et le label du vecteur
X,y = getSamplesFromROI(raster,vector,'class')

# extraire les valeurs spectrales et deux champs
X,y,group = mtb.raster_tools.getSamplesFromROI(raster,vector,'class','uniquefid')
```

Exemple complet sur : https://museotoolbox.readthedocs.io/en/latest/auto_examples/raster_tools/extractRasterValues.html

---
## Créer un masque à partir d'un vecteur

```python
# par défault, seuls les polygons sont non masqués 
museotoolbox.raster_tools.rasterMaskFromVector(vector,raster,'/tmp/mask.tif')

# si vous voulez masquer uniquement les polygones 
museotoolbox.raster_tools.rasterMaskFromVector(vector,raster,'/tmp/mask.tif',invert=True)

```

