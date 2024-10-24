""" Dragon Trainer

Written by: Sena Matsuzoe, Rianne Papa
Date: 10/23/2024

The program allows the user to play game which player must defeat three dragons to pass trails. This program uses abstract method ,inheritance, mixins to implement all entity class including player, three dragon classes.

"""
import check_input
import fire_dragon
import flying_dragon
import flying_fire_dragon
import hero
import random


def main():
  # Ask user name. create player's entity, list of three defferent type of dragons.
  game_continue = True
  player_result = False
  print("What is your name, challenger?")
  user_name = input()
  player = hero.Hero(user_name, 50)

  print("welcome to dragon training, " + user_name)
  print("You must defeat 3 dragons")

  dragon_list = [
      fire_dragon.FireDragon("Gronkle", 15, 3),
      flying_dragon.FlyingDragon("Timberjack", 10, 3),
      flying_fire_dragon.FlyingFireDragon("Deadly Nadder", 20, 2)
  ]
  # WHILE loop until player, or three dragon defeated
  while game_continue:

    #print Status of player, and three dragons
    print("\n" + str(player))
    for i in range(len(dragon_list)):
      print(str(i + 1) + ". " + str(dragon_list[i]))

    #User chose dragon to attack, and weapon
    player_target = check_input.get_int_range("\nchoose a dragon to attack: ",
                                              1, len(dragon_list))
    player_weapon = check_input.get_int_range(
        "Attack with: \n1. Sword (2 D6) \n2. Arrow (1 D12)\nEnter weapon: ", 1,
        2)

    #Player turn: player attack dragon based on what user input
    if player_weapon == 1:
      print(player.basic_attack(dragon_list[player_target - 1]))
    else:
      print(player.special_attack(dragon_list[player_target - 1]))

    # Check any dragon got defeated, and delete defeated dragon from list. Start checking from last element to first element in dragon_list
    # if list is empty, then end game with player WIN
    remain_dragons = int(len(dragon_list))

    for i in range(remain_dragons):
      if dragon_list[(remain_dragons - 1) - i].hp == 0:
        print(f"//　{dragon_list[(remain_dragons - 1) - i].name} died　//")
        dragon_list.pop((remain_dragons - 1) - i)
    if len(dragon_list) == 0:
      game_continue = False
      player_result = True
      break

    # Dragon turn: Ramdamely chose one dragon who attack player, and weapon
    dragon_who_attack = random.randint(1, len(dragon_list))
    dragon_weapon = random.randint(0, 1)
    if dragon_weapon == 0:
      print(dragon_list[dragon_who_attack - 1].basic_attack(player))
    else:
      print(dragon_list[dragon_who_attack - 1].special_attack(player))

    #Check Player hp, if player lose all hp, then end game with player lose
    if player._hp == 0:
      game_continue = False
      player_result = False
      break

  # print explanation of game result depend on bool (player_result)
  if player_result:
    print(
        "\nCongratulations! You have defeated all three dragons, you have passed the trials."
    )
  else:
    print("\nYOU LOSE ;;")


main()
