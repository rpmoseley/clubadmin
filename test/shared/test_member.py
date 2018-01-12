'''
This module aims to test each of the functions within the common.member module
'''

import unittest
from clubadmin.config.options import OptionSettings
from clubadmin.shared.member import Member
from clubadmin.config.range import AbsMemberSettings

# NewMember   = Member(number=1000, memtype='New', name='Mr A Newman', address='Somewhere, Newtown, Essex')
# RenewMember = Member(number=1001, memtype='Normal', name='Mr B Renewal', address='Elsewhere, Oldtown, Essex', joined=2016)

class Mock_Member(Member):
  def _InitUniqMemberID(self):
    while True:
      yield AbsMemberSettings.Number.Max
    return None

  def is_life_member(self):
    return False   #TST Initial testing

class TestMember(unittest.TestCase):
  '''This will test the general attributes of a Member'''
  def test_empty_member(self):
    '''Test that the MemberNumber property works correctly'''
    mem = Mock_Member(template=None)
    self.assertIsNotNone(mem._UniqueMemberID)
    self.assertEqual(mem.MemberNumber, AbsMemberSettings.Number.Max)
