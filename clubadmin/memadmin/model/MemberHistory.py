'''
This module represents the history of the members in terms of their subscriptions
'''
from ..database import columns, BaseTable

class MemberHistory(BaseTable):
  memid = columns.IntegerColumn()
  renewed = columns.YearColumn()
  assoc_card = columns.TextColumn(100)
  year_card = columns.YearColumn()
  subs_cost = columns.MoneyColumn()
