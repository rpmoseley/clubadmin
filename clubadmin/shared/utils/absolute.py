'''
This module provides the absolute range of values for the various parts of the ClubAdmin
package in order to provide a means of modifying them if required.
'''

class AbsCheckError(ValueError):
  '''Exception raised if a check fails and errors are to be issued'''
  def __init__(self, inst, value):
    self._inst, self._value = inst, value
  
  def __str__(self):
    return 'Value {0._value} is outside {0._inst._min}..{0._inst._max}'.format(self)

class AbsRange:
  '''Class providing methods to force a range of integers'''
  def __init__(self, min_, max_, error=False):
    if not isinstance(min_, int) or not isinstance(max_, int):
      raise ValueError("Must provide 'int' instances for min_ and max_")
    if min_ < 0:
      raise ValueError("Must provide a positive integer above 0 for 'min_'")
    if max_ < 1:
      raise ValueError("Must provide a positive integer above 1 for 'max_'")
    if max_ <= min_:
      raise ValueError("Must provide 'min_' and 'max_' with a difference of at least 1")
    self._min, self._max, self._error = min_, max_, error

  @property
  def Min(self):
    '''Return the minimum end of the valid range'''
    return self._min

  @property
  def Max(self):
    '''Return the maximum end of the valid range'''
    return self._max

  def Check(self, value):
    '''Check that the value correctly resides within the current range,
       raise an exception if the range is set to issue an error'''
    if not isinstance(value, int):
      if self._error:
        raise ValueError("Must provide an 'int' instance for the value to check")
      return False
    if self._min <= value <= self._max:
      return True
    if self._error:
      raise AbsCheckError(self, value)
    return False
 
class AbsSettingsBase:
  '''Class providing shared functionality for the absolute settings'''
  pass
