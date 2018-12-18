# Import
import os
import time
import random
import sqlite3
import pandas

# Custom Import
# from Map_Gen import Biome

from Map_Gen import Biome
from Map_Gen import SubBiome

# GLOBAL VARIABLES
# Map Width and Height
# I am thinking maybe start with a 50 x 50 map but when all is said and done
# 1000 x 1000 will be the map size
map_width = 100
map_height = 100
sub_map_width = 10
sub_map_height = 10
map_seed = []

#  coords
x = 1
y = 1


# Clears print screen
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


# This is the blueprint of the tiles or biomes
class Tile:
    def __init__(self, coords_x, coords_y, abriv, name, rarity, difficulty,
                 enterable, exit_x, exit_y, discovered=False):
        self.coords_x = coords_x
        self.coords_y = coords_y
        self.abriv = abriv
        self.name = name
        self.rarity = rarity  # How often you need to be spawned
        self.difficulty = difficulty
        self.enterable = enterable  # True or False
        self.floor = 0  # in SQL it is tile_level
        self.exit_x = exit_x
        self.exit_y = exit_y
        self.discovered = discovered


class SubTile:
    def __init__(self, from_x, from_y, coords_x, coords_y, biome_name, place_name, difficulty):
        self.from_x = from_x
        self.from_y = from_y
        self.coords_x = coords_x
        self.coords_y = coords_y
        self.biome_name = biome_name
        self.place_name = place_name
        self.difficulty = difficulty
        self.floor = 1  # in SQL it is tile_level
        self.discovered = False


def get_random_sub_biome(key):
    biome_keys = SubBiome.sub_biome[key].keys()
    list_of_sub_biome_abriv = []

    for bio in biome_keys:
        list_of_sub_biome_abriv.append(bio)

    return random.choice(list_of_sub_biome_abriv)


def set_exit_coords_x():
    return random.randint(0, sub_map_width)


def set_exit_coords_y():
    return random.randint(0, sub_map_height)


# right now there is only Common Uncommon and Rare, But maybe i will add Epic as well
def rare_control():
    while True:
        r_biome = Biome.World.get_random_biome()
        if r_biome.rarity == 'Rare':
            num = random.randint(0, 100)

            if num == 50:
                return r_biome

        elif r_biome.rarity == 'Uncommon':
            num = random.randint(0, 20)

            if num == 10:
                return r_biome

        elif r_biome.rarity == 'Common':
            return r_biome


# Gets a random number to set biome difficulty
def ran_diff():
    return random.randint(1, 10)


# Map is placed into a class here
def map_builder():
    loading_dots = 0
    clear()
    print('Loading.')
    for spot in range(0, (map_width * map_height)):
        # spot is index and coord_x and coord_y is finding the (x, y) coordinates from index (AKA spot)
        if spot in [10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]:
            loading_dots += 1
            clear()
            print('-------------------')
            print('Loading' + '.' * loading_dots)
            print('-------------------')

        coord_y = int((spot / map_width))
        coord_x = spot - (map_width * coord_y)
        biome = rare_control()
        map_seed.append(biome.prefix)
        biome_name = biome.name
        biome_rarity = biome.rarity
        biome_layers = biome.enterable
        # coords_x, coords_y, name, rarity, difficulty, enterable=False, discovered=False
        # coords_x, coords_y, name,        rarity,     difficulty, enterable, exit_x, exit_y, discovered=False
        insert_tile(
            Tile(coord_x, coord_y, biome, biome_name, biome_rarity, ran_diff(), biome_layers, set_exit_coords_x(),
                 set_exit_coords_y()))
        if biome_layers:
            for subspot in range(0, (sub_map_width * sub_map_height)):
                sub_coord_y = int((subspot / sub_map_width))
                sub_coord_x = subspot - (sub_map_width * sub_coord_y)
                # print(f"X: {coord_x}")
                # print(f"Y: {coord_y}")
                # print(f"SUB X: {sub_coord_x}")
                # print(f"SUB Y: {sub_coord_y}")
                # input("Enter")
                try:
                    sub_biome_name = SubBiome.sub_biome[biome.prefix][get_random_sub_biome(biome.prefix)]['name']

                except:
                    continue
                insert_subtile(
                    SubTile(coord_x, coord_y, sub_coord_x, sub_coord_y, biome_name, sub_biome_name, ran_diff()))


