import vehicle

class Car(vehicle.Vehicle):
    """
    A subclass of Vehicle representing a Car.

    Attributes:
        Inherits all attributes from Vehicle class.
        _nitro (int): The amount of nitro boost available.
    """

    def __init__(self, name, initial, min_speed, max_speed):
        """
        Initialize a new Car instance.

        Args:
            name (str): The name of the car.
            initial (str): The initial of the car.
            min_speed (int): The minimum speed of the car.
            max_speed (int): The maximum speed of the car.
        """
        super().__init__(name, initial, min_speed, max_speed)
        self._nitro = 3  # Start with 3 nitro boosts

    def description_string(self):
        """
        Return a string description of the car.

        Returns:
            str: A description of the car including its name and nitro amount.
        """
        return f"{self._name} (Car) - Nitro: {self._nitro}"

    def special_move(self):
        """
        Perform a special move (use nitro).

        Returns:
            str: A description of the special move.
        """
        if self.use_nitro():
            return f"{self._name} used nitro boost!"
        else:
            return f"{self._name} tried to use nitro, but none left!"

    def use_nitro(self):
        """
        Use a nitro boost if available.

        Returns:
            bool: True if nitro was used, False if no nitro available.
        """
        if self._nitro > 0:
            self._nitro -= 1
            print(f"Nitro boost used! Remaining nitro: {self._nitro}")
            return True
        else:
            print("No nitro boost available!")
            return False

    def get_nitro(self):
        """
        Get the current amount of nitro.

        Returns:
            int: The current amount of nitro.
        """
        return self._nitro

    def move(self):
        """
        Override the move method to account for nitro boost.

        Returns:
            int: The distance moved.
        """
        base_move = super().move()
        if self.use_nitro():
            nitro_boost = 3  # Nitro gives a boost of 3 units
            actual_move = base_move + nitro_boost
            print(f"Moved {actual_move} units. Nitro boost: {nitro_boost}")
        else:
            actual_move = base_move
            print(f"Moved {actual_move} units.")
        return actual_move
