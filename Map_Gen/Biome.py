
"""
Biome names          |abriv|            Resourses                      |            Mob/Animal_Spawns

'Cave'               |'cav'|           'Rock', 'Bones'                       'Skeleton', 'Bears', 'Zombie'
'Forest'             |'for'|           'Wood'                                'Bandit', 'Wolf'
'Dark Forest'        |'dfo'|           'Magic Wood'                          'Dark Elf', 'Imp'
'Woodlands'          |'wld'|           'Logs'                                'Earth Golem'
'Mountains'          |'mou'|           'Rock', 'Flint'                       'Rock Golem'
'Lake'               |'lak'|           'Water', 'Fish'
'River'              |'rvr'|           'Water', 'Fish', 'Clay'
'Town'               |'twn'|
'Village'            |'vil'|
'Field'              |'fld'|           'Herb'
'Farm'               |'frm'|
'Grasslands'         |'gld'|        
'Wetlands'           |'wtd'|
'Salt Marsh'         |'stm'|           'Salt'
'Alpine Grasslands'  |'agl'|
'Marsh'              |'msh'|         
'Swamp'              |'swp'|
'Ocean'              |'ocn'|

Area Names:
North  if biome is -x is not its own biome and +x -y +y is same biome as its self.
"""
# Import Modules
import random
from Map_Gen import SubBiome


class Biome:
    def __init__(self, name=None, resources=None, spawns=None, enterable=None, rarity=None, info=None, prefix=None):
        self.prefix = prefix
        self.name = name
        self.resources = resources
        self.spawns = spawns
        self.enterable = enterable
        self.rarity = rarity
        self.info = info

    # This method is for dictionary indexing, mainly for backwords compatability with the rest of the code
    def __getitem__(self, item):
        if item not in ["name", "resource", "spawns", "rarity", "enterable", "info"]:
            raise IndexError("index {} is out of range".format(item))
        if item == "name":
            return self.name
        elif item == "resource":
            return self.resource
        elif item == "spawns":
            return self.spawns
        elif item == "rarity":
            return self.rarity
        elif item == "enterable":
            return self.enterable
        else:
            return self.info


# World Class to house to biomes
class World:
    vil = Biome(prefix="vil", name="Village", resources=None, spawns=None, enterable=True, rarity="Rare",
                info="A coloumn of smoke rises from a chimney. Could this be a place to rest?")
    frt = Biome(prefix="frt", name="Forest", resources=['Wood'], spawns=['Bandit', 'Wolf'], enterable=False,
                rarity="Common", info="Dark and ominous forest, filled with wolfs and bandits")
    dfo = Biome(prefix="dfo", name="Dark Forest", resources=['Magic Wood'], spawns=['Dark Elif', 'Imp'],
                enterable=False, rarity="Rare", info="Once a light place filled with life, now consumed by dark forces")
    cav = Biome(prefix="cav", name="Cave", resources=['Rock', 'Bones'], spawns=['Skeleton', 'Bears', 'Zombie'],
                enterable=True, rarity="Uncommon",
                info="Deep, dark and void of life. Who knows what could be down there")
    wld = Biome(prefix="wld", name="Woodlands", resources=['Logs'], spawns=['Earth Golem'], enterable=False,
                rarity="Uncommon",
                info="Peaceful place, little fairies, pretty flowers. Wait, whats the thumping noise?")
    mou = Biome(prefix="mou", name="Mountains", resources=['Rock', 'Flint'], spawns=['Yeti'], enterable=False,
                rarity="Uncommon", info="There could be anything hiding in the blizzards of the mountain")
    lak = Biome(prefix="lak", name="Lake", resources=['Water'], spawns=['Earth Golem'], enterable=True, rarity="Rare",
                info="Just a lake. Nothing to see here")
    rvr = Biome(prefix="rvr", name="River", resources=['Water'], spawns=['Earth Golem'], enterable=True, rarity="Rare",
                info="Running water, peaceful serenity. Finally")
    twn = Biome(prefix="twn", name="Town", resources=None, spawns=None, enterable=False, rarity="Rare",
                info="People going about their day, a sense of normality")
    fld = Biome(prefix="fld", name="Field", resources=['Herb'], spawns=['Zombie'], enterable=False, rarity="Common",
                info="Miles and miles of hay, theres no way there are any monsters here. Right?")
    frm = Biome(prefix="frm", name="Farm", resources=['Herb'], spawns=['Zombie'], enterable=False, rarity="Uncommon",
                info="Theres got to be something of value here")
    gld = Biome(prefix="gld", name="Grasslands", resources=['grass'],
                spawns=['Deer', 'Buffalo', 'Cow', 'Bull', 'Bandit', 'Bear'], enterable=False, rarity="Common",
                info="So much life. These grasslands provide habitat for more than just animals though...")
    stm = Biome(prefix="stm", name="Salt Marsh", resources=['Salt'], spawns=['Zombies'], enterable=False,
                rarity="Uncommon", info="I wonder what materials can be found in the SALT march")
    agl = Biome(prefix="agl", name="Alpine Grasslands", resources=['Pine'], spawns=['Zombie', 'Bandit'],
                enterable=False, rarity="Rare",
                info="High on the side of a mountain, these grasslands offer some very good hiding spots")
    msh = Biome(prefix="msh", name="Marsh", resources=['Crawfish'], spawns=['Zombie'], enterable=False, rarity="Rare",
                info="Spawnpy water to your knees. This is an unruly landscape")
    ocn = Biome(prefix="ocn", name="Ocean", resources=['Salt Water'], spawns=['Sea Monster'], enterable=False,
                rarity="Rare", info="Deep, dark, unexplored. Last great frontier")

    def __init__(self):
        # This is so I can write the next function
        self.biomes = [self.frt, self.dfo, self.cav, self.wld, self.mou,
                       self.lak, self.rvr, self.twn, self.vil, self.fld,
                       self.frm, self.gld, self.stm, self.agl, self.msh,
                       self.ocn]

    # returns Biome object
    def get_random_biome(self):
        return random.choice(self.biomes)


Wld = World()
BiomeDict = {
    # Forest
    'O': Wld.biomes[0],
    # Dark Forest
    'D': Wld.biomes[1],
    # Cave
    'C': Wld.biomes[2],
    # Woodlands
    'W': Wld.biomes[3],
    # Mountains
    'M': Wld.biomes[4],
    # Lake
    'L': Wld.biomes[5],
    # River
    'I': Wld.biomes[6],
    # Town
    'T': Wld.biomes[7],
    # Village
    'V': Wld.biomes[8],
    # Field
    'F': Wld.biomes[9],
    # Grasslands
    'G': Wld.biomes[10],
    # Wetlands
    'E': Wld.biomes[11],
    # Salt Marsh
    'S': Wld.biomes[12],
    # Alpine Grasslands
    'P': Wld.biomes[13],
    # Marsh
    'H': Wld.biomes[14],
    # Swamp
    'A': Wld.biomes[15],
    # Ocean
    '#': Wld.biomes[16]
}