# mapfile is the varible name of the file that the map is stored in
mapfile = 'Worldmap.db'

# Conn connects to the database
conn = sqlite3.connect(mapfile)

# c is what lets you write
c = conn.cursor()


def neat_layout():
    df1 = pandas.read_sql_query("SELECT * FROM tile ;", conn)
    df2 = pandas.read_sql_query("SELECT * FROM subTile ;", conn)
    print(df1)
    print("\n--------------------------------------------------------------------------------------------------\n")
    print(df2)


def make_map_datebase():
    with conn:
        c.execute(
            """CREATE TABLE IF NOT EXISTS tile (coords_x int, 
            coords_y int, 
            abriv text, 
            place_name text, 
            rarity text, 
            difficulty int, 
            enterable boolean, 
            tile_level int, 
            exit_x int, 
            exit_y int, 
            discovered boolean)""")
        c.execute(
            """CREATE TABLE IF NOT EXISTS subTile (from_x int, 
            from_y int, 
            coords_x int, 
            coords_y int, 
            biome_name text, 
            place_name text, 
            difficulty int, 
            tile_level int, 
            discovered boolean)""")


def insert_tile(tile):
    with conn:
        c.execute(
            "INSERT INTO tile VALUES (:coords_x, "
            ":coords_y, "
            ":abriv, "
            ":place_name, "
            ":rarity, "
            ":difficulty, "
            ":enterable, "
            ":tile_level, "
            ":exit_x, "
            ":exit_y, "
            ":discovered)",
            {'coords_x': tile.coords_x, 'coords_y': tile.coords_y, 'abriv': tile.abriv, 'place_name': tile.name,
             'rarity': tile.rarity, 'difficulty': tile.difficulty, 'enterable': tile.enterable,
             'tile_level': tile.floor, 'exit_x': tile.exit_x, 'exit_y': tile.exit_y, 'discovered': tile.discovered})


def insert_subtile(subtile):
    with conn:
        c.execute(
            "INSERT INTO subTile VALUES (:from_x, "
            ":from_y, "
            ":coords_x, "
            ":coords_y, "
            ":biome_name, "
            ":place_name, "
            ":difficulty, "
            ":tile_level, "
            ":discovered)",
            {'from_x': subtile.from_x, 'from_y': subtile.from_y, 'coords_x': subtile.coords_x,
             'coords_y': subtile.coords_y, 'biome_name': subtile.biome_name, 'place_name': subtile.place_name,
             'difficulty': subtile.difficulty, 'tile_level': subtile.floor, 'discovered': subtile.discovered})


def get_tile(x, y):
    c.execute("SELECT * FROM tile WHERE coords_x=:coords_x AND coords_y=:coords_y;", {'coords_x': x, 'coords_y': y})
    return c.fetchall()


def get_subTile(from_x, from_y, x, y):
    c.execute(
        "SELECT * FROM subTile WHERE from_x=:from_x AND from_y=:from_y AND coords_x=:coords_x AND coords_y=:coords_y;",
        {'from_x': from_x, 'from_y': from_y, 'coords_x': x, 'coords_y': y})
    return c.fetchall()


def get_all():
    c.execute("SELECT * FROM map;")
    return c.fetchall()


def update_tile(x, y, discovered):
    with conn:
        c.execute("""UPDATE tile SET discovered=:discovered WHERE coords_x=:coords_x AND coords_y=:coords_y""",
                  {'coords_x': x, 'coords_y': y, 'discovered': discovered})


def update_subTile(from_x, from_y, x, y, discovered):
    with conn:
        c.execute(
            """UPDATE subTile SET discovered=:discovered WHERE 
            from_x=:from_x AND from_y=:from_y AND coords_x=:coords_x AND coords_y=:coords_y""",
            {'from_x': from_x, 'from_y': from_y, 'coords_x': x, 'coords_y': y, 'discovered': discovered})
