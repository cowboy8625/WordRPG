from Map_Gen import Biome


class Map:
    def __init__(self, map_file):
        self.map = open(map_file, 'r')
        self.mapList = self.parse()

    def access_information(self, x, y, item):
        _biome = Biome.BiomeDict[self.mapList[x][y]]
        if item == "Name":
            return _biome.name
        elif item == "Crossable":
            return _biome.crossable

    def parse(self):
        __map = list(self.map.read().split())

        for i in range(len(__map)):
            __map[i] = list(__map[i])

        return __map

    def get_length(self):
        return len(self.mapList)


WorldMap = Map("Map_Gen/World.map")
