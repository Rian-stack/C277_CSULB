#Name: Bailey Kwok, Rianne Papa, Rafael Papa
#Date: 08/26/2024
#Description: Guessing game between 1-100
import random
import check_input

def main():
  #Generates a random number using the random import
  print("Im thinking of a number between 1-100.")
  ourNum = random.randint(1,100)
  userNum = check_input.get_int_range("Make a guess (1-100):", 1, 100)

  #While loop to keep asking the user for a number until they get it right, count starts at 1 because the first guess is already made
  count = 1
  while userNum != ourNum:
    # checks if user number is higer than the random number
    if userNum > ourNum:           
      print("Too high!")
      userNum = check_input.get_int_range("Make a guess (1-100):", 1, 100)
    # checks if user number is lower than the random number
    elif userNum < ourNum:        
      print("Too low!")
      userNum = check_input.get_int_range("Make a guess (1-100):", 1, 100)
    # add 1 to the count everytime the user guesses
    count += 1                    

  print("Correct! You got it in " + str(count) + " tries.") 

main()