'''
This module provides the absolute range of values for the various parts of the ClubAdmin
package in order to provide a means of modifying them if required.
'''

from ..shared.utils.absolute import AbsRange, AbsSettingsBase

class AbsDatabaseSettings(AbsSettingsBase):
  '''Class encapsulating all the absolute settings for the database'''
  Year    = AbsRange(1900, 2200)   # Range for any YearColumn
  Text    = AbsRange(0,    1000)   # Range for any TextColumn
  Integer = AbsRange(0,    200 )   # Range for any IntegerColumn

class AbsMemberSettings(AbsSettingsBase):
  '''Class encapsulating all the absolute settings for a member'''
  Number  = AbsRange(1000, 9999)   # Specify the range for a member number
  Joined  = AbsRange(1900, 2200)   # Specify the range for a members' joining year
  Renewed = AbsRange(2015, 2200)   # Specify the range for a members' renewal year
  DOB     = AbsRange(1900, 2200)   # Specify the range for a members' DOB year
  Visits  = AbsRange(0,    9999)   # Specify the range for a members' number of visits
