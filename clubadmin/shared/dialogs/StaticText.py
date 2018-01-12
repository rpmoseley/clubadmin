'''
This module provides the customised StaticText class
'''

import wx

class StaticText(wx.StaticText):
  '''Provide an overloaded variant of the StaticText to add the support of labels'''
  def __init__(self, *args, **kwds):
    label = kwds.pop('label', None)
    wx.StaticText.__init__(self, *args, **kwds)
    if label is not None:
      self.label = wx.StaticText(label)
