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
    name = input("Enter your hero's name: ")
    game_map = map.Map()
    h = hero.Hero(name, game_map)

    while h._hp > 0:
        print(f"\n{h._name}'s Turn:")
        for row in game_map.show_map((h._row, h._col)):
            print(row)

        print(f"HP: {h}")
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")

        choice = check_input.get_int_range("Enter your choice: ", 1, 5)

        if choice == 1:
            move_result = h.go_north()
        elif choice == 2:
            move_result = h.go_south()
        elif choice == 3:
            move_result = h.go_east()
        elif choice == 4:
            move_result = h.go_west()
        elif choice == 5:
            print("Quitting the game.")
            break

        if move_result == 'o':
            print("You cannot move in that direction.")
        else:
            game_map.reveal((h._row, h._col))
            location = game_map[h._row][h._col]

            if location == 'm':
                e = enemy.Enemy()
                print(f"You encountered a {e._name}!")

                while e._hp > 0 and h._hp > 0:
                    print(f"1. Attack {e._name}")
                    print("2. Run Away")
                    action = input("Enter choice: ")

                    if action == '1':
                        print(h.attack(e))
                        if e._hp > 0:
                            print(e.attack(h))
                        if e._hp <= 0:
                            print(f"You have slain a {e._name}")
                            game_map.remove_at_loc((h._row, h._col))
                        elif h._hp <= 0:
                            break

                    elif action == '2':
                        directions = ['n', 's', 'e', 'w']
                        random.shuffle(directions)
                        directions = ['n', 's', 'e', 'w']
                        random.shuffle(directions)
                        for direction in directions:
                            if direction == 'n' and h.go_north() != 'o':
                                break
                            elif direction == 's' and h.go_south() != 'o':
                                break
                            elif direction == 'e' and h.go_east() != 'o':
                                break
                            elif direction == 'w' and h.go_west() != 'o':
                                break
                        print("You ran away!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif location == 'i':
                print("You found a health potion!")
                h.heal()
                game_map.remove_at_loc((h._row, h._col))
            elif location == 's':
                print("You are back at the start of the dungeon.")
            elif location == 'f':
                print("Congratulations! You found the exit and won the game!")
                break
            else:
                print("This room is empty.")

    if h._hp <= 0:
        print("You have been defeated. Game Over!")
if __name__ == "__main__":
    main()
