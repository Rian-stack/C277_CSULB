import vehicle
import random

class Motorcycle(vehicle.Vehicle):
    """
    Represents a motorcycle in the race, inheriting from the Vehicle class.

    The motorcycle has a special Wheelie move that doubles its speed but has a chance of crashing.
    It also has a unique slow movement that allows it to go around obstacles.
    """

    def __init__(self):
        """Initialize a new Motorcycle instance with predefined attributes."""
        super().__init__("Swift Bike", 'M', 6, 8)

    def slow(self, dist):
        """
        Move the motorcycle slowly at 75% speed, without consuming energy.

        Args:
            dist (int or None): The distance to the next obstacle. If None, allow moving past finish line.

        Returns:
            str: A description of the movement.
        """
        movement = int(0.75 * self._min_speed)
        if dist is not None:
            movement = min(movement, dist)
        self._position += movement
        return f"({self._name}) moves slowly and travels {movement} units!"

    def description_string(self):
        """
        Provide a description of the motorcycle.

        Returns:
            str: A description of the motorcycle, including its name, speed range, and special move.
        """
        return f"Motorcycle: {self._name} - A speedy motorcycle ({self._min_speed}-{self._max_speed} units). Special: Wheelie (2x speed but there's a chance you'll crash)"

    def special_move(self, dist):
        """
        Move the motorcycle with a special Wheelie action if there is sufficient energy.

        Args:
            dist (int or None): The distance to the next obstacle. If None, allow moving past finish line.

        Returns:
            str: A description of the movement or the reason for not moving.
        """
        if self._energy >= 15:
            self._energy -= 15
            # 75% chance to move at 2x speed
            if random.random() < 0.75:
                movement = 2 * random.randint(self._min_speed, self._max_speed)
                if dist is not None:
                    if movement >= dist:
                        self._position += (dist - 1)
                        return f"({self._name}) crashes into an obstacle and stops at {self._position} units!"
                    else:
                        self._position += movement
                else:
                    # No obstacle, motorcycle moves normally
                    self._position += movement
                return f"({self._name}) performs a wheelie and moves {movement} units!"
            else:
                # Motorcycle fails to speed and moves 1 unit
                self._position += 1
                return f"({self._name}) fails the wheelie and only moves 1 unit!"
        else:
            return f"({self._name}) does not have enough energy to perform a wheelie!"
