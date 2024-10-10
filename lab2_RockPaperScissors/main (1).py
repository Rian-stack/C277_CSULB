#Name: Sena Matsuzoe, Rianne Papa
#Date: 09/04/2024
#Description: Rock Paper Scissors Game

import check_input
import random

# Store string for User weapon, and Computer weapon
player = ''
comp = ''

def weapon_menu():
  choice = input("Choose your weapon:\n R. Rock \n P. Paper \n S. Scissors \n B. Back\n")
  if choice == "R":
    print("You picked Rock")
    return "R"
  if choice == "P":
    print("You picked Paper")
    return "P"
  if choice == "S":
    print("You picked Scissors")
    return "S"
  if choice == "B":
    return "B"
  else:
    print("Invalid input")
    weapon_menu()
  return (0)

def comp_weapon():
  comp_choice = random.randint(1,3)
  if comp_choice == 1:
    print("Computer picked Rock")
    return "R"
  if comp_choice == 2:
    print("Computer picked Paper")
    return "P"
  if comp_choice == 3:
    print("Computer picked Scissors")
    return "S"
  return (0)
  

def find_winner(player, comp):
  #return value 0 = tie, 1 = player, 2 = computer
  #player input == rock
  if player == "R" and comp == "R":
    print("Tie")
    return (0)
  if player == "R" and comp == "P":
    print("Computer wins")
    return (2)
  if player == "R" and comp == "S":
    print("Player wins")
    return (1)
  #player input == paper
  if player == "P" and comp == "R":
    print("Player wins")
    return (1)
  if player == "P" and comp == "P":
    print("Tie")
    return (0)
  if player == "P" and comp == "S":
    print("Computer wins")
    return (2)
  #player input == scissors
  if player == "S" and comp == "R":
    print("Computer wins")
    return (2)
  if player == "S" and comp == "P":
    print("Player wins")
    return (1)
  if player == "S" and comp == "S":
    print("Tie")
    return (0)

def display_scores(player_score, comp_score):
  print("Player = ", player_score, "Computer = ", comp_score)

def main():
  # Store integer for score count
  player_score = 0
  comp_score = 0
  result = 0
  user_input = 0
  while user_input != 3:
    print("RPS Menu:\n 1. Play Game \n 2. Show Score \n 3. Quit")
    #Wait User input, 1 or 2 or 3; 
    user_input = check_input.get_int_range('', 1, 3)
  
    if user_input == 1: # case 1: play game
      player = weapon_menu()
      comp = comp_weapon()
      result = find_winner(player,comp)
      if result == 1:
        player_score += 1
      if result == 2:
        comp_score += 1
      if result == 0:
        pass
    
    if user_input == 2: # case 2: show score
      display_scores(player_score, comp_score)
    
    if user_input == 3: # case 3: quit
      print("Final Score:")
      display_scores(player_score, comp_score)

main()
