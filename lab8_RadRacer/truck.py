import vehicle

class Truck(vehicle.Vehicle):
    def __init__(self, name, initial, min_speed, max_speed):
        super().__init__(name, initial, min_speed, max_speed)

    def special_move(self, dist):
        """
        Move the truck with a special ram action if there is sufficient energy.

        Args:
            dist (int): The distance to the next obstacle.

        Returns:
            str: A description of the movement.
        """
        if self._energy >= 15:
            # Deduct energy and calculate the distance moved
            self._energy -= 15
            movement = 2 * random.randint(self._min_speed, self._max_speed)
            self._position += movement
            return f"({self._name}) rams through the obstacle and moves {movement} units!"
        else:
            return f"({self._name}) does not have enough energy to ram through the obstacle!"
    
    def description_string(self):
        return f"Truck: {self._name} - A powerful truck ({self._min_speed}-{self._max_speed} units). Special: Heavy Load (2x distance when moving)"
