##-- This is dictionarys for all the biomes --##
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
'Field'              |'fld'|
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
world_biomes = {
    'for': {
            'name': 'Forest', 
            'resource': ['Wood'], 
            'spawns': ['Bandit', 'Wolf'],
            'rarity': 'Common'
        },

    'dfo': {
            'name': 'Dark Forest',
            'resource': ['Magic Wood'],
            'spawns': ['Dark Elif', 'Imp'],
            'rarity': 'Rare'
        },

    'cav': {
            'name': 'Cave',
            'resource': ['Rock', 'Bones'],
            'spawns': ['Skeleton', 'Bears', 'Zombie'],
            'rarity': 'Uncommon'
        },
     
     'wld': {
            'name': 'Woodlands',
            'resource': ['Logs'],
            'spawns': ['Earth Golem'],
            'rarity': 'Uncommon' 
        },
     
     'mou': {
            'name': 'Mountains',
            'resource': ['Rock', 'Flint'],
            'spawns': ['Rock', 'Flint'],
            'rarity': 'Uncommon'
        },

     'lak': {
            'name': 'Lake',
            'resource': ['Water'],
            'spawns': ['Earth Golem'],
            'rarity': 'Rare'
        },

      'rvr': {
             'name': 'Rive',
             'resource': ['Water'],
             'spawns': ['Earth Golem'],
             'rarity': 'Rare'
        },

       'twn': {
               'name': 'Town',
               'resource': ['NaN'],
               'spawns': ['NaN'],
               'rarity': 'Rare'
       },

       'vil': {
               'name': 'Village',
               'resource': ['NaN'],
               'spawns': ['NaN'],
               'rarity': 'Rare'
        },

        'fld': {
               'name': 'Field',
               'resource': ['Erb'],
               'spawns': ['Zombie'],
               'rarity': 'Common'
        },

        'frm': {
               'name': 'Farm',
               'resource': ['Erb'],
               'spawns': ['Zombie'],
               'rarity': 'Uncommon'
        }
}