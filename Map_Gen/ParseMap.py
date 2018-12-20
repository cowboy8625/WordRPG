from Map_Gen import Biome

class Map:
    def __init__(self, map_file):
        self.map = open(map_file, 'r')
    """
    def populate(self):
        __map = self.parse()
        for y in range(len(__map)):
            for x in range(len(__map)):
                node = __map[x][y]
    """

    def parse(self):
        __map = list(self.map.read().split())

        for i in range(len(__map)):
            __map[i] = list(__map[i])

        return __map


mp = Map("World.map")
mp.populate()



