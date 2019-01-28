__author__ = 'byteme8bit'

# File imports
from Map_Gen.ParseMap import WorldMap
from Mechanics.ui_mechanics import clear, pause

# Module imports


class Character:        # Base class
    def __init__(self, name, level):
        self.char_name = name
        self.level = level


class Player(Character):        # User's entity
    def __init__(self, name, level, health_points, char_class):
        super().__init__(name, level)
        self.type = char_class
        self.exp = 0
        self.hp = health_points
        self.pos_x = 0
        self.pos_y = 0

        self.inventory = []
        self.inventory_limit = 0

    def melee_attack(self):
        return 17

    def magic_attack(self):
        pass

    def health_generation(self):
        pass

    def move(self, _dir):
        directions = {"North": (0, -1), "South": (0, 1), "East": (1, 0), "West": (-1, 0)}
        delta_x, delta_y = directions[_dir]
        new_x, new_y = self.pos_x + delta_x, self.pos_y + delta_y
        if WorldMap.access_information(new_x, new_y, "Crossable"):
            self.pos_x, self.pos_y = new_x, new_y
        else:
            clear()
            print("You cannot cross here:")
            print(WorldMap.access_information(new_x, new_y, "Name"))
            pause()

    # Add item to inventory if space is available
    # Return true if add was successful
    def add_to_inv(self, item):
        if len(self.inventory) >= self.inventory_limit:
            return False
        self.inventory.append(item)

    # Remove item at given position
    def remove_from_inv(self, index):
        if index in range(len(self.inventory)):
            del self.inventory[index]
        else:
            raise ValueError(f'Index {index} invalid for inventory {self.inventory}')

    # TODO methods like this should probably be moved to mechanics
    # the script classes shouldn't be dealing with UI, only handling the class instances
    def inspect_area(self):
        info = {
            "Name": WorldMap.access_information(self.pos_x, self.pos_y, "Name"),
            "Resources": WorldMap.access_information(self.pos_x, self.pos_y, "Resources"),
            "Spawns": WorldMap.access_information(self.pos_x, self.pos_x, "Spawns"),
            "Info": WorldMap.access_information(self.pos_x, self.pos_y, "Info")
        }
        clear()
        print("Name: " + str(info["Name"]))
        print("Resources: " + str(info["Resources"]))
        print("Spawns: " + str(info["Spawns"]))
        print("Info: " + str(info["Info"]))
        pause()


class Mob(Character):       # Combat based entities
    def __init__(self, name, level, health_points):
        super().__init__(name, level)
        self.hp = health_points

    def melee_attack(self):
        return 5


class NPC(Character):       # Non-combat entities
    pass
