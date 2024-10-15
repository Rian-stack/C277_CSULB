import abc
import random

class Vehicle:
    '''
    Attributes:
        _name – vehicle’s name, 
        _initial – vehicle’s initial, 
        _min_speed – minimum value of speed range, 
        _max_speed – maximum value of speed range, 
        _position – the vehicle’s current location on the track, 
        _energy – vehicle’s power level.

    '''
    def __init__(self, name, initial, min_speed, max_speed):
        self._name = name
        self._initial = initial
        self._min_speed = min_speed
        self._max_speed = max_speed

    def fast(self, dist):
        #temp
        energy = 100
        movement = 0
        position = 0
        if energy >= 5:
            movement += random.randint
        movement < self.dist:
            position += movement
        
        return "(Vehicle) quickly moves " + dist +  " units!"
    
    def slow(self, dist):
        return "(Vehicle) slowly moves " + dist +  " units!"

    def __str__(self):
        return self.name + self.position + self.energy
    
    #abstract methods
    def description_string(self):
        return self.description

    def special_move(self, dist):
        return self.dist 

    
    
    
        
        