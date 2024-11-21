import plate_decorator
class Stuffing(plate_decorator.PlateDecorator):
  """
  extended plate decorator class represent stuffing
  """
  def __init__(self, p):
    self._plate = p

  def description(self):
    return super().description() + "+ Stuffing "
  
  def area(self):
    return super().area() - 18

  def weight(self):
    return super().weight() - 7

  def count(self):
    return super().count() + 1