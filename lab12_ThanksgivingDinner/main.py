""" Thanksgiving Dinner

Written by: Sena Matsuzoe, Rianne Papa
Date: 11/20/2024

A game that has the user add food to their plate without going
over the weight or area limit of a paper plate.
"""

import small_plate
import large_plate
import turkey
import green_beans
import potatoes
import stuffing
import pie
import check_input

def examine_plate(plate):
  """
  Examines the plate and displays its description.
  Provides hints based on remaining space and weight.
  Returns True if the plate has failed, otherwise False.
  """
  print('\n' + plate.description())
  remaining_area = plate.area()
  remaining_weight = plate.weight()

  # Hints for weight
  if remaining_weight <= 0 or remaining_area <= 0:
    print("Your plate isn't big enough for this much food! Your food spills over the edge.")
    return True
  elif remaining_weight <= 6:
    sturdiness = "Bending"
  elif remaining_weight <= 12:
    sturdiness = "Weak"
  else:
    sturdiness = "Strong"

  # Hints for area
  if remaining_area <= 20:
      space_hint = "A tiny bit"
  elif remaining_area <= 40:
      space_hint = "Some"
  else:
      space_hint = "Plenty"
  
  print("Sturdiness: " + sturdiness)
  print("Space available: " + space_hint)
  return False

def main():
  # Menu
  print("- Thanksgiving Dinner -")
  print("Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!")

  # Plate Options
  print("Choose a plate:")
  print("1. Small Sturdy Plate")
  print("2. Large Flimsy Plate")

  plate_choice = check_input.get_int_range('Enter Your Choice: ', 1, 2)
  if plate_choice == 1:
    plate = small_plate.SmallPlate()  
  elif plate_choice == 2:
    plate = large_plate.LargePlate() 

  # Food Options
  while True:
    print("\nChoose a food item to add:")
    print("1. Turkey")
    print("2. Stuffing")
    print("3. Potatoes")
    print("4. Green Beans")
    print("5. Pie")
    print("6. Quit")

    choice = check_input.get_int_range("Enter your choice (1-6): ", 1, 6)
    if choice == 6:
        break

    if choice == 1:
        plate = turkey.Turkey(plate)
    elif choice == 2:
        plate = stuffing.Stuffing(plate)
    elif choice == 3:
        plate = potatoes.Potatoes(plate)
    elif choice == 4:
        plate = green_beans.GreenBeans(plate)
    elif choice == 5:
        plate = pie.Pie(plate)

    # Examine plate after adding food
    if examine_plate(plate):
        return  # Exit if plate fails

  # Display plate contents and remaining space
  print("\nYour final plate:")
  print(plate.description())
  print(f"Number of items: {plate.count()}")
  print(f"Remaining area: {plate.area()} square inches")
  print(f"Remaining weight: {plate.weight()} ounces")
  print("Happy Thanksgiving!")

main()

