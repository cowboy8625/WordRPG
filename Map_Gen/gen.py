import random
import pandas as pd
import numpy as np

width = 3
hight = 3
area_names = ('Cave', 'Forest', 'Dark Forest', 'Woodlands', 'Mountains', 'Lake', 'River', 
'Town', 'Village' 'Feild', 'Farm', 'Grasslands', 'Wetlands' 'Salt Marsh', 'Alpine Grasslands')


class coord_ys:

    def __init__(self, coords_x, coords_y, name, rarity, difficulty, enterable, 
    floor, next_to, avoid, exit_x, exit_y, discovord):

        self.coords_x = coords_x
        self.coords_y = coords_y
        self.name = name
        self.rarity = rarity ##-- How often you need to be spawned --##
        self.difficulty = difficulty
        self.enterable = enterable ##-- True or False --##
        self.floor = floor  ##-- in SQL it is coord_y_level --##
        self.next_to = next_to
        self.avoid = avoid
        self.exit_x = exit_x
        self.exit_y = exit_y
        self.discovord = discovord 


##-- This creates a gride or "Map" --##

# df = pd.DataFrame(columns=range(grid[1]),index=range(grid[0]))
# print(df)

##-- This sets the coords to a biome --##
x = 1
y = 0

#  print(df)

def map_builder():

    width = 5
    hight = 3
    grid = [hight, width]
    df = pd.DataFrame(columns=range(grid[1]),index=range(grid[0]))

    for coord_y in range(0, width * hight):
        if coord_y % width == 0 and coord_y != 0:
            #y += 1
            pass
    df.set_value(y,x,'cav')
    print(df)
        #df.set_value()
map_builder()  
