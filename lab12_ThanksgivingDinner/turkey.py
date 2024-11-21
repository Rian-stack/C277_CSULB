import plate_decorator

class Turkey(plate_decorator.PlateDecorator):
  """
  extended plate decorator class represent turkey
  """
  def __init__(self, p):
    self._plate = p

  def description(self):
    return super().description() + "+ Turkey "
  
  def area(self):
    return super().area() - 15

  def weight(self):
    return super().weight() - 4

  def count(self):
    return super().count() + 1