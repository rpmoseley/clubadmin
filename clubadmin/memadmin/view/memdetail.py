'''
This module provides the frame that represents a members' details including
their photo. It also provides the individual panels to make the information
more modula and able to be used in other frames or dialogs.
'''

import wx
import wx.adv
from ...common.utils.ui_valid import PhoneValidator, MobileValidator, EmailValidator, LifeValidator
    
class MemberDetailFrame(wx.Frame):
  '''Provides the frame in which the member details can be displayed'''
  def __init__(self, *args, **kwds):
    kwds['style'] = wx.DEFAULT_FRAME_STYLE
    super().__init__(*args, **kwds)

    # Create the attributes that are accessed in this dialog as a whole
    self._MemberName = wx.TextCtrl(self, label='Name')
    self._MemberActive = wx.CheckBox(self, label='Active', default=False)
    self._MemberVisits = wx.StaticText(self, label='Visits')
    self._MemberAddress = wx.TextCtrl(self, label='Address')
    self._MemberDOB = wx.adv.DatePickerCtrl(self, label='DOB')
    self._MemberTelephone = wx.TextCtrl(self, label='Telephone', validator=PhoneValidator)
    self._MemberMobile = wx.TextCtrl(self, label='Mobile', validator=MobileValidator)
    self._MemberEmail = wx.TextCtrl(self, label='Email', validator=EmailValidator)
    self._MemberJoined = wx.adv.DatePickerCtrl(self, label='Joined')
    self._MemberRenewed = wx.adv.DatePickerCtrl(self, label='Renewed')
    self._MemberLife = wx.CheckBox(self, label='Life', validator=LifeValidator)
    self._MemberPhoto = wx.Image(320, 240, label='Photo')
    self._MemberNumber = wx.StaticText(self, label='Number')

    # Layout the dialog 
    self.__layout()

  def __layout(self):
    sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
    panel_left = wx.Choicebook(self, -1)
    panel_left.Add(self._GeneralDetails())
    if is_authoriser():
      panel_left.Add(self._AddressDetails())
    panel_left.Add(self._HistoryDetails())
    panel_right = wx.Panel(self)
    panel_right.Add(self.MemberPhoto)
    panel_right.Add(self.MemberNumber)
    sizer.Add(panel_left)
    sizer.Add(panel_right)
    self.SetSizer(sizer)

  # Define the various panels that display the different information for a member
  def _GeneralDetails(self, *args, **kwds):
    '''Display the general details for the member'''
    panel = wx.Panel(self, *args, **kwds)
    sizer = wx.FlexGridSizer(2)
    name_lbl = wx.StaticText(panel)
    name_lbl.Value = 'Name:'
    sizer.Add(name_lbl)
    sizer.Add(self._MemberName)

  def _AddressDetails(self, *args, **kwds):
    panel = wx.Panel(self, *args, **kwds)
    '''Display the personal details for the member'''

  def _HistoryDetails(self, *args, **kwds):
    '''Display the history details for the member'''
    panel = wx.Panel(self, *args, **kwds)

  # Define the access properties for all the visible attributes with optional validation
  def _gt_name(self):
    return self._MemberName.Value
  def _st_name(self, value):
    self._MemberName.Value = value
  MemberName = property(fget=_gt_name, fset=_st_name, doc='Name of member')

  def _gt_active(self):
    return self._MemberActive.Value
  def _st_active(self, value):
    self._MemberActive.Value = bool(value)
  MemberActive = property(fget=_gt_active, fset=_st_active, doc='Member is active')

  def _gt_visits(self):
    return self._MemberVisits.Value
  def _st_visits(self, value):
    self._MemberVisits.Value = value
  MemberVisits = property(fget=_gt_visits, fset=_st_visits, doc='Number of visits by member')

  def _gt_address(self):
    return self._MemberAddress.Value
  def _st_address(self, value):
    self._MemberAddress.Value = value
  MemberAddress = property(fget=_gt_address, fset=_st_address, doc='Address of member')

  def _gt_dob(self):
    return self._MemberDOB.Value    # TODO Need to convert to a Date object
  def _st_dob(self, value):
    self._MemberDOB.Value = value   # TODO Need to convert from a Date object
  MemberDOB = property(fget=_gt_dob, fset=_st_dob, doc='Date of birth for member')

  def _gt_telephone(self):
    return self._MemberTelephone.Value
  def _st_telephone(self, value):
    self._MemberTelephone.Value = value
  MemberTelephone = property(fget=_gt_telephone, fset=_st_telephone, doc='Landline number for member')

  def _gt_mobile(self):
    return self._MemberMobile.Value
  def _st_mobile(self, value):
    self._MemberMobile.Value = value
  MemberMobile = property(fget=_gt_mobile, fset=_st_mobile, doc='Mobile number for member')

  def _gt_email(self):
    return self._MemberEmail.Value
  def _st_email(self, value):
    self._MemberEmail.Value = value  # TODO Add validation on the value
  MemberEmail = property(fget=_gt_email, fset=_st_email, doc='Email address for member')

  def _gt_joined(self):
    return self._MemberJoined.Value
  def _st_joined(self, value):
    self._MemberJoined.Value = value
  MemberJoined = property(fget=_gt_joined, fset=_st_joined, doc='Date member joined')

  def _gt_renewed(self):
    return self._MemberRenewed.Value
  def _st_renewed(self, value):
    self._MemberRenewed.Value = value
  MemberRenewed = property(fget=_gt_renewed, fset=_st_renewed, doc='Date member renewed')

  def _gt_life(self):
    return self._MemberLife.Value
  def _st_life(self, value):
    self._MemberLife.Value = value
  MemberLife = property(fget=_gt_life, fset=_st_life, doc='Member is a life member')

  def _gt_photo(self):
    return self._MemberPhoto if self._MemberPhoto.IsOk() else None
  def _st_photo(self, value):
    # TODO Implement this which will load the image then rescale it to the desired size
    self._MemberPhoto.Value = value
  MemberPhoto = property(fget=_gt_photo, fset=_st_photo, doc='Photo of the member')

  def _gt_number(self):
    return self._MemberNumber.Value
  def _st_number(self, value):
    self._MemberNumber.Value = value
  MemberNumber = property(fget=_gt_number, fset=_st_number, doc='Members number')

def main():
  class TestApp(wx.App):
    def OnInit(self):
      self.frame = MemberDetailFrame(None, wx.ID_ANY, '')
      self.SetTopWindow(self.frame)
      self.frame.Show()
      return True

  app = TestApp(0)
  app.MainLoop()
