import plate_decorator

class Turkey(plate_decorator.PlateDecorator):
    """
    An extended PlateDecorator class representing Turkey.
    """

    def __init__(self, p):
        """
        Initialize a Turkey object.

        Args:
            p (Plate): The plate object to decorate.
        """
        self._plate = p

    def description(self):
        """
        Get the description of the plate with Turkey added.

        Returns:
            str: The updated description of the plate.
        """
        return super().description() + "+ Turkey "
  
    def area(self):
        """
        Get the remaining area of the plate after adding Turkey.

        Returns:
            float: The updated remaining area of the plate in square inches.
        """
        return super().area() - 15

    def weight(self):
        """
        Get the remaining weight capacity of the plate after adding Turkey.

        Returns:
            float: The updated remaining weight capacity of the plate in ounces.
        """
        return super().weight() - 4

    def count(self):
        """
        Get the updated number of food items on the plate after adding Turkey.

        Returns:
            int: The updated count of food items on the plate.
        """
        return super().count() + 1
