'''
This module will test the BaseColumn class that is the base of all other column classes
'''

import unittest
import types
from clubadmin.database.columns import _BaseColumn, _FldChanged

class TestFldChanged(unittest.TestCase):
  def test_field_changed(self):
    fc = _FldChanged()
    self.assertIsInstance(fc._changed, set)
    self.assertFalse(fc.anychanges())       # No changes on a new instance
    fc.changed('fld1')
    self.assertTrue(fc.anychanges())        # Now have one change
    self.assertIn('fld1', fc)               # Should have fld1 in the list
    fc.changed('fld2')
    self.assertIn('fld2', fc)               # Should have both fld1, and fld2 in list
    self.assertNotIn('fld3', fc)            # No fld3 in list of changes
    self.assertRaises(KeyError, fc.donechange, 'fld3')
    fc.changed('fld2')
    fc.donechange('fld1')                   # Remove change on fld1
    self.assertNotIn('fld1', fc)
    self.assertIn('fld2', fc)
    self.assertEqual(str(fc), "_FldChanged(changed={'fld2'})")
    fc.clear()
    self.assertEqual(str(fc), '_FldChanged(changed=set())')

class TestBaseColumn(unittest.TestCase):
  def test_init_function(self):
    'Test the BaseColumn.__init__ function'
    self.assertRaises(TypeError, _BaseColumn)
    class BC1(_BaseColumn):
      _valtype = int
    self.assertRaises(TypeError, BC1)
    class BC2(_BaseColumn):
      _valtype = int
      _defaultvalue = 1
    self.assertRaises(TypeError, BC2)
    class BC2B(_BaseColumn):
      _valtype = int
      _defaultvalue = None
    self.assertRaises(TypeError, BC2B)
    class BC3(_BaseColumn):
      _valtype = int
      _defaultvalue = 1
      _quoted = None
    self.assertRaises(TypeError, BC3)
    class BC4(_BaseColumn):
      _valtype = int
      _defaultvalue = 1
      _quoted = False
      _check = None
    bc = BC4()
    self.assertIsInstance(bc._check, types.MethodType)
    class BC5(_BaseColumn):
      _valtype = int
      _defaultvalue = 1.0
      _quoted = False
      _check = None
    self.assertRaises(TypeError, BC5)
    class BC6(_BaseColumn):
      _valtype = int
      _defaultvalue = 1
      _quoted = True
      def _dummy_check(self):
        return False
      _check = _dummy_check
    bc = BC6()
    self.assertEqual(bc._defaultvalue, 1)
    self.assertTrue(bc._quoted)
    self.assertIsInstance(bc._check, types.MethodType)
    self.assertFalse(bc._check(), False)

  def test_integer_field(self):
    class TBC(_BaseColumn):
      _valtype = int
      _defaultvalue = 1
      _quoted = False
    class TBL:
      fld1 = TBC()
    tbl = TBL()
    self.assertTrue(hasattr(tbl, '_changed_flds_'))
    self.assertTrue(hasattr(tbl, '_fldict_'))
    self.assertTrue(hasattr(tbl, '_fld1'))
    self.assertIsInstance(tbl.fld1, int)
    self.assertEqual(tbl.fld1, 1)
    tbl.fld1 = 2
    self.assertIn('fld1', tbl._changed_flds_)
    self.assertIn('fld1', tbl._fldict_)
    self.assertEqual(tbl.fld1, 2)
