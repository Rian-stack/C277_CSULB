from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, name, initial, min_speed, max_speed):
        super().__init__(name, initial, min_speed, max_speed)

    def special_move(self):
        distance = self._max_speed * 2
        self._position += distance
        return distance, True  # Return distance and True for smashing obstacles

    def description(self):
        return f"Truck: {self._name} - A heavy truck ({self._min_speed}-{self._max_speed} units). Special: Ram (2x speed and it smashes through obstacles)."
