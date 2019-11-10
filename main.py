import warnings
warnings.simplefilter('ignore')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import pygridgen as pgg
import pygridtools as pgt

# Domain points with betas
POINT_MODEL_SHAPEFILE = 'shpf/points.shp'

# Grid ROWS + 1
NYDIV = 111
# Grid COLS + 1
NXDIV = 91

def plot_model(domain, grid):
    """Util function that plot the domain and the grid

    Parameters:
        domain {geopandas} -- The domain
        grid {pygridgen} -- The grid
    """
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={'aspect':'equal'})
    # Update to las version 
    #fig = pgt.viz.plotCells(grid.x, grid.y, ax=ax)
    #fig = pgt.viz.plotDomain(domain.geometry.x, domain.geometry.y, beta=domain.efdc, ax=ax)
    fig = pgt.viz.plot_cells(grid.x, grid.y, ax=ax)
    pgt.viz.plot_domain(domain, betacol='efdc', ax=ax) 

domain = gpd.read_file(POINT_MODEL_SHAPEFILE)
grid = pgg.Gridgen(domain.geometry.x, domain.geometry.y, domain.efdc, shape=(NYDIV, NXDIV), thin=True)
plot_model(domain, grid)
