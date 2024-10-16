from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, name, initial, min_speed, max_speed):
        super().__init__(name, initial, min_speed, max_speed)
        self._nitro = 3

    def special_move(self):
        if self._nitro > 0:
            self._nitro -= 1
            distance = int(self.fast() * 1.5)
            self._position += distance
            return distance
        else:
            return 0

    def __str__(self):
        return f"{super().__str__()} - Nitro: {self._nitro}"
