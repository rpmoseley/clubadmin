'''
This module provides the private information for each member
'''
from . import columns, BaseTable

class MemberInfo(BaseTable):
  memid = columns.IntegerColumn()
  name = columns.TextColumn(255)
  address = columns.TextColumn(1000)
  dob = columns.DateColumn()
  telephone = columns.PhoneColumn()
  mobile = columns.MobileColumn()
  email = columns.EmailColumn()
  gender = columns.MapColumn('gender') # NOTE Uses Options table to fill in details
