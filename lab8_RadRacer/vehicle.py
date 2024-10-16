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

    def get_initial(self):
        """Get the initial of the vehicle."""
        return self._initial

    def set_initial(self, initial):
        """Set the initial of the vehicle."""
        self._initial = initial

    def fast(self, dist=None):
        """
        Move the vehicle quickly, consuming energy.

        Args:
            dist (int, optional): The distance to the next obstacle. If None, move freely.

        Returns:
            str: A description of the movement.
        """
        if self._energy >= 5:
            movement = random.randint(self._min_speed, self._max_speed)
            if dist is not None:
                movement = min(movement, dist - 1)  # Limit movement to just before the obstacle
            self._position += movement
            self._energy -= 5
            if dist is not None and movement == dist - 1:
                return f"({self._name}) quickly moves {movement} units and stops at an obstacle!"
            else:
                return f"({self._name}) quickly moves {movement} units!"
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
