'''
This module provides the general stats for a member
'''
from . import columns, BaseTable

class MemberStat(BaseTable):
  memid = columns.IntegerColumn()
  joined = columns.DateColumn()
  renewed = columns.YearColumn()
  memlength = columns.YearColumn()
  lifestart = columns.YearColumn()
  assoc_card = columns.TextColumn(100)
  year_card = columns.YearColumn()
  active = columns.BoolColumn()
