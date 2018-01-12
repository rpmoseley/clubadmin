'''
This module provides the default options configuration information for the entire
ClubAdmin package.
'''

import copy

# Define the default options that will be loaded into the Options table when installing
# for the first time the package is run.
DefaultOptions = {
  'gender' : ['Male', 'Female', 'Other', 'NotSaid'],
  'member' : ['Normal', 'Life', 'New', 'Honourable'],
  'state'  : ['None', 'Banned', 'In-arrears', 'Inactive']
}

DefaultSettings = {
  'life_years'   : 15,                # Number of years to be a full member before life member
  'life_age'     : 65,                # Age before member can become a life member
  'life_renewal' : 1,                 # Period after which life member becomes Life-inactive
  'renewal'      : 1,                 # Period after which full member becomes Inactive
}

DefaultSubscriptions = {
  'Normal'     : 15.00,               # Full member yearly subscription
  'Life'       :  1.00,               # Optional life member yearly subscription
  'New'        : 16.05,               # New member joining fee including photo and membership
  'Staff'      :  0.00,               # Staff membership whilst working full-time
}

# Classes providing controlled access to the options information
class OptionsMixin:
  '''Class providing the shared functionality for the various options classes'''
  def __init__(self, default, **kwds):
    if not isinstance(default, dict):
      raise ValueError('Must pass a dictionary to provide defaults')
    self._dict = copy.deepcopy(default)

  def __getattr__(self, name):
    pass

  def __setattr__(self, name, value):
    if name[0] == '_':
      return object.__setattr__(self, name, value)
    if name not in self._vld_names and name[0] != '_':
      raise AttributeError('Not a valid attribute {}'.format(name))
    

class Options(OptionsMixin):
  '''Class providing validation on the options within the package'''
  def __init__(self, default=DefaultOptions, **kwds):
    pass
    
class OptionSettings(OptionsMixin):
  '''Class providing validation on the settings for the clubadmin package'''
  def __init__(self, default=DefaultSettings, **kwds):
    if default is None:
      raise ValueError('Must pass a valid default dictionary')
    self._life_years   = kwds.get('life_years',   default.get('life_years',   15))
    self._life_age     = kwds.get('life_age',     default.get('life_age',     65))
    self._life_renewal = kwds.get('life_renewal', default.get('life_renewal',  1))
    self._renewal      = kwds.get('renewal',      default.get('renewal',       1))

class OptionsSubscriptions(OptionsMixin):
  '''Class providing validation on the subscriptions for the clubadmin package'''
  def __init__(self, default=DefaultSubscriptions, **kwds):
    if default is None:
      raise ValueError('Must pass a valid default dictionary')
    self._normal = kwds.get('normal', default.get('normal', 15.00))
    self._life   = kwds.get('life',   default.get('life',    1.00))
    self._new    = kwds.get('new',    default.get('new',    16.05))
    self._staff  = kwds.get('staff',  default.get('staff',   0.00))
