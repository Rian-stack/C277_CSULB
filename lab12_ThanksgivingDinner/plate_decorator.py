import abc
import plate
class PlateDecorator(plate.Plate, abc.ABC):
  """
  An abstract base class representing Plate Decorater
  
  Attributes:
      _plate(plate.Plate): type of plate user chose. Small or Large
  """
  def __init__(self, p):
    """initialize _plate"""
    self._plate = p

  def description(self):
    return self._plate.description()
  
  def area(self):
    return self._plate.area()

  def weight(self):
    return self._plate.weight()
    
  def count(self):
    return self._plate.count()