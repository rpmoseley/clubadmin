'''
This module provides the customised CheckBox class
'''

import wx

class CheckBox(wx.CheckBox):
  '''Provide an overloaded variant of the CheckBox to add the support of labels'''
  def __init__(self, *args, **kwds):
    label = kwds.pop('label', None)
    wx.CheckBox.__init__(self, *args, **kwds)
    if label is not None:
      self.label = wx.StaticText(label)
