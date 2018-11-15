##-- This is dictionarys for all the biomes --##
'''
Biome names          |abriv|            Resourses                      |            Mob/Animal_Spawns

'Cave'               |'cav'|           'Rock', 'Bones'                       'Skeleton', 'Bears', 'Zombie'
'Forest'             |'for'|           'Wood'                                'Bandit', 'Wolf'
'Dark Forest'        |'dfo'|           'Magic Wood'                          'Dark Elif', 'Imp'
'Woodlands'          |'wld'|           'Logs                                 'Earth Golem'
'Mountains'          |'mou'|           'Rock', 'Flint'                       'Rock Golem'
'Lake'               |'lak'|           'Water', 'Fish'
<<<<<<< HEAD
'River'              |'rvr'|           'Water', 'Fish', 'Clay'
=======
'River'              |'rvr'|           'Water', 'Fish'
>>>>>>> 2d88f5a0cb160ebb7f0103c9757b96671ad03936
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
            'resource': 'wood', 
            'spawns': ['Bandit', 'Wolf']
    },
    'dfo': {
            'name': 'Dark Forest',
            'resource': 'wood',
            'spawns': ['Dark Elif', 'Imp']
    },

    'cav': {
            'name': 'Cave',
            'resource': 'wood',
            'spawns': ['Skeleton', 'Bears', 'Zombie']
    }
            }