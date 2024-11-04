import door
import random

class Combo_Door(door.Door):
    '''
    A door with a combination lock. You can spin the dial to a number 1-10.
    '''

    def __init__(self):
        self._solution = random.randint(1, 10)
        self._input = None

    def examine_door(self):
        return "A door with a combination lock. You can spin the dial to a number 1-10."

    def menu_options(self):
        return "Enter # 1-10:"

    def get_menu_max(self):
        return 10

    def attempt(self, option):
        self._input = option
        if option == self._solution:
            return ""  # Add success message here
        elif option < self._solution:
            return "Too low."
        else:
            return "Too high."

    def is_unlocked(self):
        return self._input == self._solution

    def clue(self):
        if self._input < self._solution:
            return "Too low."
        else:
            return "Too high."

    def success(self):
        return "You opened the combination lock!"
