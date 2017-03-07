#!/bin/python

from os              import system as bash
from sys             import path

path.append ('/data/git/Python/moduls')

from reglament_defs import write_db, update_db, read_db

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

class StaffNeed (object):
  '''Необходимость обслуживания'''
  def __init__ (self, id):
    self.id      = id
    self.host, self.type, self.is_need = read_db (tables = 'staff_need', columns = 'host, type, is_need', case = 'id = %d' % self.id, type = 'row')
    self.is_need = bool (self.is_need)

  def __str__(self):
    return (self.id, self.host, self.type, self.is_need)

