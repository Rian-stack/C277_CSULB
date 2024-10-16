import vehicle
import random

class Car(vehicle.Vehicle):
    """
    Represents a car in the race, inheriting from the Vehicle class.

    The car has a special Nitro Boost move that increases its speed by 1.5 times.
    """

    def __init__(self):
        """Initialize a new Car instance with predefined attributes."""
        super().__init__("Lightning Car", 'C', 6, 8)

    def description_string(self):
        """
        Provide a description of the car.

        Returns:
            str: A description of the car, including its name, speed range, and special move.
        """
        return f"Car: {self._name} - A fast car ({self._min_speed}-{self._max_speed} units). Special: Nitro Boost (1.5x speed)"

    def special_move(self, dist):
        """
        Move the car with a special Nitro Boost action if there is sufficient energy.

        Args:
            dist (int): The distance to the next obstacle.

        Returns:
            str: A description of the movement or the reason for not moving.
        """
        if self._energy >= 15:
            self._energy -= 15
            movement = int(1.5 * random.randint(self._min_speed, self._max_speed))
            if movement >= dist:
                # Car crashes into the obstacle
                self._position += (dist - 1)
                return f"({self._name}) crashes into an obstacle and stops at {self._position} units!"
            else:
                # Car moves normally
                self._position += movement
                return f"({self._name}) boosts forward and moves {movement} units!"
        else:
            return f"({self._name}) does not have enough energy to boost!"
