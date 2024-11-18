import abc

class Door(abc.ABC):
    '''
    An abstact base class that represents a door
    '''
    @abc.abstractmethod
    def examine_door(self):
        '''returns str door description'''
        pass

    @abc.abstractmethod
    def menu_options(self):
        '''returns str menu options when attempting to unlock the door'''
        pass

    @abc.abstractmethod
    def get_menu_max(self):
        '''returns the number of options in the menu for check input'''
        pass

    @abc.abstractmethod
    def attempt(self, option):
        '''passes in menu selection used to update input attr. returns str describing attempt'''
        pass

    @abc.abstractmethod
    def is_unlocked(self):
        '''compares input attr with the solution. Returns true if unlocked, else false'''
        pass

    @abc.abstractmethod
    def clue(self):
        '''returns str hint'''
        pass

    @abc.abstractmethod
    def success(self):
        '''returns str congratulatory message'''
        pass