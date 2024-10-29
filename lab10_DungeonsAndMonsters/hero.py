import entity

class Hero(entity.Entity):
    '''
    Hero – extends entity - the user’s character
        a. __init__(self, name) – initializes the name and max_hp using super, sets the
        hero’s starting location to row=0, col=0.
        b. attack(self, entity) – hero attacks the enemy – randomize damage in the range 2-5,
        the enemy should take the damage and the method should return a string
        representing the event.
        c. go_north/south/east/west(self) – update the hero’s location by adding or
        subtracting 1 to the row or column, but only if that location is within the bounds
        of the map (between 0 and the len(map)-1). If it is, return the character at that
        location, if it isn’t, return an ‘o’ to signify that the direction is out of bounds.
    '''
    def __init__(self, name):
        '''Initialize the Hero, setting its name, max HP, and starting location.'''
        super().__init__(name, 25)
        self._row = 0
        self._col = 0

    def attack(self, entity):
        '''Attack an entity, dealing random damage between 2 and 5.'''
        from random import randint
        damage = randint(2, 5)
        entity.take_damage(damage)
        return f'{self._name} attacks {entity._name} for {damage} damage.'

    def go_north(self):
        '''Move the hero one step north if possible.'''
        if self._row > 0:
            self._row -= 1
            return self._map[self._row][self._col]
        return 'o'

    def go_south(self):
        '''Move the hero one step south if possible.'''
        if self._row < 9:
            self._row += 1
            return self._map[self._row][self._col]
        return 'o'

    def go_east(self):
        '''Move the hero one step east if possible.'''
        if self._col < 9:
            self._col += 1
            return self._map[self._row][self._col]
        return 'o'

    def go_west(self):
        '''Move the hero one step west if possible.'''
        if self._col > 0:
            self._col -= 1
            return self._map[self._row][self._col]
        return 'o'
