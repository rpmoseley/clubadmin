'''
This directory provides support classes and functions for dialogs
'''

from types import FunctionType

class BaseMixin:
  '''This provides the mixin for dialogs'''
  def __init__(self, *args, **kwds):
    label = kwds.pop('label', None)
    orig_klass = kwds.pop('orig_klass')
    if orig_klass is None:
      raise ValueError("Must pass wx object to initialise as 'orig_klass'")
    orig_klass.__init__(self, *args, **kwds)
    if label is not None:
      self._label = wx.StaticText(label)
    validator = kwds.pop('validator', None)
    if validator is not None:
      if not isinstance(validator, FunctionType):
        raise ValueError('Validator must be a function')
      self._valid_cb = validator
    else:
      self._valid_cb = None
