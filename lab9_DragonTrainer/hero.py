import entity

class Hero(entity.Entity):
    '''
    Hero Class (hero.py) – inherits from Entity
        1. basic_attack(self, opponent) – the drago takes a random amount of damage in the
        range 2D6 (1-6 + 1-6). Return a string with the description of the attack and the damage
        dealt to the dragon.
        2. special_attack(self, opponent) – the dragon takes a random amount of damage in
        the range 1D12 (1-12). Return a string with the description of the attack and the damage
        dealt to the dragon.
    '''
    def basic_attack(self, opponent):
        return 0
    
    def special_attack(self, opponent):
        return 0