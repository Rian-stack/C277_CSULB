import plate_decorator
class Potatoes(plate_decorator.PlateDecorator):
  """
  extended plate decorator class represent potatoes
  """
  def __init__(self, p):
    self._plate = p

  def description(self):
    return super().description() + "+ Potatoes "
  
  def area(self):
    return super().area() - 18

  def weight(self):
    return super().weight() - 6

  def count(self):
    return super().count() + 1