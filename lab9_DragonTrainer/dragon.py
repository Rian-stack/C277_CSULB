import entity

class Dragon(entity.Entity):
    '''
    Dragon Class (dragon.py) – abstract class – inherits from Entity
        1. __init__(self, name, max_hp, num_sp) – call super’s init, then set _special_attacks.
        2. decrement_special_attacks(self) – subtract 1 from _special_attacks. If the value
        becomes negative, then reset it to 0.
        3. basic_attack(self, opponent) – tail attack – the hero takes a random amount of
        damage in the range 3-7. Return a string with the description of the attack and the
        damage dealt to the hero.
        4. __str__(self) – use super to get the __str__ from the entity class, then concatenate on
        the number of special attacks remaining.
    '''
    def __init__(self, name, max_hp, num_sp):
        return 0
    
    def decrement_special_attacks(self):
        return 0
    
    def basic_attack(self, opponent):
        return 0
    
    def __str__(self):
        return 0