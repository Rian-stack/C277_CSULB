import puppy
import check_input

def main():
    print("Congratulations on your new puppy!")
    my_puppy = puppy.Puppy("Buddy")  # Create a Puppy object with a name
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")
        
        choice = check_input.get_int_range("Enter choice: ", 1, 3)
        
        if choice == '1':
            print(my_puppy.give_food())
        elif choice == '2':
            print(my_puppy.throw_ball())
        elif choice == '3':
            print("Goodbye!")
            break

main()