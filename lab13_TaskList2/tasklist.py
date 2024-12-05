import task

class Tasklist(task.Task):
  """
  Attributes:
  _task (task.Task)– list of task type object
  _n (int)– count of iterater
  
  """

  def __init__(self):
    """
    initialize _task and _n. then open file to read tasks and store all tasks in tasklist, _task.
    """
    self._task = []
    self._n = 0
    file = open('tasklist.txt', 'r')  #opens file only for reading
    for line in file:
      desc, date, time = line.strip().split(',')
      self._task.append(task.Task(desc, date, time))
    file.close()
    self._task.sort()

  def add_task(self, desc, date, time):
    """
    add new task in tasklist
    Args:
      desc (str)– string description of the task.
      date (str)– due date of the task. A string in the format: MM/DD/YYYY
      time (str)– time the task is due. A string in the format: HH:MM
    """
    self._task.append(task.Task(desc, date, time))
    self._task.sort()

  def get_current_task(self):
    """
    return current task
    Return: task[0](task.Task)
    """
    self._task.sort()
    return self._task[0]
  
  def mark_complete(self):
    """
    mark current task completed. return deleated task
    Return: temp(task.Task)
    """
    temp = self._task[0]
    self._task.pop(0)
    return temp
  
  def postpone_task(self, date, time):
    """
    postpone current task with date and time that user input.

    Argument:
      date (str)– due date of the task. A string in the format: MM/DD/YYYY
      time (str)– time the task is due. A string in the format: HH:MM
    """
    desc = self._task[0].description
    self._task.pop(0)
    self._task.append(task.Task(desc, date, time))
    self._task.sort()

  def save_file(self):
    """
    Save all task in tasklist in text file 'tasklist.txt' 
    """
    file = open('tasklist.txt', 'w')  #opens file only for writing
    for new_task in self._task:
      file.write(repr(new_task) + '\n')
    file.close()

  def __len__(self):
    """
    override len() function. return length of task list
    Return: len(self._task) (int)
    """
    return len(self._task)
  
  def __iter__(self):
    """
    override __iter__ function to traverse elements of tasklist. initialize _n, then return self
    """
    self._n = 0
    return self
  
  def __next__(self):
    """
     return the next item in the sequence.
    """
    if self._n < len(self):
        task = self._task[self._n]
        self._n += 1
        return task
    else:
        raise StopIteration