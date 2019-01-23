import sqlite3
import pandas


##-- mapfile is the varible name of the file that the map is stored in --##
saveFile = 'player_data.db'

##-- Conn connects to the database --##
conn = sqlite3.connect(saveFile)

##-- c is what lets you write 
c = conn.cursor()


def neat_layout():
    df1 = pandas.read_sql_query("SELECT * FROM player ;", conn)
    print(df1)


def save_player_datebase():
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS player_stats (player_name TEXT, player_class TEXT, player_level INT, exp_amount INT, max_health INT, health INT, melee_attack INT, magic_attack INT, max_mana INT, mana INT, max_stamina INT, stamina INT, defence INT, pures INT, luck INT)""")
        c.execute("""CREATE TABLE IF NOT EXISTS player_inventory (inventory_item_limit INT, bag )""")

def get_player_info(x,y):
    c.execute("SELECT * FROM tile WHERE coords_x=:coords_x AND coords_y=:coords_y;", {'coords_x': x, 'coords_y': y})
    return c.fetchall()


def get_all():
    c.execute("SELECT * FROM player;")
    return c.fetchall()


def update_save(x,y,discovered):
    with conn:
        c.execute("""UPDATE tile SET discovered=:discovered WHERE coords_x=:coords_x AND coords_y=:coords_y""", 
        {'coords_x': x, 'coords_y': y, 'discovered': discovered})


# def insert_tile(tile):
#     with conn:
#         c.execute("INSERT INTO tile VALUES (:coords_x, :coords_y, :abriv, :place_name, :rarity, :difficulty, :enterable, :tile_level, :exit_x, :exit_y, :discovered)", 
#         {'coords_x': tile.coords_x, 'coords_y': tile.coords_y, 'abriv': tile.abriv, 'place_name': tile.name, 'rarity': tile.rarity, 'difficulty': tile.difficulty, 'enterable': tile.enterable, 'tile_level': tile.floor, 'exit_x': tile.exit_x, 'exit_y': tile.exit_y, 'discovered': tile.discovered})
