

class Map:
    def __init__(self, map_file):
        self.map = open(map_file, 'r')

    def parse(self):
        __map = list(self.map.read().split())

        for i in range(len(__map)):
            __map[i] = list(__map[i])

        return __map


