'''
This module will test the columns.BoolColumn class
'''

import unittest
from clubadmin.database.columns import BoolColumn
from clubadmin.database.columns import DatabaseValueError

class TestBoolColumn(unittest.TestCase):
  '''Test that the BoolColumn class correctly operates'''
  def test_table(self):
    class TestTable:
      boolfld = BoolColumn()
    tt = TestTable()
    with self.assertRaises(DatabaseValueError):
      tt.boolfld = 2
    with self.assertRaises(DatabaseValueError):
      tt.boolfld = 'False'
    self.assertEqual(tt.boolfld, False)
    tt.boolfld = True
    self.assertEqual(tt.boolfld, True)
