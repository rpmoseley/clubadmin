'''
This module provides the unit test for the TextColumn within the database.columns module
'''

import unittest
from clubadmin.database.columns import TextColumn
from clubadmin.database.errors import DatabaseValueError, DatabaseConvertError

class TestTextColumn(unittest.TestCase):
  def test_check(self):
    tc = TextColumn(10)
    self.assertFalse(tc._check(None))
    self.assertFalse(tc._check('0123456789ABCDEF'))
    self.assertTrue(tc._check('012345'))

  def test_table_illegal_1(self):
    with self.assertRaises(TypeError):
      class TestTable:
        textfld = TextColumn(-1)

  def test_table_illegal_2(self):
    with self.assertRaises(TypeError):
      class TestTable:
        textfld = TextColumn('10')

  def test_table_illegal_3(self):
    with self.assertRaises(TypeError):
      class TestTable:
        textfld = TextColumn(3.14)

  def test_table(self):
    class TestTable:
      textfld = TextColumn(10)
    tt = TestTable()

    with self.assertRaises(DatabaseValueError):
      tt.textfld = '0123456789ABCDEF'

    tt.textfld = '0123456789'
    self.assertEqual(tt.textfld, '0123456789')

    with self.assertRaises(DatabaseValueError):
      tt.textfld = '0123456789A'

    tt.textfld = None
    self.assertIsNot(tt.textfld, None)
    self.assertIs(tt.textfld, '')
