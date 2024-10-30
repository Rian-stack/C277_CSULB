import door
import random

class Basic_Door(door.Door):
    '''
    A basic door. You either push or pull
    '''
    def __init__(self):
        solution = random.randint(1,2)
        self._solution = solution

    def examine_door(self):
        return super().examine_door()
