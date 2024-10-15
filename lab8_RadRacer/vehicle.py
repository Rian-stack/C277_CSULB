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
    '''
    An abstract base class representing a vehicle.

    Attributes:
        _name (str): vehicle's name
        _initial (str): vehicle's initial
        _min_speed (int): minimum value of speed range
        _max_speed (int): maximum value of speed range
        _position (int): the vehicle's current location on the track
        _energy (int): vehicle's power level
    '''

    def __init__(self, name, initial, min_speed, max_speed):
        '''
        Initialize a new Vehicle instance.

        Args:
            name (str): The name of the vehicle.
            initial (str): The initial of the vehicle.
            min_speed (int): The minimum speed of the vehicle.
            max_speed (int): The maximum speed of the vehicle.
        '''
        self._name = name
        self._initial = initial
        self._min_speed = min_speed
        self._max_speed = max_speed
        self._position = 0
        self._energy = 100

    def move(self):
        '''
        Move the vehicle a random distance within its speed range.

        Returns:
            int: The distance moved.
        '''
        distance = random.randint(self._min_speed, self._max_speed)
        self._position += distance
        self._energy -= 1
        return distance

    def get_position(self):
        '''
        Get the current position of the vehicle.

        Returns:
            int: The current position.
        '''
        return self._position

    def get_energy(self):
        '''
        Get the current energy level of the vehicle.

        Returns:
            int: The current energy level.
        '''
        return self._energy

    @abc.abstractmethod
    def description_string(self):
        '''
        Return a string description of the vehicle.

        This method should be implemented by subclasses.

        Returns:
            str: A description of the vehicle.
        '''
        pass

    @abc.abstractmethod
    def special_move(self):
        '''
        Perform a special move unique to the vehicle type.

        This method should be implemented by subclasses.

        Returns:
            str: A description of the special move performed.
        '''
        pass
