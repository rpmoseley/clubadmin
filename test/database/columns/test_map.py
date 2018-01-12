'''
This is the test file for the MapColumn datatype used to provide a mapping from
an internal numeric value into the related external value, this is meant to
provide an easily maintained list of valid values for fields where there is a
limited range of values, such as gender.
'''

import unittest
from clubadmin.config.options import DefaultOptions

class TestMapColumn(unittest.TestCase):
  def test_defaults(self):
    '''Check that the minimum default options are available'''
    gender = DefaultOptions['gender']
    self.assertIn('Male',          gender)
    self.assertIn('Female',        gender)
    self.assertIn('Other',         gender)
    self.assertIn('NotSaid',       gender)
    member = DefaultOptions['member']
    self.assertIn('Normal',        member)
    self.assertIn('Life',          member)
    self.assertIn('New',           member)
    self.assertIn('Honourable',    member)
    state = DefaultOptions['state']
    self.assertIn('None',          state)
    self.assertIn('Banned',        state)
    self.assertIn('In-arrears',    state)
    self.assertIn('Inactive',      state)
