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
        super.__init__(name)