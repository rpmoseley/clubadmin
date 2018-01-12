'''
This module will test the columns.MemIDColumn class
'''

import unittest
from .mock_MemIDColumn import MemIDColumn
from clubadmin.database.columns import DatabaseValueError

class TestMemIDColumn(unittest.TestCase):
  def test_check(self):
    mid = MemIDColumn()
    self.assertTrue(mid._check(None))
    self.assertTrue(mid._check(1))
    self.assertFalse(mid._check(-1))

  def test_table(self):
    class TestTable:
      memidfld = MemIDColumn()
    tt = TestTable()

    with self.assertRaises(DatabaseValueError):
      tt.memidfld = -1

    tt.memidfld = None
    self.assertIsNot(tt.memidfld, None)
