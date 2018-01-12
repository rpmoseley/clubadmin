'''
This module provides the customised Image class
'''

import wx

class Image(wx.Image):
  '''Provide an overloaded variant of the Image to add the support of labels'''
  def __init__(self, *args, **kwds):
    label = kwds.pop('label', None)
    wx.Image.__init__(self, *args, **kwds)
    if label is not None:
      self.label = wx.StaticText(label)
