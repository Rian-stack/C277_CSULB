import abc

class DoorFactory(abc.ABC):
  @abc.abstractmethod
  def create_door(self):
    pass
  