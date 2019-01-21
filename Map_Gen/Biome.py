
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


class Biome:
    def __init__(self, name=None, resources=None, spawns=None, enterable=None, rarity=None, info=None, prefix=None,
                 crossable=True):
        self.prefix = prefix
        self.name = name
        self.resources = resources
        self.spawns = spawns
        self.enterable = enterable
        self.rarity = rarity
        self.info = info
        self.crossable = crossable

    # This method is for dictionary indexing, mainly for backwords compatability with the rest of the code
    def __getitem__(self, item):
        if item not in ["name", "resource", "spawns", "rarity", "enterable", "info"]:
            raise IndexError("index {} is out of range".format(item))
        if item == "name":
            return self.name
        elif item == "resource":
            return self.resources
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
                rarity="Rare", info="Deep, dark, unexplored. Last great frontier", crossable=False)
    rod = Biome(prefix="rod", name="Road", resources=[], spawns=[], enterable=True, rarity="Common",
                info="A safe, protected, pathway for travels and trading", crossable=True)
    # TODO: Add spawns\resources to this biome
    bch = Biome(prefix="Bch", name="Beach", resources=[], spawns=[], enterable=True, rarity="Common",
                info="A nice, relaxing place to spend the summer. Just watch your toes for crabs", crossable=True)

    def __init__(self):
        # This is so I can write the next function
        self.BiomeDict = {
            # Forest
            'O': self.frt,
            # Dark Forest
            'D': self.dfo,
            # Cave
            'C': self.cav,
            # Woodlands
            'W': self.wld,
            # Mountains
            'M': self.mou,
            # Lake
            'L': self.lak,
            # River
            'I': self.rvr,
            # Town
            'T': self.twn,
            # Village
            'V': self.vil,
            # Field
            'E': self.fld,
            # Farm
            'F': self.frm,
            # Grasslands
            'G': self.gld,
            # Salt Marsh
            'S': self.stm,
            # Alpine Grasslands
            'P': self.agl,
            # Marsh
            'H': self.msh,
            # Ocean
            '#': self.ocn,
            # Road
            'R': self.rod,
            # Beach
            'B': self.bch
        }


Wld = World()

