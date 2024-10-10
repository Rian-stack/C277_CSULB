import check_input
import player

""" Yahtzee Game

Written by: Sena Matsuzoe, Rianne Papa
Date: 10/02/2024

The program runs a game of Yahtzee. The player is given three dice to roll. The player roll a pair, three of a kind, or a series. The player can then choose to keep the dice or roll again. The game will continue until the player chooses to end the game. The player will be given a score at the end of the game.

Functions:
    take_turn(player) - Rolls the player's dice, checks for win conditions, displays the dice and score.
    main() - Initializes the player, repeatedly calls take_turn, and manages user input for continuing or ending the game.

Usage:
    Run the script to play the Yahtzee game. The program will prompt the player to roll the dice and decide whether to continue or end the game.

"""

def take_turn(player):
  """
  Plays one turn for the given player in the Yahtzee game.
  The function rolls the player's dice, prints the result, checks for 
  any win conditions (three-of-a-kind, pair, or series), and updates 
  and displays the player's score accordingly.
  Args:
      player (Player): The Player object whose turn is being processed.
  Returns:
      None
  """
  player.roll_dice()
  print(player)
  if player.has_three_of_a_kind():
    print("You got 3 of a kind!")
    print("Score = " + str(player.get_points()))
    return
  elif player.has_pair():
    print("You got a pair!")
    print("Score = " + str(player.get_points()))
    return
  elif player.has_series():
    print("You got a series of 3!")
    print("Score = " + str(player.get_points()))
    return
  else:
    print("Aww. Too Bad.")
    print("Score = " + str(player.get_points()))

def main():
  """
  The main function for the Yahtzee game.

  Initializes the player and continuously calls take_turn() until the user decides 
  to end the game. At the end of the game, the final score is displayed.

  The function utilizes the check_input.get_yes_no() method to prompt 
  the player if they want to play again, ensuring proper user input validation.

  Returns:
      None
  """
  print('-yahtzee-\n')
  user = player.Player()
  #Do while loop below
  while True:
    take_turn(user)
    if not check_input.get_yes_no("Play again? (Y/N): "):
      print("Game Over")
      print("Final Score = " + str(user.get_points()))
      break
    print('\n')
    
main()
