'''
This module provides the unique Member IDs
'''
from . import columns, BaseTable

class MemberID(BaseTable):
  memid = columns.IntegerColumn()
  memtype = columns.MapColumn('member') # This is filled in by the options module
  photo = columns.PhotoColumn()
