'''
This module provides a sample database table implemented using the columns module in
order to explore the issues that may arise when performing a database retrieval or
store.
'''

import apsw
import sys

class _BaseTableMixin:
  '''Class providing the shared functionality for access to the database tables
     utilising the columns.* classes and adding the appropriate conversion methods
     required to meet the requirements of the underlying database library.'''
  def __init__(self, tabname=None, *args, **kwargs):
    if not hasattr(self, '_fldict'):
      raise TypeError('Table must have some fields defined to be a valid table')
    if tabname is None:
      self._tabname = self.__class__.__name__
    elif isinstance(tabname, str):
      self._tabname = tabname
    else:
      raise TypeError('Tabname if specified should be a str')

  def _connok(self, conn):
    'Check if the connection is valid and open'
    if not isinstance(conn, apsw.Connection):
      raise ValueError('A valid APSW connection is required')

  def _as_sqlvalues(self):
    'Return all the valid columns suitable for use in a cursor'
    return ','.join([self._fldict[fldname]._as_sqlvalue(self) for fldname in self._data_flds if fldname not in self._ignore_flds])
    
  def _as_sqlbind(self):
    'Return all the valid columns suitable for binding in a cursor'
    res = dict()
    for fldname in self._data_flds:
      if fldname not in self._ignore_flds:
        res[fldname] = self._fldict[fldname]._as_sqlvalue(self)
    return res

  def _rowdesc(self, conn):
    'Retrieve the columns actually available on the underlying table'
    self._connok(conn)
    if not hasattr(self, '_sql_columns'):
      rowset = conn.cursor().execute('pragma table_info({})'.format(self._tabname))
      self._data_flds = data_cols = [row[1] for row in rowset]
      db_cols = set(data_cols)
      app_cols = set([fld for fld in self._fldict.keys()])
      self._ignore_flds = ign_cols = db_cols - app_cols
      self._default_flds = app_cols - db_cols
      self._used_flds = used_flds = db_cols - ign_cols
      self._sql_columns = ','.join([fldname for fldname in data_cols if fldname in used_flds])

  def _select(self, conn, memid=None):
    'Fetch the information for the given MEMID or all members'
    self._rowdesc(conn)
    if memid is None:
      rowset = conn.cursor().execute('select {0._sql_columns} from {0._tabname}'.format(self))
    elif not isinstance(memid, int):
      raise ValueError('Member ID must be an integer value')
    elif memid < 0:
      raise ValueError('Member ID must be a positive integer value')
    else:
      rowset = conn.cursor().execute('select {0._sql_columns} from {0._tabname} where memid = :memid'.format(self), {'memid' : memid})

    # Handle the row ignoring those fields that are not in the application definition
    for row in rowset:
      for idx, value in enumerate(row):
        fldname = self._data_flds[idx]
        if fldname in self._used_flds:
          setattr(self, fldname, value)
        elif fldname in self._default_flds:
          setattr(self, fldname, None)
      yield self

  def _insert(self, conn):
    'Insert a new record whose values come from the fields defined at class instantiation'
    self._rowdesc(conn)
    colvalues = ','.join([self._fldict[fldname]._as_sqlvalue(self) for fldname in self._data_flds if fldname not in self._ignore_flds])
    sqltext = 'insert into {0._tabname} ({0._sql_columns}) values ({1})'.format(self, colvalues)
    print('SQL:', sqltext)
    # conn.cursor().execute(sqltext)
 
if sys.version_info.minor < 6:
  # Versions before 3.6 require special handling to maintain the order of fields
  class _TableMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
      return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
      result = type.__new__(cls, name, bases, dict(namespace))
      if name.endswith('_TableMeta'):
        return result
      for name, info in namespace.items():
        info.__set_name__(result, name)
      return result

  class BaseTable(_BaseTableMixin, metaclass=_TableMeta):
    pass
else:
  # Versions after 3.5 maintain the order of class attributes
  BaseTable = _BaseTableMixin
