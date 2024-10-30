import entity 
import random

class Enemy(entity.Entity):
    '''Enemy – extends entity - monster character that the hero encounters in the maze.
        a. __init__(self) – randomizes a name from a list of names (ex. ‘Goblin’, ‘Vampire’,
        ‘Ghoul’, ‘Skeleton’, ‘Zombie, etc) and randomizes the monster’s hp (4-8).
        b. attack(self, entity) – enemy attacks hero – randomize damage in the range 1-4.
        The hero should take the damage and the method should return a string
        representing the event.
    '''
    _monsters = ['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie']

    def __init__(self):
        name = random.choice(self._monsters)
        hp = random.randint(4, 8)
        super().__init__(name, hp)

    def attack(self, entity):
        '''Attack the player, dealing random damage between 1 and 4.'''
        damage = random.randint(1, 4)
        entity.take_damage(damage)
        return f'{self._name} attacks {entity._name} for {damage} damage.'
