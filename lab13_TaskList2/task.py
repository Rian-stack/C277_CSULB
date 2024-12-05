class Task:
  '''
  Attributes:
      description (str)– string description of the task.
      date (str)– due date of the task. A string in the format: MM/DD/YYYY
      time (str)– time the task is due. A string in the format: HH:MM
  '''

  def __init__(self, desc, date, time):
      self.description = desc
      self.date = date
      self.time = time

  def get_description(self):
      return self.description

  def __str__(self):
      return self.description + '- Due: ' + self.date + ' at ' + self.time

  def __repr__(self):
      return self.description + ',' + self.date + ',' + self.time

  def __lt__(self, other):
      #Convert
      self_descript, self_date, self_time = self.__repr__().split(',')
      other_descript, other_date, other_time = other.__repr__().split(',')

      self_month, self_day, self_year = map(int, self_date.split('/'))
      other_month, other_day, other_year = map(int, other_date.split('/'))
      #Compare by Year, Month,day
      if self_year != other_year:
          return self_year < other_year

      if self_month != other_month:
          return self_month < other_month

      if self_day != other_day:
          return self_day < other_day
      #Compare by Time
      self_hour, self_minute = map(int, self_time.split(':'))
      other_hour, other_minute = map(int, other_time.split(':'))
      if self_hour != other_hour:
          return self_hour < other_hour
      if self_minute != other_minute:
          return self_minute < other_minute
      #Compare by Description
      return self_descript < other_descript
