'''
This module provides the Member object that represents a member within the program,
it is an amalgamation of the underlying data model to provide a single object that
can be passed around and operated on as required. Most of the attributes are local
to the object and are accessed using the property decorator in order to apply some
form of data validation.
'''

from ..config.range import AbsMemberSettings
from .utils.security import authorised
from datetime import date, datetime

class Member:
  '''Class representing a member within the clubadmin package'''
  _UniqueMemberID = None   # NOTE: This should be initialised from the database before use

  def __init__(self, template=None, **kwds):
    self._authorised = True    # TST Set this during testing
    if self._UniqueMemberID is None:
      # Perform necessary tasks to produce a starting unique ID
      self._UniqueMemberID = self._InitUniqMemberID()

    # Populate with either an empty set or an initial set of attributes
    self._Init(template)

  def _InitUniqMemberID(self):
    '''Determine the next unused member ID that is higher than the current
       members to avoid reusing numbers that may be related to life members
       that have not been seen for a number of years'''

  def _Init(self, template):
    '''Copy a template using the property decorators for each attribute to ensure
       that the data is validated'''
    if template is None:
      # Create an empty but valid member
      self._MemberNumber = None                   # Use automatic numbers
      self._MemberName = ''
      self._MemberAddress = ''
      self._MemberPhoto = None
      self._MemberDOB = None
      self._MemberJoined = None
      self._MemberRenewed = None
      pass
    elif isinstance(template, Member):
      # Copy the underlying attributes directly
      pass
    elif isinstance(template, dict):
      # Copy the items from the dictionary indirectly
      pass
    elif isinstance(template, (list, tuple)):
      # Copy the items from the sequence indirectly
      pass
    else:
      raise ValueError('Unhandled template type: {}'.format(template.__class__.__name__))

  # Property functions to access the underlying attributes
  @authorised
  def _gt_MemberNumber(self):
    if self._MemberNumber is None:
      self._MemberNumber = next(self._UniqueMemberID)
    return self._MemberNumber if AbsMemberSettings.Number.Check(self._MemberNumber) else None

  @authorised
  def _st_MemberNumber(self, value):
    if value is None:
      if isinstance(self._MemberNumber, int) and self._MemberNumber > 0:
        raise ValueError('Attempt to overwrite an existing MemberNumber with an automatic one')
    else:
      if not isinstance(value, int):
        raise ValueError('MemberNumber should be an integer')
      if not AbsMemberSettings.Number.Check(value):
        raise ValueError('MemberNumber should be {0.Number.Min}..{0.Number.Max}'.format(AbsMemberSettings))
    self._MemberNumber = value
  MemberNumber = property(_gt_MemberNumber, _st_MemberNumber)
      
  @authorised
  def _gt_MemberName(self):
    return '' if self.MemberNumber is None else self._MemberName

  @authorised
  def _st_MemberName(self, value):
    if not isinstance(value, (str, bytes)):
      raise ValueError('MemberName should be an instance of str or bytes')
    if not AbsMemberSettings.Name.Check(len(value)):
      raise ValueError('MemberName should have {0.Name.Min} to {0.Name.Max} characters'.format(AbsMemberSettings))
    self._MemberName = value
  MemberName = property(_gt_MemberName, _st_MemberName)

  @authorised
  def _gt_MemberAddress(self):
    return '' if self.MemberNumber is None else self._MemberAddress

  @authorised
  def _st_MemberAddress(self, value):
    if (isinstance(value, (list, tuple)) and not any(value)) or \
       (isinstance(value, str)           and value == '')    or \
       (isinstance(value, bytes)         and value == b''):
      raise ValueError('MemberAddress should not be empty')
    addr = value.join(', ') if isinstance(value, (list, tuple)) else value
    if not AbsMemberSettings.Address.Check(len(addr)):
      raise ValueError('MemberAddress should have {0.Address.Min} to {0.Address.Max} characters'.format(AbsMemberSettings))
    self._MemberAddress = addr
  MemberAddress = property(_gt_MemberAddress, _st_MemberAddress)

  @authorised
  def _gt_MemberDOB(self):
    return None if self.MemberNumber is None else self._MemberDOB

  @authorised
  def _st_MemberDOB(self, value):
    if not isinstance(value, date):
      raise ValueError('MemberDOB should be an instance of datetime.date')
    if not AbsMemberSettings.DOB.Check(value.year):
      raise ValueError('MemberDOB year should be {0.DOB.Min}..{0.DOB.Max}'.format(AbsMemberSettings))
    self._MemberDOB = value
  MemberDOB = property(_gt_MemberDOB, _st_MemberDOB)

  @authorised
  def _gt_MemberJoined(self):
    return None if self.MemberNumber is None else self._MemberJoined

  @authorised
  def _st_MemberJoined(self, value):
    if not isinstance(value, int):
      raise ValueError('MemberJoined should be an integer')
    if not AbsMemberSettings.Joined.Check(value):
      raise ValueError('MemberJoined should be {0.Joined.Min}..{0.Joined.Max}'.format(AbsMemberSettings))
    self._MemberJoined = value
  MemberJoined = property(_gt_MemberJoined, _st_MemberJoined)

  @authorised
  def _gt_MemberRenewed(self):
    return None if self.MemberNumber is None else self._MemberRenewed

  @authorised
  def _st_MemberRenewed(self, value):
    if not isinstance(value, int):
      raise ValueError('MemberRenewed should be an integer')
    if not AbsMemberSettings.Renewed.Check(value):
      raise ValueError('MemberRenewed should be {0.Renewed.Min}..{0.Renewed.Max}'.format(AbsMemberSettings))
    self._MemberRenewed = value
  MemberRenewed = property(_gt_MemberRenewed, _st_MemberRenewed)

  @authorised
  def _gt_MemberTelephone(self):
    return None if self.MemberNumber is None else self._MemberTelephone

  @authorised
  def _st_MemberTelephone(self, value):
    pass
  MemberTelephone = property(_gt_MemberTelephone, _st_MemberTelephone)

  @authorised
  def _gt_MemberMobile(self):
    pass

  @authorised
  def _st_MemberMobile(self, value):
    pass
  MemberMobile = property(_gt_MemberMobile, _st_MemberMobile)

  @authorised
  def _gt_MemberEmail(self):
    pass

  @authorised
  def _st_MemberEmail(self, value):
    pass
  MemberEmail = property(_gt_MemberEmail, _st_MemberEmail)

  @authorised
  def _gt_MemberGender(self):
    pass

  @authorised
  def _st_MemberGender(self, value):
    pass
  MemberGender = property(_gt_MemberGender, _st_MemberGender)
