from vehicle import Vehicle
import random

class Motorcycle(Vehicle):
    def __init__(self, name, initial, min_speed, max_speed):
        super().__init__(name, initial, min_speed, max_speed)

    def special_move(self):
        if random.random() < 0.7:  # 70% chance of successful wheelie
            distance = self._max_speed * 2
            self._position += distance
            return distance
        else:
            return 0  # Crash, no movement

    def slow(self, dist):
        movement = min(self._min_speed // 4, dist)  # Motorcycles move slower when going slow
        self._position += movement
        return f"({self._name}) slowly moves {movement} units!"

    def description(self):
        return f"Motorcycle: {self._name} - A speedy motorcycle ({self._min_speed}-{self._max_speed} units). Special: Wheelie (2x speed but there's a chance you'll crash)."
