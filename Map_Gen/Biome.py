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
    'for': {
            'name': 'Forest', 
            'resource': ['Wood'], 
            'spawns': ['Bandit', 'Wolf'],
            'rarity': 'Common',
            'enterable': False,
            'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

    'dfo': {
            'name': 'Dark Forest',
            'resource': ['Magic Wood'],
            'spawns': ['Dark Elif', 'Imp'],
            'rarity': 'Rare',
            'enterable': False,
            'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

    'cav': {
            'name': 'Cave',
            'resource': ['Rock', 'Bones'],
            'spawns': ['Skeleton', 'Bears', 'Zombie'],
            'rarity': 'Uncommon',
            'enterable': True,
            'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },
     
     'wld': {
            'name': 'Woodlands',
            'resource': ['Logs'],
            'spawns': ['Earth Golem'],
            'rarity': 'Uncommon',
            'enterable': False,
            'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },
     
     'mou': {
            'name': 'Mountains',
            'resource': ['Rock', 'Flint'],
            'spawns': ['Yeti'],
            'rarity': 'Uncommon',
            'enterable': False,
            'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

     'lak': {
            'name': 'Lake',
            'resource': ['Water'],
            'spawns': ['Earth Golem'],
            'rarity': 'Rare',
            'enterable': True,
            'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

      'rvr': {
             'name': 'Rive',
             'resource': ['Water'],
             'spawns': ['Earth Golem'],
             'rarity': 'Rare',
             'enterable': True,
             'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

       'twn': {
               'name': 'Town',
               'resource': ['NaN'],
               'spawns': ['NaN'],
               'rarity': 'Rare',
               'enterable': False,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
       },

       'vil': {
               'name': 'Village',
               'resource': ['NaN'],
               'spawns': ['NaN'],
               'rarity': 'Rare',
               'enterable': True,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

        'fld': {
               'name': 'Field',
               'resource': ['Herb'],
               'spawns': ['Zombie'],
               'rarity': 'Common',
               'enterable': False,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

        'frm': {
               'name': 'Farm',
               'resource': ['Erb'],
               'spawns': ['Zombie'],
               'rarity': 'Uncommon',
               'enterable': False,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

        'gld': {
               'name': 'Grasslands',
               'resource': ['grass'],
               'spawns': ['Deer', 'Buffalo', 'Cow', 'Bull', 'Bandit', 'Bear'],
               'rarity': 'Common',
               'enterable': False,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

        'wtd': {
               'name': 'Wetlands',
               'resource': ['None'],
               'spawns': ['None'],
               'rarity': 'Common',
               'enterable': False,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

        'stm': {
               'name': 'Salt Marsh',
               'resourse': ['Salt'],
               'spawns': ['Zombies'],
               'rarity': 'Uncommon',
               'enterable': False,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

        'agl': {
               'name': 'Alpine Grasslands',
               'resourse': ['Pine'],
               'spawns': ['Zombie', 'Bandit'],
               'rarity': 'Rare',
               'enterable': False,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

        'msh': {
               'name': 'Marsh',
               'resourse': ['Crawfish'],
               'spawns': ['Zombie'],
               'rarity': 'Rare',
               'enterable': False,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        },

        'ocn': {
               'name': 'Ocean',
               'resourse': ['Salt Water'],
               'spawns': ['Sea Monster'],
               'rarity': 'Rare',
               'enterable': False,
               'info': "FILL IN A QUICK ANSWER ABOUT BIOME"
        }
}
