import random

class Die:
  """
  A class representing a die.

  Attributes:
      _sides (int): The number of sides on the die (default is 6).
      _value (int): The current value of the rolled die.
  """

  def __init__(self, sides=6):
      """
      Initializes the Die object with a specified number of sides.
      Rolls the die upon initialization to set its initial value.
      Args:
          sides (int): The number of sides on the die (default is 6).
      """
      self._sides = sides
      self._value = self.roll()

  def roll(self):
      """
      Rolls the die, generating a random value between 1 and the number of sides.
      Returns:
          int: The new value of the die after rolling.
      """
      self._value = random.randint(1, self._sides)
      return self._value

  def __str__(self):
      """
      Returns a string representation of the die's value.
      Returns:
          str: The string representation of the current die value.
      """
      return str(self._value)

  def __lt__(self, other):
      """
      Compares if the value of this die is less than the value of another die.
      Args:
          other (Die): The other die to compare against.
      Returns:
          bool: True if this die's value is less than the other die's value, False otherwise.
      """
      return self._value < other._value

  def __eq__(self, other):
      """
      Checks if the value of this die is equal to the value of another die.
      Args:
          other (Die): The other die to compare against.
      Returns:
          bool: True if both dice have the same value, False otherwise.
      """
      return self._value == other._value

  def __sub__(self, other):
      """
      Subtracts the value of another die from this die's value.
      Args:
          other (Die): The other die whose value will be subtracted.

      Returns:
          int: The difference between this die's value and the other die's value.
      """
      return self._value - other._value
