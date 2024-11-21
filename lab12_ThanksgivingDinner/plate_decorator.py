import abc
import plate

class PlateDecorator(plate.Plate, abc.ABC):
    """
    An abstract base class representing a Plate Decorator.

    Attributes:
        _plate (plate.Plate): The plate object being decorated. This can be a Small or Large plate.
    """

    def __init__(self, p):
        """
        Initialize a PlateDecorator object.

        Args:
            p (plate.Plate): The plate object to decorate.
        """
        self._plate = p

    def description(self):
        """
        Get the description of the plate.

        Returns:
            str: The description of the plate.
        """
        return self._plate.description()
  
    def area(self):
        """
        Get the remaining area of the plate.

        Returns:
            float: The remaining area of the plate in square inches.
        """
        return self._plate.area()

    def weight(self):
        """
        Get the remaining weight capacity of the plate.

        Returns:
            float: The remaining weight capacity of the plate in ounces.
        """
        return self._plate.weight()
    
    def count(self):
        """
        Get the number of food items currently on the plate.

        Returns:
            int: The number of food items on the plate.
        """
        return self._plate.count()
