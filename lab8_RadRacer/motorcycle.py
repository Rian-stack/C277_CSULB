import vehicle
import random

class Motorcycle(vehicle.Vehicle):
    def __init__(self):
        super().__init__("Swift Bike", 'M', 6, 8)

    def slow(self, dist):
        """
        Move the motorcycle slowly at 75% speed, without consuming energy.

        Args:
            dist (int): The distance to the next obstacle.

        Returns:
            str: A description of the movement.
        """
        movement = min(int(0.75 * self._min_speed), dist)
        self._position += movement
        return f"({self._name}) goes around the obstacle and moves {movement} units!"

    def description(self):
        return f"Motorcycle: {self._name} - A speedy motorcycle ({self._min_speed}-{self._max_speed} units). Special: Agile Maneuvering (75% speed)"

    def special_move(self, dist):
        """
        Move the motorcycle with a special boost action if there is sufficient energy.

        Args:
            dist (int): The distance to the next obstacle.

        Returns:
            str: A description of the movement.
        """
        if self._energy >= 15:
            self._energy -= 15
            # 75% chance to move at 2x speed
            if random.random() < 0.75:
                movement = 2 * random.randint(self._min_speed, self._max_speed)
                if movement >= dist:
                    # Motorcycle crashes into the obstacle
                    self._position += (dist - 1)
                    return f"({self._name}) crashes into an obstacle and stops at {self._position} units!"
                else:
                    # Motorcycle moves normally
                    self._position += movement
                    return f"({self._name}) speeds forward and moves {movement} units!"
            else:
                # Motorcycle fails to speed and moves 1 unit
                self._position += 1
                return f"({self._name}) failed to speed up and only moves 1 unit!"
        else:
            return f"({self._name}) does not have enough energy to speed up!"
