#\[tileset\].json
Tilesets are defined as JSON files in the following format:

##'Tile' Example:
"village":{
	"color":"red",
	"symbol":"±",
    "font":{
        "fgcolor":"BLACK",
        "bgcolor":"WHITE",
        "style":"NORMAL"
        },
    "movement":1,
    "description":"YOU ARE IN A PEACEFUL VILLAGE",
    "resources":[ ],
    "discovered":true,
    "default":true,
    }

##Keys:
- **village**		name of the tile in the Tilesets
- **color**		    string name of a color used to parse a map image into an
                    array of tiles
- **symbol**		the string character to display for this tile
- **font**		    color/style keywords used to format text when printed to
                    terminal(see Font below)
- **movement**	    int value that represents how difficult a tile is to move
                    into
- **description**	text used to describe the tile to the player
- **resources**	    list of resources that can be found in this tiles
- **discovered**	whether this tile starts as 'disovered'
- **default**	    if this flag is True, this Tile should be used for any out
                    of range Tiles when the sub-map is generated

###Font:
colorama supported color and style names:
    **fgcolor/bgcolor**:
        'BLACK', 'BLUE', 'CYAN', 'GREEN', 'LIGHTBLACK_EX', 'LIGHTBLUE_EX',
        'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX', 'LIGHTRED_EX',
        'LIGHTWHITE_EX', 'LIGHTYELLOW_EX', 'MAGENTA', 'RED', 'RESET',
        'WHITE', 'YELLOW'
    **style**:
        'BRIGHT', 'DIM', 'NORMAL', 'RESET_ALL'