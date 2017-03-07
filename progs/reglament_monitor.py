#!/bin/python

from configparser    import RawConfigParser
from datetime        import datetime, time, date, timedelta
from mysql.connector import MySQLConnection, Error
from os              import system as bash

DB_CONFIG = {
  'host':     'localhost',
  'database': 'computers',
  'user':     'pingvin',
  'password': 'server881130',
}

NOW = datetime.today ()

conf = RawConfigParser ()

def read_db (tables, columns, case = None, type = 'all'):
  '''Чтение из БД'''
  rows = None
  try:
    con = MySQLConnection (**DB_CONFIG)
    if con.is_connected ():
      cur = con.cursor ()
      sql = 'SELECT %s FROM %s ' % (columns, tables)
      if case:
        sql += 'WHERE %s' % case
      cur.execute (sql)
      if   type == 'all': rows = cur.fetchall ()
      elif type == 'row': rows = cur.fetchone ()
      elif type == 'val':
        try:
          rows = cur.fetchone () [0]
        except:
          rows = None

  finally:
    cur.close ()
    con.close ()

  return rows

class StaffType (object):
  '''Тип обслуживания'''
  def __init__ (self, id):
    self.id = id
    self.name, self.comment = read_db (tables = 'staff_types', columns = 'name, comment', case = 'id = %d' % self.id, type = 'row')

  def __str__ (self):
    return self.name

class Host (object):
  '''Хост'''
  def __init__ (self, id):
    self.id = id
    self.name, self.ip = read_db (tables = 'hosts', columns = 'name, ip', case = 'id = %d' % self.id, type = 'row')
    self.is_look       = not (bash ('ping -c 1 %s 1>/dev/null' % self.name))
    self.staff_periods = {}
    self.staff_lasts   = {}
    for id in read_db (tables = 'staff_types', columns = 'id', type = 'all'):
      staff_type = StaffType (id [0])
      self.staff_periods [staff_type.name] = read_db (tables = 'staff_periods', columns = 'period', case = 'host = %d AND type = %d' % (self.id, staff_type.id), type = 'val')
      self.staff_lasts   [staff_type.name] = read_db (tables = 'staff_log',     columns = 'date',   case = 'host = %d AND type = %d' % (self.id, staff_type.id), type = 'val')

  def __str__ (self):
    return self.name

for id_host in read_db (tables = 'hosts', columns = 'id', case = 'id > 0', type = 'all'):
  host = Host (id_host [0])
  conf_file = '/network/%s/monitor.conf' % host.name
  conf.read (conf_file)
  if not conf.has_section ('staff_need'): conf.add_section ('staff_need')

  for id_staff_type in read_db (tables = 'staff_types', case = 'id > 0', columns = 'id', type = 'all'):
    staff_type = StaffType (id_staff_type [0])
    period     = host.staff_periods [staff_type.name]
    last       = host.staff_lasts   [staff_type.name]
    conf.set ('staff_need', staff_type.name, False)

    if not period:
      continue

    if not last: last = date (1, 1, 1)
    control_date = datetime.combine ((last + timedelta (days = period)), time (0, 0, 0))
    if NOW > control_date:
      conf.set ('staff_need', staff_type.name, True)

  with open (conf_file, 'w') as config:
    conf.write (config)

