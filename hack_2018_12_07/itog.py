import arcgis
from arcgis.gis import GIS
import pyplot as plt

my_gis = GIS()

hello_map = my_gis.map("Санкт-Петербург", zoomlevel=15)
plt.pyplot.show(hello_map)