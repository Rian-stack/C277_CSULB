""" Puppy Simulator

Written by: Sena Matsuzoe, Rianne Papa
Date: 12/11/2024

A puppy simulator program with two basic functions, feed or play with the puppy. The puppy will react
differently depending on its current state: eating, playing, or asleep.
"""

import check_input
import puppy

def main():
    """
    Main function to interact with the virtual puppy.
    
    This function creates a Puppy object and displays a menu to the user.
    The user can choose to feed the puppy, play with the puppy, or quit the program.
    The puppy's reactions are displayed based on the user's choices.
    """
    print("Congratulations on your new puppy!")
    my_puppy = puppy.Puppy("Buddy")  # Create a Puppy object with a name
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")
        
        choice = check_input.get_int_range("Enter choice: ", 1, 3)
        
        if choice == 1:
            print(my_puppy.give_food())
        elif choice == 2:
            print(my_puppy.throw_ball())
        elif choice == 3:
            print("Goodbye!")
            break

main()