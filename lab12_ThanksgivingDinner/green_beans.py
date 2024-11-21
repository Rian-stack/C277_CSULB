import plate_decorator

class GreenBeans(plate_decorator.PlateDecorator):
  """
  extended plate decorator class represent Green beans
  """
  def __init__(self, p):
    self._plate = p
  def description(self):
    return super().description() + "+ GreenBeans "
  def area(self):
    return super().area() - 20

  def weight(self):
    return super().weight() - 3

  def count(self):
    return super().count() + 1