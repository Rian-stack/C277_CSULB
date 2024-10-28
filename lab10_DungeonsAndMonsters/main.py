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

def main():
    print()
if __name__ == "__main__":
    main()