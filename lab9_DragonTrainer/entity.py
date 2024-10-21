import abc

class Entity(abc.ABC):
    '''
    Entity Class (entity.py) – abstract class
        1. __init__(self, name, max_hp) – set the _name, _max_hp, and _hp. Assign the
        max_hp value to both the _max_hp and _hp attributes.
        2. name and hp properties – use decorators to get (not set) the values of _name and _hp.
        3. take_damage(self, dmg) – the damage the entity takes. Subtract the dmg value from
        the entity’s _hp. Do not let the hp go past 0 (if it’s a negative value, reset it to 0).
        4. __str__(self) – return the entity’s name and hp in the format “Name: hp/max_hp”.
        5. Abstract methods basic_attack and special_attack. No code
    '''
    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    
    def take_damage(self, dmg):
        self._hp -= dmg                                                                                                                                                
        if self._hp < 0:                                                                                                                                               
             self._hp = 0     
    
    def __str__(self):
        return f"{self._name}: {self._hp}/{self._max_hp}" 
    
    def get_name(self):                                                                                                                                                
         return self._name                                                                                                                                              
                                                                                                                                                                        
    def is_alive(self):                                                                                                                                                
         return self._hp > 0 
    
