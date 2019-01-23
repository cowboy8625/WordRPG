##-- This Handles the inside of some biomes like Caves --##

'''
Caveren         |   'can'
Small Passage   |   'spg
'''
##-- i need to fix the second key handling --##

sub_biome = {'cav': {

                        'can': {
                            'name': 'Caveren',
                            'resource': ['Stone', 'Mossy'],
                            'spawns': ['Zombie', 'Bear', 'Skeleton'],
                            'pass_through': True

                        },

                        'spg': {
                            'name': 'Small Passage',
                            'resource': ['Stone', 'Mossy'],
                            'spawns': ['Zombie', 'Bear', 'Skeleton'],
                            'pass_through': True
                        
                        },

                        'wal': {
                            'name': '',
                            'resource': [],
                            'spawns': [],
                            'pass_through': False}
                    }
}  