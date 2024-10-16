from vehicle import Vehicle
import random

class Motorcycle(Vehicle):
    def __init__(self, name, initial, min_speed, max_speed):
        super().__init__(name, initial, min_speed, max_speed)

    def special_move(self):
        if random.random() < 0.7:  # 70% chance of successful wheelie
            distance = self.fast() * 2
            self._position += distance
            return distance
        else:
            return 0  # Crash, no movement
