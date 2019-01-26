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
    "discovered":true
    }
##Keys:
- **village**		name of the tile in the Tilesets
- **color**		    string name of a color used to parse a map image into an array of
			        tiles
- **symbol**		the string character to display for this tile
- **font**		    color/style keywords used to format text when printed to terminal
- **movement**	    int value that represents how difficult a tile is to move into
- **description**	text used to describe the tile to the player
- **resources**	    list of resources that can be found in this tiles
- **discovered**	whether this tile starts as 'disovered' (IE visible to player)    