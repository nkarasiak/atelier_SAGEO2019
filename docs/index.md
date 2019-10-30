---
marp: true
title : Démonstration de museotoolbox
paginate : true
author : nicolas karasiak
---
<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>


# Démonstration de MuseoToolBox
![right 100%](https://github.com/nkarasiak/MuseoToolBox/raw/master/metadata/museoToolBox_logo_128.png)

Comment faciliter les principaux traitements de la télédétection ?

###### Par [Nicolas Karasiak](https://www.karasiak.net/)

----

# Atelier télédétection python

L'objectif de cet atelier est :

- d'extraire les valeurs spectrales d'une image à partir d'un vecteur (point/polygone)
- de générer un indice spectral (type NDVI)
- créer un modèle à partir d'un algorithme de votre choix
- évaluer la qualité d'un modèle
- prédire un modèle (raster, ou en générant à la volée un indice de type NDVI)

---

# Qu'est-ce que MuseoToolBox ?
MuseoToolBox est une bibliothèque dévelopée en python3 par [Nicolas Karasiak](https://www.karasiak.net).

![center](figures/mtb_uml.png)

---


## Principe de rasterMath
rasterMath est la clé de voute de MuseoToolBox. Cette classe est utilisée pour lire et écrire sur les images de manière optimisée.

La plupart des utilisations d'un raster dans notre domaine se fait pixel par pixel, c'est-à-dire que l'on n'a pas besoin de l'information des pixels voisins, mais que l'on traite la plupart du temps un pixel avec l'ensemble de ses bandes. C'est par exemple le cas quand on calcule l'indice NDVI.

---

**rasterMath** permet donc de lire une image et de ne recevoir que l'information par lot de pixels :

![center](figures/raster_math_3dto2d.png)

 
 ---

 Ainsi, vous n'avez plus besoin de gérer les projections géographiques, l'ouverture et la fermeture de l'image, la gestion des no-data ou encore la compression.
 La lecture et l'écriture sont optimisées en lisant l'image bloc par bloc. 
 Il est à noter que par défaut rasterMath force la lecture et l'écriture par bloc de 256x256 pixels.
 
 Si vous souhaitez changer la taille des blocs, vous pouvez utiliser la fonction `rasterMath().customBlockSize(x_block_size,y_block_size)`.
 
 ---

 ### Calcul d'un NDVI
 
 Supposons que nous voulons calculer un NDVI avec les bandes 3 et 4 (donc comme en python on commence le calcul à 0, il s'agira des bandes 2 et 3) :

```
 def calcul_ndvi(x):
 	    ndvi = np.divide((x[:,3]-x[:,2]),(x[:,3]+x[:,2]))
     return ndvi
```
Il ne reste plus qu'à donner cette fonction à rasterMath. Le seul argument obligatoire dans votre fonction est le premier argument qui est en fait le tableau au format numpy.

---

### Tester votre code
Après avoir écrit votre fonction calcul_ndvi, il faut donc la tester.
Pour cela, on va demander à rasterMath un bloc de l'image source.

``` 
rM = rasterMath('monimage.tif')

# x est un bloc de mon image
x = rM.getRandomBlock()

# Je peux donc le donner à la fonction calcul_ndvi
calcul_ndvi(x)
```
---

### Calculer et écrire le NDVI

``` 
rM = rasterMath('monimage.tif')

# Ajoute une fonction à calculer et un chemin pour écrire le résultat
rM.addFunction(ajout_ndvi,'/tmp/ndvi.tif')

# Je lance le calcul et l'écriture
rM.run()
```
 Plus d'exemples sur : https://museotoolbox.readthedocs.io/en/latest/modules/raster_tools/museotoolbox.raster_tools.rasterMath.html
 
---

# Principes de learnAndPredict
Classe qui permet de faire de l'apprentissage automatique depuis un raster ou un vecteur.

Vous avez le choix : 
- de l'algorithme et de ses paramètres
- de la validation croisée
- de l'indice de qualité, etc...

learnAndPredict gère : 
- la standardisation des données
- la sauvegarde du modèle et peut générer les indices de qualité de chaque pli (issu des validations croisées)
- prédit à partir d'une image ou d'un vecteur

---

```
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(random_state=12,n_jobs=1)

from museotoolbox.learn_tools import learnAndPredict


mymodel = LAP = learnAndPredict(n_jobs=4,verbose=1)
LAP.learnFromRaster(raster,vector,field,cv=5,
                    classifier=classifier,param_grid=dict(n_estimators=[100,200]))
```

Plus d'exemples sur : https://museotoolbox.readthedocs.io/en/latest/modules/learn_tools/museotoolbox.learn_tools.learnAndPredict.html#museotoolbox.learn_tools.learnAndPredict
