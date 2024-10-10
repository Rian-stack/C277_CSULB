#Name: Sena Matsuzoe, Rianne Papa
#Date: 09/16/2024
#Description: Treasure Hunter. Player will be given a blank map starting from the top left corner. The player will be able to move around the map by typing in the direction they want to go. The objective is to find all 7 treasures without hitting a trap. 

def read_map():
  file = open("map.txt", "r")
  content = file.read()
  file.close()

  content = content.replace("\n", " ")
  Mylist = content.split()

  list2D_map = [[" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "]]
  for i in range(0, 7): 
    for j in range(0, 7):
      list2D_map[i][j] = Mylist[i * 7 + j]

  return list2D_map

def display_map(map, player):
  for i in range(0, 7):
    for j in range(0, 7):
      if player[0] == i and player[1] == j:
        print("P", end=" ")
      else:
        print(map[i][j], end=" ")
    print(" ")

def move_player(player, dir, upper_bound):
  row, col = player
  if (dir == 'W' or dir == "w") and row > 0:
    player[0] -= 1  # Move up
  elif (dir == 'A' or dir == "a") and col > 0:
    player[1] -= 1  # Move left
  elif (dir == 'S' or dir == 's') and row < upper_bound - 1:
    player[0] += 1  # Move down
  elif (dir == 'D' or dir == 'd') and col < upper_bound - 1:
    player[1] += 1  # Move right
  elif dir == 'l' or dir == 'L':
    return player
  else:
    print("You can't move in that direction!")
  return player

def count_treasures_traps(map, player, upper_bound):
  row, col = player
  treasures = 0
  traps = 0

  #iterates a 3x3 area around the player
  for i in range(max(0, row - 1), min(upper_bound, row + 2)):
    for j in range(max(0, col - 1), min(upper_bound, col + 2)):
      if map[i][j] == 'T' or map[i][j] == 'P':
        treasures += 1
      elif map[i][j] == 'X':
        traps += 1

  return treasures, traps

def main():
  treasure_count = 0

  #Game explaination
  print("Treasure Hunt!" + "\n" +
        "Find the 7 treasure without getting caught in a trap." + "\n" +
        "look around to spot nearby traps and treasures.")
  #Create 2d list of Player Map
  list2D_player_map = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "]]

  for i in range(0, 7):
    for j in range(0, 7):
      list2D_player_map[i][j] = "."

  list2D_Treasure_map = read_map()

  #create list for the user that stores location
  list1D_player_location = [0, 0]

  #Game Loop
  game_continue = True
  while game_continue:

    display_map(list2D_player_map, list1D_player_location)
    #chack user input below
    valid = False
    user_input = " "
    while not valid:
      user_input = input(
          "Enter Direction (WASD or L to Look around or Q to quit): ").upper()
      if user_input == "W" or user_input == "S" or user_input == "A" or user_input == "D":
        if user_input != "L" and user_input != "l":
          break
      elif user_input == "Q" or user_input == "q":  #Case user opt quit
        print("Case :(Q) quit" + "\n" + "Goodbye!")
        return 0
      elif user_input == "L" or user_input == "l":
        print("Case Look around (L)")
        treasures, traps = count_treasures_traps(list2D_Treasure_map,
                                                 list1D_player_location,
                                                 len(list2D_player_map))
        print('You detect ' + str(treasures) + ' treasures nearby' + '\n' +
              'You detect ' + str(traps) + ' traps nearby')
        display_map(list2D_player_map, list1D_player_location)
      else:
        print("Invalid input.")
        display_map(list2D_player_map, list1D_player_location)
        continue

    list1D_player_location = move_player(list1D_player_location, user_input, 7)
    #chack user Found treasure or Trap
    if list2D_Treasure_map[list1D_player_location[0]][
        list1D_player_location[1]] == "T":
      list2D_Treasure_map[list1D_player_location[0]][
          list1D_player_location[1]] = "P"
      print("you found treasure! ")
      treasure_count += 1
      print("There are", str(7 - treasure_count), "treasures remaining.")
      #mapping curent location to T (found treasure)
      list2D_player_map[list1D_player_location[0]][
          list1D_player_location[1]] = "T"
      if treasure_count == 7:
        print("You found all the treasures! You win!")
        return 0
    elif list2D_Treasure_map[list1D_player_location[0]][
        list1D_player_location[1]] == "X":
      print("You were caught in a trap!")
      #Game Over
      print("you found", str(treasure_count), "treasures.")
      print("Game Over!")
      game_continue = False
    else:
      list2D_player_map[list1D_player_location[0]][
          list1D_player_location[1]] = "1"

main()
