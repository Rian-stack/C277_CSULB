#Name: Sena Matsuzoe, Rianne Papa
#Date: 09/09/2024
#Description: Hangman Game

from dictionary import words
import random
import check_input


def display_gallows(num_incorrect):
  if num_incorrect == 0:
    print('========\n||/  |\n||\n||\n||\n||\n')
  elif num_incorrect == 1:
    print('========\n||/  |\n||   o\n||\n||\n||\n')
  elif num_incorrect == 2:
    print('========\n||/  |\n||   o\n||   |\n||\n||\n')
  elif num_incorrect == 3:
    print('========\n||/  |\n||   o\n||  /|\n||\n||\n')
  elif num_incorrect == 4:
    print('========\n||/  |\n||   o\n||  /|\\\n||\n||\n')
  elif num_incorrect == 5:
    print('========\n||/  |\n||   o\n||  /|\\\n||  /\n||\n')
  elif num_incorrect == 6:
    print('========\n||/  |\n||   o\n||  /|\\\n||  / \\\n||\n')
  return 0


def display_letters(letters):
  #prints letters in non-list format
  print(" ".join(letters))
  return 0


def get_letters_remaining(incorrect, correct):
  remaining_letters = [
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  ]

  guessed = incorrect + correct

  #removes letters from remaining_letters list
  for letter in guessed:
    if letter in remaining_letters:
      remaining_letters.remove(letter)

  return remaining_letters


def main():
  while True:
    print('-Hangman-')
    #get random word from list
    correct_word = (random.choice(words))
    #convert String to List of letters
    correct_word_list = list(correct_word)
    remaining_letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    display_letters(remaining_letters)

    correct_guesses = 0
    incorrect_guesses = 0
    correct_guess_list = []
    incorrect_guess_list = []
    guessed_word = ['_' for _ in correct_word_list]

    while correct_guesses != 5:
      if incorrect_guesses == 6:
        print("Game Over! \n The correct word was " + correct_word)
        break

      userInput = input("Guess a letter: ").upper()

      #output for duplicate guesses
      if userInput in incorrect_guess_list or userInput in correct_guess_list:
        print("You already guessed that letter.")

      elif userInput in correct_word_list:
        #constructs correct guesses list
        print('Correct !!')
        correct_guess_list.append(userInput)
        display_gallows(incorrect_guesses)

        #replace '_' with correct letter
        for position, letter in enumerate(correct_word_list):
          if letter == userInput:
            guessed_word[position] = userInput
            correct_guesses += 1
        display_letters(guessed_word)

      else:
        #constructs incorrect guesses list
        print('Incorrect !!')
        incorrect_guesses += 1
        incorrect_guess_list.append(userInput)

      #displays remaining letters and gallows
      display_gallows(incorrect_guesses)
      remaining_letters = get_letters_remaining(incorrect_guess_list,
                                                correct_guess_list)
      print("Remaining letters:")
      display_letters(remaining_letters)

    #Game Loop
    if correct_guesses == 5:
      print('You win !!')
    else:
      print('You lose !!')
    print('Incorrect selections:')
    display_letters(incorrect_guess_list)
    play_again = check_input.get_yes_no('Play Again (Y/N)?')
    if play_again == False:
      print("Thanks for playing! Goodbye.")
      break


main()
