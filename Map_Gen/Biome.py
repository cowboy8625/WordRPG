#-- This is dictionarys for all the biomes --#
'''
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
'''
##-- Import Modules --##

from Map_Gen import SubBiome


class Biome:
    def __init__(self, name=None, resources=None, spawns=None, enterable=None, rarity=None, info=None):
        self.name = name
        self.resources = resources
        self.spawns = spawns
        self.enterable = enterable
        self.rarity = rarity
        self.info = info
    ## -- This method is for dictionary indexing, mainly for backwords compatability with the rest of the code -- ##
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
##-- Biome Dictionarys --##
world_biomes = {
    'for': Biome(name="Forest", resources=['Wood'], spawns=['Bandit', 'Wolf'], enterable=False, rarity="Common", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'dfo': Biome(name="Dark Forest", resources=['Magic Wood'], spawns=['Dark Elif', 'Imp'], enterable=False, rarity="Rare", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'cav': Biome(name="Cave", resources=['Rock', 'Bones'], spawns=['Skeleton', 'Bears', 'Zombie'], enterable=True, rarity="Uncommon", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'wld': Biome(name="Woodlands", resources=['Logs'], spawns=['Earth Golem'], enterable=False, rarity="Uncommon", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'mou': Biome(name="Mountains", resources=['Rock', 'Flint'], spawns=['Yeti'], enterable=False, rarity="Uncommon", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'lak': Biome(name="Lake", resources=['Water'], spawns=['Earth Golem'], enterable=True, rarity="Rare", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'rvr': Biome(name="River", resources=['Water'], spawns=['Earth Golem'], enterable=True, rarity="Rare", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'twn': Biome(name="Town", resources=['NaN'], spawns=['NaN'], enterable=False, rarity="Rare", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'vil': Biome(name="Village", resources=['NaN'], spawns=['NaN'], enterable=True, rarity="Rare", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'fld': Biome(name="Field", resources=['Herb'], spawns=['Zombie'], enterable=False, rarity="Common", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'frm': Biome(name="Farm", resources=['Erb'], spawns=['Zombie'], enterable=False, rarity="Uncommon", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'gld': Biome(name="Grasslands", resources=['grass'], spawns=['Deer', 'Buffalo', 'Cow', 'Bull', 'Bandit', 'Bear'], enterable=False, rarity="Common", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'wtd': Biome(name="Grasslands", resources=['grass'], spawns=['Deer', 'Buffalo', 'Cow', 'Bull', 'Bandit', 'Bear'], enterable=False, rarity="Common", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'stm': Biome(name="Salt Marsh", resources=['Salt'], spawns=['Zombies'], enterable=False, rarity="Uncommon", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'agl': Biome(name="Alpine Grasslands", resources=['Pine'], spawns=['Zombie', 'Bandit'], enterable=False, rarity="Rare", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'msh': Biome(name="Marsh", resources=['Crawfish'], spawns=['Zombie'], enterable=False, rarity="Rare", info="FILL IN A QUICK ANSWER ABOUT BIOME"),
    'ocn': Biome(name="Ocean", resources=['Salt Water'], spawns=['Sea Monster'], enterable=False, rarity="Rare", info="FILL IN A QUICK ANSWER ABOUT BIOME")
}
