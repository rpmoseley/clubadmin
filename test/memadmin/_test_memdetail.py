'''
This module will perform a unittest on the memdetail GUI view using mock objects,
all values are assumed to be valid within the database.
'''

import unittest
from . import mock_memdetail

class TestMemDetail(unittest.TestCase):
  '''Test the memdetail dialog'''
  def setUp(self):
    dialog = self.dialog = mock_memdetail.Mock_MemberDetailFrame()
    dialog.MemberNumber = 1090
    dialog.MemberName = 'Freddy Starr'
    dialog.MemberGender = 'Male'
    dialog.MemberAddress = '1 Main Road, Harwich, Essex'
    dialog.MemberDOB = '12/04/1950'
    dialog.MemberTelephone = '01255 508910'
    dialog.MemberMobile = '07873 246720'
    dialog.MemberEmail = 'freddy.starr@gmail.com'
    dialog.MemberJoined = 1968
    dialog.MemberRenewed = 2017
    dialog.MemberActive = True
    dialog.MemberLife = True

  def testMemNumber(self):
    self.assertGreater(self.dialog.MemberNumber, 0)

  def testMemLife(self):
    self.assertTrue(self.dialog.is_life_member())
