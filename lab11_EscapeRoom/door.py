import abc

class Door(abc.ABC):
    '''
    Door (door.py) – interface – these methods should be overridden in each of the subclasses.
        1. examine_door(self) – returns a string description of the door.
        2. menu_options(self) – returns a string with the menu options that user can choose from
        when attempting to unlock the door.
        3. get_menu_max(self) – returns the number of options in the above menu for check input.
        4. attempt(self, option) – passes in the user’s menu selection. Use this value to update the
        input attribute. Return a string describing the user’s attempt.
        5. is_unlocked(self) – checks to see if the door was unlocked by comparing the input
        attribute with the solution. Returns true if it is unlocked, false otherwise.
        6. clue(self) – returns a hint for the user if their attempt was unsuccessful.
        7. success(self) – returns a congratulatory message if the user attempt was successful.
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