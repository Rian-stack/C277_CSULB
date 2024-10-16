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
        """
        Initialize a new Vehicle instance.

        Args:
            name (str): The name of the vehicle.
            initial (str): The initial letter representing the vehicle on the track.
            min_speed (int): The minimum speed of the vehicle.
            max_speed (int): The maximum speed of the vehicle.
        """
        self._name = name
        self._initial = initial
        self._min_speed = min_speed
        self._max_speed = max_speed
        self._position = 0
        self._energy = 100

    @property
    def initial(self):
        """str: The initial letter representing the vehicle on the track."""
        return self._initial

    @initial.setter
    def initial(self, value):
        """Set the initial letter representing the vehicle on the track."""
        self._initial = value

    @property
    def position(self):
        """int: The current position of the vehicle on the track."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the current position of the vehicle on the track."""
        self._position = value

    @property
    def energy(self):
        """int: The current energy level of the vehicle."""
        return self._energy

    @energy.setter
    def energy(self, value):
        """Set the current energy level of the vehicle."""
        self._energy = value

    def fast(self, dist):
        """
        Move the vehicle quickly, consuming 5 energy.

        Args:
            dist (int): The distance to the next obstacle.

        Returns:
            str: A description of the movement.
        """
        if self.energy >= 5:
            movement = random.randint(self._min_speed, self._max_speed)
            if dist is not None:
                movement = min(movement, dist - 1)  # Limit movement to just before the obstacle
            self.position += movement
            self.energy -= 5
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
        self.position += movement
        return f"({self._name}) slowly moves {movement} units!"
    
    def __str__(self):
        """
        Return a string representation of the vehicle.

        Returns:
            str: A string containing the vehicle's name, position, and energy.
        """
        return f"{self._name} [Position - {self.position}, Energy - {self.energy}]"

    @abc.abstractmethod
    def special_move(self, dist):
        """
        Execute the vehicle's special move.

        This method should be implemented by subclasses.

        Args:
            dist (int): The distance to the next obstacle.

        Returns:
            str: A description of the special move's outcome.
        """
        pass

    @abc.abstractmethod
    def description_string(self):
        """
        Provide a description of the vehicle.

        This method should be implemented by subclasses.

        Returns:
            str: A description of the vehicle.
        """
        pass
