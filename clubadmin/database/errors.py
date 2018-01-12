'''
This module provides all the exceptions that can be raised by the database sub-package
'''

class DatabaseError(ValueError):
  '''Base class for all other exceptions'''

class DatabaseChangedError(DatabaseError):
  '''Exception raised when a column already marked as changed is changed again'''
  def __init__(self, owner, field):
    super().__init__()
    self._owner = owner
    self._field = field

  def __str__(self):
    return "Column {0._field} is marked as changed previously".format(self)

class DatabaseValueError(DatabaseError):
  def __init__(self, owner, field, value):
    super().__init__()
    self._owner = owner
    self._field = field
    self._value = value

  def __str__(self):
    return "Column {0._field} has an invalid value {0._value}".format(self)

class DatabaseConvertError(DatabaseError):
  def __init__(self, owner, field, value, oldvalue):
    super().__init__()
    self._owner = owner
    self._field = field
    self._value = value
    self._oldvalue = oldvalue

  def __str__(self):
    oldfmt = '' if self._value is None else ' to {0._value}'
    retfmt = 'Column {0._field} has failed conversion from {0._oldvalue}' + oldfmt
    return retfmt.format(self)
