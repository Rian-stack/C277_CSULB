import abc

class Plate(abc.ABC):
    @abc.abstractmethod
    def description(self):
        '''returns a string description of the plate and what is on it.'''
        pass

    @abc.abstractmethod
    def area(self):
        '''returns the remaining square inches of the plate can hold.'''
        pass

    @abc.abstractmethod
    def weight(self):
        '''returns the remaining number of ounces the plate can hold.'''
        pass

    @abc.abstractmethod
    def count(self):
        '''returns the number of food items the plate is currently holding.'''
        pass