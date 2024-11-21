import plate_decorator

class Potatoes(plate_decorator.PlateDecorator):
    """
    An extended PlateDecorator class representing Potatoes.

    This class decorates a Plate object by adding Potatoes to it.
    It modifies the description, area, weight, and count properties of the Plate
    to account for the addition of Potatoes.
    """

    def __init__(self, p):
        """
        Initialize a Potatoes object.

        Args:
            p (Plate): The plate object to decorate.
        """
        self._plate = p

    def description(self):
        """
        Get the description of the plate with Potatoes added.

        Returns:
            str: The updated description of the plate.
        """
        return super().description() + "+ Potatoes "
  
    def area(self):
        """
        Get the remaining area of the plate after adding Potatoes.

        Returns:
            float: The updated remaining area of the plate in square inches.
        """
        return super().area() - 18

    def weight(self):
        """
        Get the remaining weight capacity of the plate after adding Potatoes.

        Returns:
            float: The updated remaining weight capacity of the plate in ounces.
        """
        return super().weight() - 6

    def count(self):
        """
        Get the updated number of food items on the plate after adding Potatoes.

        Returns:
            int: The updated count of food items on the plate.
        """
        return super().count() + 1
