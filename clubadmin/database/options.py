'''
This module provides the support for the Options table, and enables the application
to work with a simple mapping given the option text or number without having to access
the underlying database information directly.
'''

import apsw
from ...config import configdb

# Define the default set of options for the program
_default_options = {
  'gender' : ('Male', 'Female', 'Other'),
  'member' : ('Normal', 'Life', 'New', 'Honourable', 'Banned', 'In-arrears', 'Inactive'),
}

def load_options():
  '''Load the Options table and create a mapping for each of the areas found
     within the table enabling the translation of internal integers into the
     external textual strings that are used by the application'''
  mapping = dict()
  try:
    conn = apsw.connection(configdb.options)
    rowset = conn.cursor().execute('select * from Options')
    print(rowset.getdescription())
    #TODO: Complete this function
  except:
    mapping = _default_options
  return mapping
