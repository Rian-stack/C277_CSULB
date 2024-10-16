from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, name, initial, min_speed, max_speed):
        super().__init__(name, initial, min_speed, max_speed)

    def special_move(self):
        distance = self.fast() * 2
        self._position += distance
        return distance, True  # Return distance and flag for obstacle smashing
