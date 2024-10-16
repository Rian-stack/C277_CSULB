import vehicle
import random

class Car(vehicle.Vehicle):
    def __init__(self):
        super().__init__("Lightning Car", 'C', 6, 8)

    def description(self):
        return f"Car: {self._name} - A fast car ({self._min_speed}-{self._max_speed} units). Special: Nitro Boost (1.5x speed)"

    def special_move(self):
        """
        Move the car with a special boost action if there is sufficient energy.

        Returns:
            int: The distance moved by the special move.
        """
        if self._energy >= 15:
            self._energy -= 15
            movement = int(1.5 * random.randint(self._min_speed, self._max_speed))
            return movement
        else:
            return 0

