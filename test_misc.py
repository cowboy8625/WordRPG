import os
import json

# get list of .json filenames in the 'tilesets' subfolder
DIRNAME = r'E:\Python\WordRPG\WordRPG\map'  #os.path.dirname(__file__)
FILEPATH = os.path.join(DIRNAME, 'tilesets')
TILESETS = []
for f in os.listdir(FILEPATH):
    if f.endswith('.json'):
        TILESETS.append(os.path.join(FILEPATH, f))


BIOMES = {
    'village':{'movement':1, 'color':'red', 'symbol':'±',
            'description':'YOU ARE IN A PEACEFUL VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'BLACK','bgcolor':'WHITE','style':'NORMAL'},
            'discovered':True
            },
    'cave':{'movement':1, 'color':'black', 'symbol':'▄',
            'description':'YOU ARE STANDING AT THE ENTRANCE TO A DEEP, DARK CAVE',
            'resources':None,
            '_format':{'fgcolor':'BLACK','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
            },
    'path':{'movement':1, 'color':'white', 'symbol':'·',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'BLACK','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
            'discovered':True
            },
    'farmland':{'movement':2, 'color':'magenta', 'symbol':'≡',
            'description':'YOU ARE IN A VILLAGE',
            'resources':['herb'],
            '_format':{'fgcolor':'LIGHTYELLOW_EX','bgcolor':'GREEN','style':'NORMAL'},
            },
    'beach':{'movement':2, 'color':'khaki', 'symbol':'░',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'WHITE','bgcolor':'YELLOW','style':'NORMAL'},
            },
    'desert':{'movement':4, 'color':'peru', 'symbol':'░',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'RED','bgcolor':'YELLOW','style':'NORMAL'},
            },
    'grassland':{'movement':2, 'color':'lawngreen', 'symbol':' ',
            'description':'YOU ARE IN A VILLAGE',
            'resources':None,
            '_format':{'fgcolor':'LIGHTYELLOW_EX','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
            },
    'forest':{'movement':3, 'color':'olivedrab', 'symbol':'♣',
            'description':'YOU ARE IN THE FOREST',
            'resources':['wood'],
            '_format':{'fgcolor':'GREEN','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
            },
    'deep_forest':{'movement':4, 'color':'darkgreen', 'symbol':'♣',
            'description':'YOU ARE IN THE DEEP, DARK FOREST',
            'resources':None,
            '_format':{'fgcolor':'LIGHTGREEN_EX','bgcolor':'BLACK','style':'NORMAL'},
            },
    'river':{'movement':2, 'color':'cyan', 'symbol':'~',
            'description':'YOU ARE ON THE RIVER',
            'resources':['water', 'fish'],
            '_format':{'fgcolor':'BLUE','bgcolor':'CYAN','style':'NORMAL'},
            },
    'lake':{'movement':3, 'color':'darkcyan', 'symbol':'~',
            'description':'YOU ARE ON A LAKE',
            'resources':['water', 'fish'],
            '_format':{'fgcolor':'CYAN','bgcolor':'BLUE','style':'NORMAL'},
            },
    'swamp':{'movement':5, 'color':'darkolivegreen', 'symbol':'▒',
            'description':'YOU ARE IN THE SWAMP',
            'resources':None,
            '_format':{'fgcolor':'RED','bgcolor':'GREEN','style':'NORMAL'},
            },
    'salt_marsh':{'movement':4, 'color':'darkseagreen', 'symbol':'▒',
            'description':'YOU ARE IN THE SALT MARSH',
            'resources':['fish', 'salt'],
            '_format':{'fgcolor':'GREEN','bgcolor':'BLUE','style':'NORMAL'},
            },
    'alpine_grassland':{'movement':1, 'color':'lightgreen', 'symbol':'░',
            'description':'YOU ARE IN THE ALPINE GRASSLAND',
            'resources':['pine'],
            '_format':{'fgcolor':'WHITE','bgcolor':'LIGHTGREEN_EX','style':'NORMAL'},
            },
    'mountain':{'movement':-1, 'color':'darkslategray', 'symbol':'^',
            'description':'YOU ARE IN THE MOUNTAINS',
            'resources':None,
            '_format':{'fgcolor':'WHITE','bgcolor':'LIGHTBLACK_EX','style':'NORMAL'},
            },
    'ocean':{'movement':-1, 'color':'blue', 'symbol':'~',
            'description':'YOU ARE IN THE OCEAN',
            'resources':None,
            '_format':{'fgcolor':'BLACK','bgcolor':'BLUE','style':'NORMAL'},
            'discovered':True
            },
    }


filename = TILESETS[0]
print(filename)
test = json.loads(filename)
print(test)

# print(json.dumps(BIOMES))

# TILESETS = { os.path.basename(filename):json.loads(filename) for filename in TILESETS }
# print( TILESETS )