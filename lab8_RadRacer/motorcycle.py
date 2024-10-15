import vehicle

class Motorcycle(vehicle.Vehicle):
    """
    A subclass of Vehicle representing a Motorcycle.

    Attributes:
        Inherits all attributes from Vehicle class.
        _lean_angle (int): The current lean angle of the motorcycle.
    """

    def __init__(self, name, initial, min_speed, max_speed):
        """
        Initialize a new Motorcycle instance.

        Args:
            name (str): The name of the motorcycle.
            initial (str): The initial of the motorcycle.
            min_speed (int): The minimum speed of the motorcycle.
            max_speed (int): The maximum speed of the motorcycle.
        """
        super().__init__(name, initial, min_speed, max_speed)
        self._lean_angle = 0

    def description_string(self):
        """
        Return a string description of the motorcycle.

        Returns:
            str: A description of the motorcycle including its name and lean angle.
        """
        return f"{self._name} (Motorcycle) - Lean Angle: {self._lean_angle}"

    def special_move(self):
        """
        Perform a special move (extreme lean).

        Returns:
            str: A description of the special move.
        """
        extreme_lean = 45  # Maximum lean angle
        self.lean(extreme_lean)
        return f"{self._name} performed an extreme lean at {extreme_lean} degrees!"

    def lean(self, angle):
        """
        Set the lean angle of the motorcycle.

        Args:
            angle (int): The angle to lean, between -45 and 45 degrees.
        """
        if -45 <= angle <= 45:
            self._lean_angle = angle
            print(f"Leaning at {self._lean_angle} degrees.")
        else:
            print("Error: Lean angle must be between -45 and 45 degrees.")

    def get_lean_angle(self):
        """
        Get the current lean angle.

        Returns:
            int: The current lean angle.
        """
        return self._lean_angle

    def move(self):
        """
        Override the move method to account for lean angle.

        Returns:
            int: The distance moved.
        """
        base_move = super().move()
        lean_bonus = abs(self._lean_angle) // 15  # Every 15 degrees of lean adds 1 to movement
        actual_move = base_move + lean_bonus
        print(f"Moved {actual_move} units. Lean bonus: {lean_bonus}")
        return actual_move
