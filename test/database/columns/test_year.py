'''
This module will test the columns.YearColumn class
'''

import unittest
from clubadmin.database.columns import YearColumn
from clubadmin.database.columns import DatabaseValueError

class TestYearColumn(unittest.TestCase):
  def test_check(self):
    dc = YearColumn()
    self.assertFalse(dc._check(1890))
    self.assertFalse(dc._check(3010))
    self.assertTrue(dc._check(1970))

  def test_table(self):
    class TestTable:
      yearfld = YearColumn()
    tt = TestTable()

    with self.assertRaises(DatabaseValueError):
      tt.yearfld = b'1980'

    with self.assertRaises(DatabaseValueError):
      tt.yearfld = 198

    # Using the underlying datetime.strptime method will raise a ValueError if there is any
    # following "garbage" in the value being converted.
    with self.assertRaises(ValueError):
      tt.yearfld = '1980-2-5@13:30'

    with self.assertRaises(ValueError):
      tt.yearfld = '1980-'

    tt.yearfld = '1980'
    self.assertEqual(tt.yearfld, 1980)

    tt.yearfld = 1980
    self.assertEqual(tt.yearfld, 1980)
