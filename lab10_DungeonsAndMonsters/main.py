'''
    Main – prompt the user to enter their name, then construct the hero and a map object.
    Create a loop that repeats until the hero dies, the hero finds the finish, or the user quits the
    game. Present a menu that allows the user to choose a direction to move in (north, south,
    east, west), move the hero in that direction, reveal that spot, and then present the
    encounter at that location as follows:
        a. ‘m’ – monster – construct an enemy and display its information. Create a loop
        that allows the user to either attack or run away. If they attack, the hero attacks
        the monster, and if the monster has hp left, then the monster attacks back. If the
        monster is dead, then display a message and remove the ‘m’ from the map. If the
        user chooses to run away, then choose a random direction to run in (reveal but
        don’t present the encounter for the new location) (‘m’ should remain on the map).
        b. ‘o’ – invalid direction – display a message stating that they cannot move that
        direction.
        c. ‘n’ – nothing – display a message stating that this room is empty.
        d. ‘s’ – start – display a message that they wound up back at the start of the dungeon.
        e. ‘i' – item room – display a message stating that they found a health potion. Heal
        the hero and remove the ‘i' from the map so they can’t get it again (not required,
        but you can add a check to see if the hero has full hp, if they do, then you can
        leave the ‘i' on the map to save it for later).
        f. ‘f’ – finish – display a congratulatory message stating that they found the way out
        of the maze and won the game.
'''
import random
import hero
import map
import enemy
import check_input

def main():
    user_name = input("What is your name, traveler? ")
    game_map = map.Map()
    player = hero.Hero(user_name, game_map)
    monster = enemy.Enemy()

    #Game Loop
    while player._hp > 0:
        print(f"\n{player._name}")
        print(f"HP: {player}")
        for row in game_map.show_map((player._row, player._col)):
            print(row)
        
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")

        choice = check_input.get_int_range("Enter your choice: ", 1, 5)

        if choice == 1:
            move_result = player.go_north()
        elif choice == 2:
            move_result = player.go_south()
        elif choice == 3:
            move_result = player.go_east()
        elif choice == 4:
            move_result = player.go_west()
        elif choice == 5:
            print("Quitting the game.")
            break

        #handles invalid direction
        if move_result == 'o':
            print("You cannot move in that direction.")

        #other encounters
        else:
            game_map.reveal((player._row, player._col))
            location = game_map[player._row][player._col]

            #monster encounter
            if location == 'm':
                print(f"You encountered a {monster._name}!")

                #monster minigame loop
                while monster._hp > 0 and player._hp > 0:
                    print(f"1. Attack {monster._name}")
                    print("2. Run Away")
                    action = check_input.get_int_range("Enter choice: ", 1, 2)

                    if action == '1':
                        print(player.attack(monster))
                        if monster._hp > 0:
                            print(monster.attack(player))
                        if monster._hp <= 0:
                            print(f"You have slain a {monster._name}")
                            game_map.remove_at_loc((player._row, player._col))
                        elif player._hp <= 0:
                            break

                    elif action == '2':
                        directions = ['n', 's', 'e', 'w']
                        random.shuffle(directions)
                        directions = ['n', 's', 'e', 'w']
                        random.shuffle(directions)
                        for direction in directions:
                            if direction == 'n' and player.go_north() != 'o':
                                break
                            elif direction == 's' and player.go_south() != 'o':
                                break
                            elif direction == 'e' and player.go_east() != 'o':
                                break
                            elif direction == 'w' and player.go_west() != 'o':
                                break
                        print("You ran away!")
                        break

            #item encounter
            elif location == 'i':
                print("You found a Health Potion! You drink it to restore your health.")
                player.heal()
                game_map.remove_at_loc((player._row, player._col))

            #starting position
            elif location == 's':
                print("You are back at the start of the dungeon.")

            #final position
            elif location == 'f':
                print("Congratulations! You found the exit and won the game!")
                break

            #empty room or 'n'
            else:
                print("This room is empty.")

    if player._hp <= 0:
        print("You have been defeated. Game Over!")

if __name__ == "__main__":
    main()
