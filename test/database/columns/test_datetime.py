'''
This module will test the columns.DateTimeColumn class
'''

import unittest
from datetime import datetime
from clubadmin.database.columns import DateTimeColumn
from clubadmin.database.errors import DatabaseConvertError
from clubadmin.database.errors import DatabaseValueError

class TestDateTimeColumn(unittest.TestCase):
  def test_check(self):
    dt = DateTimeColumn()
    self.assertFalse(dt._check(datetime(1890, 1, 15, 12, 30)))
    self.assertFalse(dt._check(datetime(3010, 1, 15, 12, 30)))
    self.assertTrue (dt._check(datetime(1970, 1, 15, 13, 30)))

  def test_table(self):
    chk_datetime = datetime(1980, 2, 5, 12, 30)

    class TestTable:
      timefld = DateTimeColumn()
    tt = TestTable()

    with self.assertRaises(DatabaseValueError):
      tt.timefld = 198002051230

    with self.assertRaises(DatabaseValueError):
      tt.timefld = b'1980-2-5@1230'

    with self.assertRaises(ValueError):
      tt.timefld = '1980-2-5@1230'

    tt.timefld = '1980-2-5@12:30'
    self.assertEqual(tt.timefld, chk_datetime)

    tt.timefld = '1980-02-5@12:30'
    self.assertEqual(tt.timefld, chk_datetime)

    tt.timefld = '1980-2-05@12:30'
    self.assertEqual(tt.timefld, chk_datetime)

    with self.assertRaises(ValueError):
      tt.timefld = '1980-02-30@14:00'

    tt.timefld = '1980-02-05@12:30'
    self.assertEqual(tt.timefld, datetime(1980, 2, 5, 12, 30))
