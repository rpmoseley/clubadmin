'''
This module provides the customised TextCtrl class
'''

import wx
from . import BaseMixin

class TextCtrl(wx.TextCtrl, BaseMixin):
  '''Provide an overloaded variant of the TextCtrl to add the support of labels'''
  def __init__(self, *args, **kwds):
    BaseMixin.__init__(self, wx.TextCtrl, *args, **kwds)
