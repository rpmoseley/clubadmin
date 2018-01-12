'''
This is the test for the clubadmin.config.absolute module
'''

import unittest
import clubadmin.shared.utils.absolute as Absolute

class TestAbsRange(unittest.TestCase):
  '''Test the AbsRange class to ensure it is correct'''
  def test_abs_init(self):
    # Test the __init__ function is handling arguments correctly
    self.assertRaises(TypeError,  Absolute.AbsRange)
    self.assertRaises(ValueError, Absolute.AbsRange, -1, -1)
    self.assertRaises(ValueError, Absolute.AbsRange,  0, -1)
    self.assertRaises(ValueError, Absolute.AbsRange, -1,  0)
    self.assertRaises(ValueError, Absolute.AbsRange,  0,  0)
    self.assertRaises(ValueError, Absolute.AbsRange,  1,  0)
    self.assertRaises(ValueError, Absolute.AbsRange,  2,  1)
    self.assertRaises(ValueError, Absolute.AbsRange,  1,  1)

  def _internal_abs_check(self, error):
    # Internal method to avoid duplication of testing code
    ar = Absolute.AbsRange(0, 10, error=error)
    if error:
      self.assertRaises(ValueError, ar.Check, 'BadValue')
      self.assertRaises(ValueError, ar.Check, 5.0)
      self.assertRaises(Absolute.AbsCheckError, ar.Check, -1)
      self.assertRaises(Absolute.AbsCheckError, ar.Check, 11)
    else:
      self.assertFalse(ar.Check('BadValue'))
      self.assertFalse(ar.Check(5.0))
      self.assertFalse(ar.Check(-1))
      self.assertFalse(ar.Check(11))
    self.assertTrue(ar.Check(5))
    self.assertTrue(ar.Check(0))
    self.assertTrue(ar.Check(10))

  def test_abs_check_error(self):
    # Test the Check function is handling arguments correctly in error mode
    self._internal_abs_check(True)

  def test_abs_check_return(self):
    # Test the Check function is handling arguments correctly in return mode
    self._internal_abs_check(False)

  def test_abs_property(self):
    # Check that the properties on the range are correct
    ar = Absolute.AbsRange(3, 9)
    self.assertEqual(ar.Min, 3)
    self.assertEqual(ar.Max, 9)
