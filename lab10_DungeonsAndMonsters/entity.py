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
        self._hp = max_hp

    def take_damage(self, dmg):
        '''Method to reduce hp by dmg taken'''
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    def heal(self):
        '''Method to reset hp to max_hp'''
        self._hp = self._max_hp

    def __str__(self):
        '''Method to return a formatted string of the entity'''
        return f'{self._name}\nHP: {self._hp}/{self._max_hp}'

    @abc.abstractmethod
    def attack(self, entity):
        '''Abstract method to attack another entity'''
        pass
