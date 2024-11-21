import plate_decorator
class Pie(plate_decorator.PlateDecorator):
  """
  extended plate decorator class represent Pie
  """
  def __init__(self, p):
    self._plate = p
  def description(self):
    return super().description() + "+ Pie "
  def area(self):
    return super().area() - 19

  def weight(self):
    return super().weight() - 8

  def count(self):
    return super().count() + 1