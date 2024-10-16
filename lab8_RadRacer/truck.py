import vehicle
import random

class Truck(vehicle.Vehicle):
    def __init__(self):
        super().__init__("Behemoth Truck", 'T', 4, 8)

    def special_move(self):
        """
        Move the truck with a special ram action if there is sufficient energy.

        Returns:
            int: The distance moved by the special move.
        """
        if self._energy >= 15:
            self._energy -= 15
            movement = 2 * random.randint(self._min_speed, self._max_speed)
            return movement
        else:
            return 0
    
    def description(self):
        return f"Truck: {self._name} - A powerful truck ({self._min_speed}-{self._max_speed} units). Special: Ram (2x speed and it smashes through obstacles)"
