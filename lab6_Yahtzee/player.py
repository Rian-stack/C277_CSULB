import die
  
class Player:
  """
  A class representing a player in the Yahtzee game.

  Attributes:
      _dice (list of Die): A list containing three Die objects, each representing a die rolled by the player.
      _points (int): The player's total score.
  """

  def __init__(self):
      """
      Initializes the Player object by creating three Die objects,
      sorting them in ascending order, and setting the player's points to 0.
      """
      self._dice = [die.Die(), die.Die(), die.Die()] 
      self._points = 0
      self._dice.sort()

  def get_points(self):
      """
      Returns the player's current total score.
      Returns:
          int: The player's current score.
      """
      return self._points

  def roll_dice(self):
      """
      Rolls all three dice for the player and sorts them in ascending order.
      This simulates a player's turn in the game.
      """
      for d in self._dice:
          d.roll()
      self._dice.sort()

  def has_pair(self):
      """
      Checks if the player has a pair (two dice with the same value).
      If a pair is found, increments the player's points by 1.
      Returns:
          bool: True if a pair is found, False otherwise.
      """
      if self._dice[0] == self._dice[1] or self._dice[1] == self._dice[2]:
          self._points += 1
          return True
      return False

  def has_three_of_a_kind(self):
      """
      Checks if the player has three of a kind (all three dice have the same value).
      If three of a kind is found, increments the player's points by 3.
      Returns:
          bool: True if three of a kind is found, False otherwise.
      """
      if self._dice[0] == self._dice[1] == self._dice[2]:
          self._points += 3
          return True
      return False

  def has_series(self):
      """
      Checks if the player has a series (three consecutive dice values, e.g., 1-2-3).
      If a series is found, increments the player's points by 2.
      Returns:
          bool: True if a series is found, False otherwise.
      """
      if self._dice[2] - self._dice[1] == 1 and self._dice[1] - self._dice[0] == 1:
          self._points += 2
          return True
      return False

  def __str__(self):
      """
      Returns a string representation of the player's dice values.
      Returns:
          str: A string in the format "D1=value, D2=value, D3=value".
      """
      return f"D1={self._dice[0]} D2={self._dice[1]} D3={self._dice[2]}"
