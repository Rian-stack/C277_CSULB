import check_input
import easy_door_factory
import difficult_door_factory

def open_door(door):
    """Opens a door by presenting the user with options and clues until unlocked.

    Args:
        door: The door object to be opened.
    """
    print("\n" + door.examine_door())
    while True:
        print(door.menu_options())
        choice = check_input.get_int_range("Enter choice: ", 1, door.get_menu_max())
        print(door.attempt(choice))
        if door.is_unlocked():
            print(door.success())
        else:
            print(door.success(), end=" ")

        if door.is_unlocked():
            break
        print(door.clue())

def main():
    """Runs the escape room game."""
    print("Welcome to the Escape Room\nYou must unlock 3 doors to escape...")
    user_choice = check_input.get_int_range("Enter Difficulty (1. Easy 2. Hard): ", 1, 2)
    if user_choice == 1:
        factory = easy_door_factory.EasyDoorFactory()
    else:
        factory = difficult_door_factory.DifficultDoorFactory()

    for _ in range(3):
        open_door(factory.create_door())

    print("Congratulations! You escaped...this time")

main()
