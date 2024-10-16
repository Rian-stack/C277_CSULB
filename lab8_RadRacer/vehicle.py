import abc
import random

class Vehicle(abc.ABC):
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
        if self._energy >= 5:
            movement = random.randint(self._min_speed, self._max_speed)
            if movement < dist:
                self._position += movement
                self._energy -= 5
                return f"({self._name}) quickly moves {movement} units!"
            else:
                self._position += dist
                self._energy -= 5
                return f"({self._name}) crashes into obstacle at {dist} units!"
        else:
            return f"({self._name}) does not have enough energy to move quickly!"
    
    def slow(self, dist):
        movement = min(self._min_speed // 2, dist)
        self._position += movement
        return f"({self._name}) slowly moves {movement} units!"

    def __str__(self):
        return f"{self._name} - Position: {self._position}, Energy: {self._energy}"
    
    @abc.abstractmethod
    def description_string(self):
        pass

    @abc.abstractmethod
    def special_move(self, dist):
        pass
import abc
import random

class Vehicle(abc.ABC):
    def __init__(self, name, initial, min_speed, max_speed):
        self._name = name
        self._initial = initial
        self._min_speed = min_speed
        self._max_speed = max_speed
        self._position = 0
        self._energy = 100

    def fast(self, dist):
        if self._energy >= 5:
            movement = random.randint(self._min_speed, self._max_speed)
            if movement < dist:
                self._position += movement
                self._energy -= 5
                return f"({self._name}) quickly moves {movement} units!"
            else:
                self._position += dist - 1
                self._energy -= 5
                return f"({self._name}) crashes into obstacle at {dist} units!"
        else:
            return f"({self._name}) does not have enough energy to move quickly!"
    
    def slow(self, dist):
        movement = min(self._min_speed // 2, dist)
        self._position += movement
        return f"({self._name}) slowly moves {movement} units!"

    @abc.abstractmethod
    def special_move(self):
        pass

    def get_position(self):
        return self._position

    def get_energy(self):
        return self._energy

    def __str__(self):
        return f"{self._name} [Position - {self._position}, Energy - {self._energy}]"
