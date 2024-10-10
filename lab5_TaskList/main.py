#Name: Sena Matsuzoe, Rianne Papa
#Date: 09/25/2024
'''
Description:  Maintains task list for user. The user should be able to view the current task, mark the current task complete, postpone the current task, or to add a new task. The program will read the list from a file (‘tasklist.txt’) when the program begins and then store the updated list by overwriting the old contents when the user quits the program.
'''

import task
import check_input


def main_menu(tasklist):
  '''
  Displays the main menu and returns the user’s valid input.

  Returns: 
    int: The user's menu choice between 1-5
  '''
  print("\n-Tasklist-")
  print(f"You have {len(tasklist)} tasks")
  print("1. Display current task")
  print("2. Mark current task complete")
  print("3. Postpone current task")
  print("4. Add new task")
  print("5. Save and quit")
  choice = check_input.get_int_range("Enter choice: ", 1, 5)
  return int(choice)


def read_file():
  '''
  Reads tasks from 'tasklist.txt' and returns a list of tasks.

  Returns:
    list: A list of tasks created from the file
  '''
  file = open('tasklist.txt', 'r')  #opens file only for reading
  tasklist = []
  for line in file:
    desc, date, time = line.strip().split(',')
    tasklist.append(task.Task(desc, date, time))
  file.close()
  return tasklist


def write_file(tasklist):
  '''
  Write the list of tasks to the file 'tasklist.txt'.

  Returns:
    none
  Args:
    tasklist (list): A list of tasks to be written to the file
  '''
  file = open('tasklist.txt', 'w')  #opens file only for writing
  for new_task in tasklist:
    file.write(repr(new_task) + '\n')
  file.close()


def get_date():
  '''
  Prompts the user to enter the month, day, and year

  Returns:
    str: The date in the format MM/DD/YYYY
  '''
  month = check_input.get_int_range('Enter month (1-12): ', 1, 12)
  day = check_input.get_int_range('Enter day (1-31): ', 1, 31)
  year = check_input.get_int_range('Enter year (2000-2100): ', 2000, 2100)
  return f'{month:02}/{day:02}/{year}'


def get_time():
  '''
  Prompts the user to enter the hour (military time) and minute.

  Returns:
    str: The time in the format HH:MM
  '''
  hour = check_input.get_int_range('Enter hour (0-23): ', 0, 23)
  minute = check_input.get_int_range('Enter minute (0-59): ', 0, 59)
  return f'{hour:02}:{minute:02}'
  
def main():
  '''
  Main function which handles task list operations.
  '''
  tasklist = read_file()
  tasklist.sort()
  while True:
    choice = main_menu(tasklist)

    if choice == 1:
      if len(tasklist) == 0:  # CASE List is empty
        print('All tasks are complete')
      else:
        tasklist.sort()
        print(tasklist[0])

    elif choice == 2:
      if len(tasklist) == 0:  # CASE List is empty
        print('All tasks are complete')
      elif len(tasklist) == 1:  # CASE List has 1 task
        print("Marking current task as complete:\n", tasklist[0])
        tasklist.pop(0)
        print("All tasks are complete")
      else:  # CASE List has 2 or more task
        print("Marking current task as complete:\n", tasklist[0])
        tasklist.pop(0)
        print("New current task:\n", tasklist[0])
        tasklist.sort()

    elif choice == 3:
      if len(tasklist) == 0:  # CASE List is empty
        print("All tasks are complete")
      else:
        print("Postponing task:\n", tasklist[0])
        #prompt the user to enter a new date and time
        print('Enter a new due date: ')
        new_date = get_date()
        new_time = get_time()
        tasklist.append(task.Task(tasklist[0].description, new_date, new_time))
        tasklist.pop(0)
        tasklist.sort()

    elif choice == 4:
      new_desc = input('Enter a task: ')
      new_date = get_date()
      new_time = get_time()
      tasklist.append(task.Task(new_desc, new_date, new_time))
      tasklist.sort()
    elif choice == 5:
      write_file(tasklist)
      print('Saving and exiting.')
      break

main()
