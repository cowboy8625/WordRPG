##-- Functions and the all around map frame work goes here --##

##-- This is a simple drawing of the map             --##
##-- I would like to make amap generator             --##
##-- But we can work on that once the game functions --##
'''
 1 2 3
1 | | 
 -|-|-
2 | | 
 -|-|-
3 | | 
'''

map = {
    (1,1): {'name': 'Forest', 'difficulty': 1},
    (1,2): {'name': 'Dark Forest', 'difficulty': 3},
    (1,3): {'name': 'Vallie Town', 'difficulty': 0},
    (2,1): {'name': 'Cave', 'difficulty': 4},
    (2,2): {'name': 'Field', 'difficulty': 2},
    (2,3): {'name': 'Farm', 'difficulty': 2},
    (3,1): {'name': 'River', 'difficulty': 3},
    (3,2): {'name': 'Moutains', 'difficulty': 1},
    (3,3): {'name': 'Lake', 'difficulty': 2}
}