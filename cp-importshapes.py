'''
Created on Aug 24, 2015

@author: cmp
'''

import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as pl
import numpy as np
import geopandas as gpd

parks = gpd.GeoDataFrame.from_file('./DPR_ParksProperties_001.shp')
parksbounds=parks.geometry

pg = parks.groupby(['BOROUGH','TYPECATEGO'])

pl.hist(parks[''])

fig = pl.figure()
ax1 = pl.subplot2grid((1,1),(0,0))
ax1=parks.plot()

pl.show()

if __name__ == '__main__':
    pass