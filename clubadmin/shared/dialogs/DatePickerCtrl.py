'''
This module provides a customised DatePicker class
'''

import wx
import wx.adv

class DatePickerCtrl(wx.adv.DatePickerCtrl):
  '''Provide an overloaded variant of the DatePickerCtrl to add the support of labels'''
  def __init__(self, *args, **kwds):
    label = kwds.pop('label', None)
    wx.adv.DatePickerCtrl.__init__(self, *args, **kwds)
    if label is None:
      self.label = wx.StaticText(label)
