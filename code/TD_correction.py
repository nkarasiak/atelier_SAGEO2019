#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:47:39 2019

@author: nicolas
"""
import numpy as np
import museotoolbox as mtb

raster = '/home/nicolas/Bureau/atelier_SAGEO2019-data/sentinel2_3a_20180815.tif'
vector = '/home/nicolas/Bureau/atelier_SAGEO2019-data/ROI.gpkg'

rM = mtb.raster_tools.rasterMath(raster)

x = rM.getRandomBlock()

def ndvi(x):
    num = x[:,3]-x[:,2]
    denum = x[:,3]+x[:,2]
    result = num/denum
    result.astype(np.float32)
    return result
    
print(ndvi(x))

rM.addFunction(ndvi,'/tmp/ndvi.tif')

#rM.run()
##
def LChloC(x):
    # division entre B7 et B5
    return np.divide(x[:,6],x[:,4])

LChloC(x)

rM.addFunction(LChloC,'/tmp/LChloC.tif')
rM.run()

####
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(random_state=12,n_jobs=1)



mtb.learn_tools.learnAndPredict()
cv = mtb.cross_validation.LeaveOneSubGroupOut()
X,y,group = mtb.raster_tools.getSamplesFromROI(raster,vector,'class','group')

mymodel = mtb.learn_tools.learnAndPredict(n_jobs=4,verbose=1)

# entrainement à partir d'un vecteur avec standardisation (centré/réduit)
mymodel.customizeX(LChloC)

mymodel.learnFromVector(X,y,group=group,cv=cv,
    classifier=classifier,
    param_grid=dict(n_estimators=[100,200]),
    standardize=True)
mymodel.predictRaster(raster,'/tmp/LChloC_map.tif')
mymodel.saveCMFromCV('/tmp/matrices/')
mymodel.getStatsFromCV()

mymodel.model.best_estimator_
