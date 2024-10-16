import vehicle
import random

class Truck(vehicle.Vehicle):
    def __init__(self):
        super().__init__("Behemoth Truck", 'T', 4, 8)

    def description_string(self):
        return f"Truck: {self._name} - A powerful truck ({self._min_speed}-{self._max_speed} units). Special: Ram (2x speed and it smashes through obstacles)"
    
    def special_move(self, dist):
        """
        Move the truck with a special ram action if there is sufficient energy.

        Args:
            dist (int): The distance to the next obstacle (ignored for truck's special move).

        Returns:
            str: A description of the event that occurred.
        """
        if self._energy >= 15:
            self._energy -= 15
            movement = 2 * random.randint(self._min_speed, self._max_speed)
            self._position += movement
            return f"({self._name}) uses ram and travels {movement} units, ignoring all obstacles!"
        else:
            return f"({self._name}) does not have enough energy to use ram!"
    
    
