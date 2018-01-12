'''
This module will test the columns.IntegerColumn class
'''

import unittest
from clubadmin.database.columns import IntegerColumn
from clubadmin.database.columns import DatabaseValueError

class TestIntegerColumn(unittest.TestCase):
  '''Test that the IntegerColumn class correctly operates'''
  def test_create(self):
    self.assertRaises(TypeError, IntegerColumn, -1)
    self.assertRaises(TypeError, IntegerColumn, maxvalue=-1)

  def test_check(self):
    col = IntegerColumn(maxvalue=5)
    self.assertFalse(col._check(-1))
    self.assertFalse(col._check(6))
    self.assertTrue(col._check(3))

  def test_table(self):
    class TestTable:
      intfld = IntegerColumn()
    tt = TestTable()
    with self.assertRaises(DatabaseValueError):
      tt.intfld = -1
    with self.assertRaises(DatabaseValueError):
      tt.intfld = 900000000
    with self.assertRaises(DatabaseValueError):
      tt.intfld = 1.25
    tt.intfld = False
    self.assertEqual(tt.intfld, 0)  
