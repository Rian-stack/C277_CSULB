import abc

class Entity(abc.ABC):
    '''
    Entity – abstract class - describes a character in the game.
        a. __init__(self, name, max_hp) – initializes each of the instance variables
        b. take_damage(self, dmg) – subtracts the dmg from the hp, but does not allow the
        hp to drop below 0.
        c. heal(self) – restores the entity’s hp to max_hp.
        d. __str__(self) – returns a string in the format ‘Name\nHP: hp/max_hp’.
        e. attack(self, entity) – abstract method (no code) that all entity subclasses will
        override to attack and do damage to the opposing entity.
    '''
    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp