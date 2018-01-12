'''
This module provides the current subscription costs for members
'''

from . import columns, BaseTable

class Subscriptions(BaseTable):
  subtype = columns.IntegerColumn()
  text = columns.TextColumn(50)
  cost = columns.MoneyColumn()
  newcost = columns.MoneyColumn()
