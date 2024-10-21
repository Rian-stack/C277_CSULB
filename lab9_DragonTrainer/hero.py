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
        import random
        damage = random.randint(1, 6) + random.randint(1, 6) 
        opponent.take_damage(damage)
        return f"{self.get_name()} attacks with a SWORD SLASH for {damage} damage."
    
    def special_attack(self, opponent):
        import random
        damage = random.randint(1, 12)
        opponent.take_damage(damage)
        return f"{self.get_name()} attacks with a FIREBALL for {damage} damage."
