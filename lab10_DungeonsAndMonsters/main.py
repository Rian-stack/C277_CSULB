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
from hero import Hero
from map import Map
from enemy import Enemy

def main():
    name = input("Enter your hero's name: ")
    hero = Hero(name)
    game_map = Map()

    while hero._hp > 0:
        print(game_map.show_map((hero._row, hero._col)))
        print(hero)
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            move_result = hero.go_north()
        elif choice == '2':
            move_result = hero.go_south()
        elif choice == '3':
            move_result = hero.go_east()
        elif choice == '4':
            move_result = hero.go_west()
        elif choice == '5':
            print("Quitting the game.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if move_result == 'o':
            print("You cannot move in that direction.")
        else:
            game_map.reveal((hero._row, hero._col))
            location = game_map[hero._row][hero._col]

            if location == 'm':
                enemy = Enemy()
                print(f"You encountered a {enemy._name}!")

                while enemy._hp > 0 and hero._hp > 0:
                    print(enemy)
                    action = input("Do you want to attack (a) or run away (r)? ")

                    if action == 'a':
                        print(hero.attack(enemy))
                        if enemy._hp > 0:
                            print(enemy.attack(hero))
                        else:
                            print(f"You defeated the {enemy._name}!")
                            game_map.remove_at_loc((hero._row, hero._col))
                    elif action == 'r':
                        directions = ['n', 's', 'e', 'w']
                        random.shuffle(directions)
                        for direction in directions:
                            if direction == 'n' and hero.go_north() != 'o':
                                hero._row -= 1
                                break
                            elif direction == 's' and hero.go_south() != 'o':
                                hero._row += 1
                                break
                            elif direction == 'e' and hero.go_east() != 'o':
                                hero._col += 1
                                break
                            elif direction == 'w' and hero.go_west() != 'o':
                                hero._col -= 1
                                break
                        print("You ran away!")
                        game_map.reveal((hero._row, hero._col))
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif location == 'i':
                print("You found a health potion!")
                hero.heal()
                game_map.remove_at_loc((hero._row, hero._col))
            elif location == 'f':
                print("Congratulations! You found the exit and won the game!")
                break
            else:
                print("This room is empty.")

    if hero._hp <= 0:
        print("You have been defeated. Game Over!")
if __name__ == "__main__":
    main()
