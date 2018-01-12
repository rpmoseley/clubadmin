'''
Provide a mock object that represents the MemberDetailFrame for testing 
purposes.
'''

class Mock_MemberDetailFrame:
  '''Provide a mock frame for the test framework to use'''
  def __init__(self, *args, **kwds):
    self.MemberName = ''
    self.MemberActive = False
    self.MemberVisits = 0
    self.MemberAddress = None
    self.MemberDOB = None
    self.MemberTelephone = None
    self.MemberMobile = None
    self.MemberEmail = None
    self.MemberJoined = None
    self.MemberRenewed = None
    self.MemberLife = False
    self.MemberPhoto = None
    self.MemberNumber = 0
    self.MemberGender = None
    
  def is_life_member(self):
    return False
