from typing import List, Dict

#Biome class used to create regions with the various aspects below.
#@Property decorator used for readibility and ease of class use later on.
class Biome(object):
    def __init__(self):
        self.name: str = None
        self.resources: List[str] = None
        self.spawns: List[str] = None
        self.rarity: str = None
        self.enterable: bool = None
        self.info: str = None
     
    # name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
        
    @name.deleter
    def name(self):
        del self._name
    
    # resources
    @property
    def resources(self):
        return self._resources
    
    @resources.setter
    def resources(self, resources: List[str]):
        self._resources = resources
        
    @resources.deleter
    def resources(self):
        del self._resources
     
    # spawns
    @property
    def spawns(self):
        return self._spawns
    
    @spawns.setter
    def spawns(self, spawns: List[str]):
        self._spawns = spawns
        
    @spawns.deleter
    def spawns(self):
        del self._spawns
     
    # rarity
    @property
    def rarity(self):
        return self._rarity
    
    @rarity.setter
    def rarity(self, rarity: str):
        self._rarity = rarity
        
    @rarity.deleter
    def rarity(self):
        del self._rarity
    
    # enterable
    @property
    def enterable(self):
        return self._enterable
    
    @enterable.setter
    def enterable(self, enterable: bool):
        self._enterable = enterable
        
    @enterable.deleter
    def enterable(self):
        del self._enterable
    
    # info
    @property
    def info(self):
        return self._info
    
    @info.setter
    def info(self, info: str):
        self._info = info
        
    @info.deleter
    def info(self):
        del self._info
