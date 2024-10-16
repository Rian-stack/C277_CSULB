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
    """
    Abstract base class for all vehicles in the race.

    Attributes:
        _name (str): The name of the vehicle.
        _initial (str): The initial letter representing the vehicle on the track.
        _min_speed (int): The minimum speed of the vehicle.
        _max_speed (int): The maximum speed of the vehicle.
        _position (int): The current position of the vehicle on the track.
        _energy (int): The current energy level of the vehicle.
    """

    def __init__(self, name, initial, min_speed, max_speed):
        self._name = name
        self._initial = initial
        self._min_speed = min_speed
        self._max_speed = max_speed
        self._position = 0
        self._energy = 100

    def fast(self, dist):
        """
        Move the vehicle quickly, consuming energy.

        Args:
            dist (int): The distance to the next obstacle.

        Returns:
            str: A description of the movement.
        """
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
        """
        Move the vehicle slowly, without consuming energy.

        Args:
            dist (int): The distance to the next obstacle.

        Returns:
            str: A description of the movement.
        """
        movement = min(self._min_speed // 2, dist)
        self._position += movement
        return f"({self._name}) slowly moves {movement} units!"

    @abc.abstractmethod
    def special_move(self):
        """
        Execute the vehicle's special move.

        This method should be implemented by subclasses.

        Returns:
            int: The distance moved by the special move.
        """
        pass

    @abc.abstractmethod
    def description(self):
        """
        Provide a description of the vehicle.

        This method should be implemented by subclasses.

        Returns:
            str: A description of the vehicle.
        """
        pass

    def get_position(self):
        """Get the current position of the vehicle."""
        return self._position

    def get_energy(self):
        """Get the current energy level of the vehicle."""
        return self._energy

    def __str__(self):
        return f"{self._name} [Position - {self._position}, Energy - {self._energy}]"
