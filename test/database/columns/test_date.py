'''
This module will test the columns.DateColumn class
'''

import unittest
from clubadmin.database.columns import DateColumn
from clubadmin.database.errors import DatabaseConvertError, DatabaseValueError
from datetime import date

class TestDateColumn(unittest.TestCase):
  def test_check(self):
    dc = DateColumn()
    self.assertFalse(dc._check(date(1890, 1, 15)))
    self.assertFalse(dc._check(date(3010, 1, 15)))
    self.assertTrue(dc._check(date(1970, 1, 15)))

  def test_table(self):
    class TestTable:
      datefld = DateColumn()
    tt = TestTable()

    with self.assertRaises(DatabaseValueError):
      tt.datefld = 19800205

    with self.assertRaises(DatabaseValueError):
      tt.datefld = b'1980-2-5'

    with self.assertRaises(ValueError):
      tt.datefld = '198-02-05'

    with self.assertRaises(ValueError):
      tt.datefld = '1980-02-30'

    tt.datefld = None

    tt.datefld = date(1980, 2, 5)
    self.assertIsInstance(tt.datefld, date)
    self.assertEqual(tt.datefld, date(1980, 2, 5))
