#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:18:38 2019

@author: nicolas
"""
import glob
S2_3A_dir  = "/mnt/DATAssd/S2/2018_3A/SENTINEL2X_20180815-000000-000_L3A_T31TCJ_D_V1-1/"
out_dir = "/mnt/DATAssd/S2/demo_bouconne/"
crop_extent = "351441.03008532827 4837981.308893643 362579.9884300245 4828550.683884008" # bouconne Forest
bands = glob.glob(S2_3A_dir+'*.tif')
for band in bands:
    out_raster = band[:-4]+'_crop.tif'
    out_raster = out_dir+glob.os.path.basename(out_raster)
    cmd = "gdal_translate -projwin {} -of GTiff -co COMPRESS=PACKBITS -co ZLEVEL=9 {} {}".format(crop_extent,band,out_raster)
    glob.os.system(cmd)
    
crop_files = glob.glob(out_dir+'*.tif')
band_order = ['B2','B3','B4','B8_','B5','B6','B7','B8A_','B11','B12']
crop_files_ordered = [s for i in band_order for s in crop_files if i in s]
cmd = 'gdalbuildvrt {}sentinel2_3a_20180815.vrt {} -resolution highest -separate'.format(out_dir,' '.join(crop_files_ordered))
glob.os.system(cmd)


import museotoolbox as mtb
rM = mtb.processing.RasterMath('/mnt/DATAssd/S2/demo_bouconne/sentinel2_3a_20180815.vrt')
def returnX(x):
    return x
rM.add_function(returnX,'/mnt/DATAssd/S2/demo_bouconne/sentinel2_3a_20180815.tif',compress='high')
rM.run()
