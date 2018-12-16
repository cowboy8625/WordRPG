# This module will handle all Merchants; Also can handle any other type of NPC we add
class ArmorMerchant:
    def __init__(self, name):
        self.name = name
        self.for_sell = []
        self.gold_in = 0
        self.gold_out = 0
        self.item_in = ''
        self.item_out = ''

    def npc_inventory(self):
        return self.for_sell

    def buy(self, gold_in, item_out):
        self.gold_in = gold_in
        self.item_out = item_out
    
    def sell(self, gold_out, item_in):
        self.gold_out = gold_out
        self.item_in = item_in
