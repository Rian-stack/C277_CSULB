import vehicle

class Truck(vehicle.Vehicle):
    """
    A subclass of Vehicle representing a Truck.

    Attributes:
        Inherits all attributes from Vehicle class.
        _cargo (int): The current cargo load of the truck.
    """

    def __init__(self, name, initial, min_speed, max_speed):
        """
        Initialize a new Truck instance.

        Args:
            name (str): The name of the truck.
            initial (str): The initial of the truck.
            min_speed (int): The minimum speed of the truck.
            max_speed (int): The maximum speed of the truck.
        """
        super().__init__(name, initial, min_speed, max_speed)
        self._cargo = 0

    def load_cargo(self, amount):
        """
        Load cargo onto the truck.

        Args:
            amount (int): The amount of cargo to load.
        """
        self._cargo += amount
        print(f"Loaded {amount} units of cargo. Total cargo: {self._cargo}")

    def unload_cargo(self, amount):
        """
        Unload cargo from the truck.

        Args:
            amount (int): The amount of cargo to unload.
        """
        if amount > self._cargo:
            print(f"Error: Not enough cargo. Current cargo: {self._cargo}")
        else:
            self._cargo -= amount
            print(f"Unloaded {amount} units of cargo. Remaining cargo: {self._cargo}")

    def get_cargo(self):
        """
        Get the current cargo amount.

        Returns:
            int: The current amount of cargo.
        """
        return self._cargo

    def move(self):
        """
        Override the move method to account for cargo weight.

        Returns:
            int: The distance moved.
        """
        base_move = super().move()
        cargo_penalty = self._cargo // 10  # Every 10 units of cargo reduces movement by 1
        actual_move = max(base_move - cargo_penalty, 0)
        print(f"Moved {actual_move} units. Cargo penalty: {cargo_penalty}")
        return actual_move
