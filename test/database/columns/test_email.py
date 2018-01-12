'''
This module will test the columns.EmailColumn class
'''

import unittest
from clubadmin.database.columns import EmailColumn
from clubadmin.database.columns import DatabaseValueError
from clubadmin.shared.utils import EmailValidator

class TestEmailColumn(unittest.TestCase):
  def test_check(self):
    ef = EmailColumn()
