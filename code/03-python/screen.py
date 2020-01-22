# Standard modules
from types import FunctionType

class Screen:
  def __init__(self,
               raw_lines:        'list - Of strings, lists of strings, functions, or a mix of all',
               screen_id:        'str - A manually-set unique id for any logic',
               refresh_interval: 'int - How often the screen should update dynamic values, in seconds'=3):
    self.lines = []
    for l in raw_lines:
      l_object = self.create_line_object(l)
      self.lines.append(l_object)

    self.id = screen_id
    self.refresh_interval = refresh_interval

  def create_line_object(self,
                         l: 'str OR list OR FunctionType - Raw info for static or dynamic line content'):
    values = ['']
    function = None
    if (isinstance(l, list)):
      values = l
    elif (isinstance(l, str)):
      values = [l]
    elif (type(l) == FunctionType):
      function = l

    return Line(values, function, 0)

  def advance_line_value_index(self,
                               li:  'int - Line index in lines list',
                               dir: 'int - "1" goes forward and "-1" goes backward'):
    n = self.lines[li].value_index
    if (dir == 1):
      if (n >= len(self.lines[li].values) - 1):
        n = 0
      else:
        n += 1
    elif (dir == -1):
      if (n <= 0):
          n = len(self.lines[li].values) - 1
      else:
          n -= 1
    self.lines[li].value_index = n

  def update_line_values(self,
                        line: 'Line - Line object, obviously'):
    if (line.function != None):

      old_values = line.values
      new_values = line.function()
      # A hack to make sure the new value is in the correct format (i.e. a list of string(s)).
      new_values = self.create_line_object(new_values).values

      has_changed = False
      if (type(old_values) != list):
        has_changed = True
      if (len(old_values) != len(new_values)):
        has_changed = True
      for i in range(0, len(new_values)):
        if old_values[i] != new_values[i]:
          has_changed = True
          break

      if has_changed:
        line.values = new_values

# Shouldn't really be a class (https://www.youtube.com/watch?v=o9pEzgHorH0).
# Ideally, a dict would suffice.
class Line:
  def __init__(self,
               values:      'list - Of string(s) which are the static content of a line',
               function:    '(Optional) FunctionType - A dynamic source for the list of values above',
               value_index: 'int - Index of current value'):
    self.values = values
    self.function = function
    self.value_index = value_index