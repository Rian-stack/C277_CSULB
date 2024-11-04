import door
import random

class Locked_Door(door.Door):
    '''
    A locked door. Look for a key in 3 different locations
    '''
    def __init__(self):
        self._solution = random.randint(1,3)
        self._input = None

    def menu_options(self):
        return "1. Look under the mat.\n2. Look under the flower pot.\n 3. Look under the fake rock."
    
    def get_menu_max(self):
        return 3
    
    def attempt(self, option):
        '''Update _input attr'''
        self._input = option
        if option == 1:
            return "You look under the mat."
        elif option == 2:
            return "You look under the flower pot."
        elif option == 3:
            return "You looked under the fake rock."
        
    def is_unlocked(self):
        return self._input == self._solution
    
    def clue(self):
        return "Look somewhere else."
    
    def success(self):
        return "Congratulations, you opened the door." 