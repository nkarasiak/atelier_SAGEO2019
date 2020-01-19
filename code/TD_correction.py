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

rM = mtb.processing.RasterMath(raster)

x = rM.get_random_block()

def ndvi(x):
    num = x[:,3]-x[:,2]
    denum = x[:,3]+x[:,2]
    result = num/denum
    result.astype(np.float32)
    return result
    
print(ndvi(x))

rM.add_function(ndvi,'/tmp/ndvi.tif')

#rM.run()
##
def LChloC(x):
    # division entre B7 et B5
    return np.divide(x[:,6],x[:,4])

LChloC(x)

rM.add_function(LChloC,'/tmp/LChloC.tif')
rM.run()

####
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(random_state=12,n_jobs=1)



mtb.learn_tools.learnAndPredict()
cv = mtb.cross_validation.LeaveOneSubGroupOut()
X,y,group = mtb.processing.extract_ROI(raster,vector,'class','group')

mymodel = mtb.ai.SuperLearner(n_jobs=4,verbose=1,classifier=classifier,param_grid=dict(n_estimators=[100,200]))

# entrainement à partir d'un vecteur avec standardisation (centré/réduit)
mymodel.customize_array(LChloC)

mymodel.fit(X,y,group=group,cv=cv,standardize=True)
mymodel.predict_image(raster,'/tmp/LChloC_map.tif')
mymodel.save_CM_from_CV('/tmp/matrices/')
mymodel.get_stats_from_CV()

mymodel.model.best_estimator_
