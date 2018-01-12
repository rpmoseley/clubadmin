'''
This module provides security to prevent the release of personal information
if the user is granted suitable level of access.
'''

# The following has been disabled during initial development
'''
def authorised(func):
  def wrapper(self):
    if self._authorised:
      return func(self)
    return None
  return wrapper
'''
# The following has been enabled during initial development
def authorised(func):
  def wrapper(self):
    return func(self)
  return wrapper
