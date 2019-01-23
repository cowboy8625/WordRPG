##-- This is for the genoration of the Map File --##

##-- Imports --##

import random
import sqlite3
import pandas


##-- This is a simple drawing of the map             --##
##-- I would like to make a map generator             --##
##-- But we can work on that once the game functions --##
'''
 1 2 3 x
1 | | 
 -|-|-
2 | | 
 -|-|-
3 | | 
y
'''


map = {
    (1,1): {'name': 'Forest', 'difficulty': 1},
    (1,2): {'name': 'Dark Forest', 'difficulty': 3},
    (1,3): {'name': 'Vallie Town', 'difficulty': 0},
    (2,1): {'name': 'Cave', 'difficulty': 4},
    (2,2): {'name': 'Field', 'difficulty': 2},
    (2,3): {'name': 'Farm', 'difficulty': 2},
    (3,1): {'name': 'River', 'difficulty': 3},
    (3,2): {'name': 'Moutains', 'difficulty': 1},
    (3,3): {'name': 'Lake', 'difficulty': 2}
}
##-------------------------------------------------------------------------##
##-- EVERTHING BELOW THIS IS ALL FOR TESTING ------------------------------##
width = 3
hight = 3
area_names = ('Cave', 'Forest', 'Dark Forest', 'Woodlands', 'Mountains', 'Lake', 'River', 
'Town', 'Village' 'Feild', 'Farm', 'Grasslands', 'Wetlands' 'Salt Marsh', 'Alpine Grasslands')


class Tiles:

    def __init__(self, coords_x, coords_y, name, rarity, difficulty, enterable, floor, exit_x, exit_y, discovord):

        self.coords_x = coords_x
        self.coords_y = coords_y
        self.name = name
        self.rarity = rarity ##-- How often you need to be spawned --##
        self.difficulty = difficulty
        self.enterable = enterable ##-- True or False --##
        self.floor = floor  ##-- in SQL it is tile_level --##
        self.exit_x = exit_x
        self.exit_y = exit_y
        self.discovord = discovord 

mapfile = 'Worldmap.db'
conn = sqlite3.connect(mapfile)
c = conn.cursor()


def neat_layout(name):

    df = pandas.read_sql_query("SELECT * FROM tile LIMIT 10;", conn)
    print(df[name])

def make_map():
     
    with conn:
         c.execute("""CREATE TABLE IF NOT EXISTS tile (coords_x int, coords_y int, place_name text, rarity text, difficulty int, enterable boolean, tile_level int, exit_x int, exit_y int, discovord boolean)""")

def insert_tile(tile):
    
    with conn:
            c.execute("INSERT INTO tile VALUES (:coords_x, :coords_y, :place_name, :rarity, :difficulty, :enterable, :tile_level, :exit_x, :exit_y, :discovord)", 
            {'coords_x': tile.coords_x, 'coords_y': tile.coords_y, 'place_name': tile.name, 'rarity': tile.rarity, 'difficulty': tile.difficulty, 'enterable': tile.enterable, 'tile_level': tile.floor, 'exit_x': tile.exit_x, 'exit_y': tile.exit_y, 'discovord': tile.discovord})

def get_tile():
    c.execute("SELECT * FROM tile WHERE coords_x=100 AND coords_y=100;")
    return c.fetchall()

def get_all():
    c.execute("SELECT * FROM map;")
    return c.fetchall()

def update_tile():
    pass

#make_map()
#insert_tile(Tiles(200, 200, 'Cave', 'Common', 6, False, 0, 500, 500, False))
#neat_layout('place_name')
#print(get_tile())