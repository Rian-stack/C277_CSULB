import door
import random

class ComboDoor(door.Door):
    """A door with a combination lock."""

    def __init__(self):
        """Initializes the ComboDoor with a random solution and sets input to None."""
        self.solution = random.randint(1, self.get_menu_max())
        self.input = None

    def examine_door(self):
        """Returns a description of the door."""
        return "A door with a combination lock. You can spin the dial to a number 1-10"

    def menu_options(self):
        """Returns the menu options for the door."""
        return "Enter #1-10: "

    def get_menu_max(self):
        """Returns the maximum menu option."""
        return 10

    def attempt(self, option):
        """Sets the user's input and returns a message."""
        if 1 <= option <= self.get_menu_max():
            self.input = option
            return f"You entered: {option}"
        else:
            return "Invalid input. Please enter a number between 1 and 10."

    def is_unlocked(self):
        """Checks if the door is unlocked."""
        return self.input == self.solution

    def clue(self):
        """Returns a clue if the door is not unlocked."""
        if not self.is_unlocked() and self.input is not None:
            if self.input < self.solution:
                return "Too low"
            elif self.input > self.solution:
                return "Too high"

    def success(self):
        """Returns a success or failure message."""
        if self.is_unlocked():
            return "You successfully unlocked the combo door!!"
        else:
            return "The door remains locked."
