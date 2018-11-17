##-- Import --##

import os
import time
import random
import sqlite3
import pandas


##-- Custom Import --##

from Map_Gen import Biome


#  Clears print screen

def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

class Tile:

    def __init__(self, coords_x, coords_y, name, rarity, difficulty, enterable=False, discovord=False):

        self.coords_x = coords_x
        self.coords_y = coords_y
        self.name = name
        self.rarity = rarity ##-- How often you need to be spawned --##
        self.difficulty = difficulty
        self.enterable = enterable ##-- True or False --##
        self.floor = 0  ##-- in SQL it is coord_y_level --##
        self.next_to = 0
        self.avoid = 0
        self.exit_x = 0
        self.exit_y = 0
        self.discovord = discovord 


def get_random_biome():
    biome_keys = Biome.world_biomes.keys()

    list_of_biome_abriv = []

    for bio in biome_keys:
        list_of_biome_abriv.append(bio)

    random_biome = random.choice(list_of_biome_abriv)
    return random_biome


    

##-- Map Width and Hight                                                        --##
##-- I am thinking maybe start with a 50 x 50 map but when all is said and done --##
##-- 1000 x 1000 will be the map size                                           --##
 
map_width = 10  
map_hight = 10   

map_list = []

#  coords
x = 1
y = 1

left_side = [i for i in range(0, (map_width * map_hight), map_width)]
right_side = [i for i in range(map_width - 1, (map_width * map_hight), map_width)]

##-- Gets a random number to set biome difficulty --##
def ran_diff():
    num = random.randint(1, 10)
    return num
##-- Map is placed in to a class here --##

def map_builder():

    for spot in range(0, (map_width * map_hight)):
        coord_y = int((spot / map_width))
        coord_x = spot - (map_width * coord_y)
        biome = get_random_biome()
        map_list.append(biome)
        insert_tile(Tile(coord_x, coord_y, Biome.world_biomes[biome]['name'], Biome.world_biomes[biome]['rarity'], 
        difficulty=ran_diff()))

mapfile = 'Worldmap.db'
conn = sqlite3.connect(mapfile)
c = conn.cursor()


def neat_layout():

    df = pandas.read_sql_query("SELECT * FROM tile ;", conn)
    print(df)

def make_map_datebase():
     
    with conn:
         c.execute("""CREATE TABLE IF NOT EXISTS tile (coords_x int, coords_y int, place_name text, rarity text, difficulty int, enterable boolean, tile_level int, exit_x int, exit_y int, discovord boolean)""")

def insert_tile(tile):
    
    with conn:
            c.execute("INSERT INTO tile VALUES (:coords_x, :coords_y, :place_name, :rarity, :difficulty, :enterable, :tile_level, :exit_x, :exit_y, :discovord)", 
            {'coords_x': tile.coords_x, 'coords_y': tile.coords_y, 'place_name': tile.name, 'rarity': tile.rarity, 'difficulty': tile.difficulty, 'enterable': tile.enterable, 'tile_level': tile.floor, 'exit_x': tile.exit_x, 'exit_y': tile.exit_y, 'discovord': tile.discovord})

def get_tile(x,y):
    c.execute("SELECT * FROM tile WHERE coords_x=:coords_x AND coords_y=:coords_y;", {'coords_x': x, 'coords_y': y})
    return c.fetchall()
    #print(c.fetchall())

def get_all():
    c.execute("SELECT * FROM map;")
    return c.fetchall()

def update_tile():
    pass

#make_map_datebase()
#map_builder()
#neat_layout()
# print('---------------------------------------------------------------')
#print(get_tile(0,0))