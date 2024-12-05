#Name: Sena Matsuzoe, Rianne Papa
#Date: 12/3/2024
#Lab 13 - Task List – Part 2
'''
Description:  Maintains task list for user. The user should be able to view the current task, view all tasks, mark the current task complete, postpone the current task, or to add a new task, serach tasks by date. Task_list(tasklist.Tasklist) will read the list from a file (‘tasklist.txt’) when the program begins and then store the updated list by overwriting the old contents when the user quits the program.
'''
import tasklist
import check_input

def main_menu(tasklist_obj):
  '''
  Displays the main menu and returns the user’s valid input.

  Returns: 
    int: The user's menu choice between 1-5
  '''
  print("\n-Tasklist-")
  print(f"You have {len(tasklist_obj)} tasks")
  print("1. Display all tasks")
  print("2. Display current task")
  print("3. Add new task")
  print("4. Mark current task complete")
  print("5. Postpone current task")
  print("6. Search tasks by date")
  print("7. Save and quit")
  choice = check_input.get_int_range("Enter choice: ", 1, 7)
  return int(choice)


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
  task_list = tasklist.Tasklist()

  while True:
    choice = main_menu(task_list)
    if choice == 1: #Case print all tasks
      print("Tasks to complete:")
      task_number = 1
      #traverse elements of tasklist using loop to print all tasks
      for n in task_list:
        print(f"{task_number}. {n}")
        task_number += 1
    elif choice == 2: # Case print only current task
      if len(task_list) == 0:  # CASE List is empty
        print('All tasks are complete')
      else:
        print(task_list.get_current_task())

    elif choice == 3:# Case add new task to tasklist
      new_desc = input('Enter a task: ')
      new_date = get_date()
      new_time = get_time()
      task_list.add_task(new_desc, new_date, new_time)

    elif choice == 4: # CASE mark current task comp
      if len(task_list) == 0:  # CASE List is empty
        print('All tasks are complete')
      elif len(task_list) == 1:  # CASE List has 1 task
        print("Marking current task as complete:\n", task_list.mark_complete())
        print("All tasks are complete")
      else: # Case list has least 2 tasks
        print("Marking current task as complete:\n", task_list.mark_complete())
        print("New current task:\n", task_list.get_current_task())

    elif choice == 5: #Postpone task
      if len(task_list) == 0:  # CASE List is empty
        print("All tasks are complete")
      else:
        print("Postponing task:\n", task_list.get_current_task())
        #prompt the user to enter a new date and time
        print('Enter a new due date: ')
        new_date = get_date()
        new_time = get_time()
        task_list.postpone_task(new_date, new_time)

    elif choice == 6:# Search tasks by date
      print("Search by Date:")
      search_date = get_date()
      task_number = 1
      #Traverse every element of tasklist to search task that has same date which user input
      for n in task_list:
        if n.date == search_date:
          print(f"{task_number}. {n}")
          task_number += 1
      if task_number == 1: # CASE No task found
        print("No tasks found")

    elif choice == 7: #Save and quit
      task_list.save_file()
      print('Saving and exiting.')
      break


main()
