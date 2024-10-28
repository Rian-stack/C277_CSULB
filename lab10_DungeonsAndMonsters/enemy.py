import entity 

class Enemy(entity.Entity):
    '''Enemy – extends entity - monster character that the hero encounters in the maze.
        a. __init__(self) – randomizes a name from a list of names (ex. ‘Goblin’, ‘Vampire’,
        ‘Ghoul’, ‘Skeleton’, ‘Zombie, etc) and randomizes the monster’s hp (4-8).
        b. attack(self, entity) – enemy attacks hero – randomize damage in the range 1-4.
        The hero should take the damage and the method should return a string
        representing the event.
    '''
    def __init__(self):
        self._monsters = monsters
        monsters = []