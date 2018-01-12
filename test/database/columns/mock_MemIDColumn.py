'''
This module provides a mock version of the MemIDColumn which avoids the need for a 
proper database table to generate the unique IDs.
'''

from itertools import count
from clubadmin.database.columns import MemIDColumn as orig_MemIDColumn

class MemIDColumn(orig_MemIDColumn):
  id_generator = count(1000)    # Start from 1000 

  def __next__(self):
    # Return the next number from the id_generator class
    return next(self.id_generator)
