#!/bin/python

from os              import system as bash
from sys             import path

path.append ('/data/git/Python/moduls')

from reglament_defs import write_db, update_db, read_db

class StaffType (object):
  '''Тип обслуживания'''
  TABLE = 'staff_types'

  def __init__ (self, id = 0, name = None, comment = None):
    try:
      self.get (id = id, name = name)
    except:
      self.id      = id
      self.name    = name
      self.comment = comment

  def __str__ (self):
    return 'Staff type %d: %s - %s' % (self.id, self.name, self.comment)

  def get (self, id = 0, name = None):
    if id and not name:
      self.id = id
      self.name, self.comment = read_db (tables = self.TABLE, columns = 'name, comment', case = 'id = %d' % self.id, type = 'row')
    elif not id and name:
      self.name = name
      self.id, self.comment = read_db (tables = self.TABLE, columns = 'id, comment', case = 'name = "%s"' % self.name, type = 'row')
    elif id and name:
      self.id      = id
      self.name    = name
      self.comment = read_db (tables = self.TABLE, columns = 'comment', case = 'id = %d AND name = "%s"' % (self.id, self.name), type = 'val')

  def is_find (self):
    return bool (read_db (tables = self.TABLE, column = 'id', case = 'id = %d AND name = "%s"' % (self.id, self.name), type = 'val'))

  def write (self):
    if self.is_find ():
      update_db (table = self.TABLE, column = 'name',    value = self.name,    case = 'id = %d' % self.id)
      update_db (table = self.TABLE, column = 'comment', value = self.comment, case = 'id = %d' % self.id)
    else:
      write_db (table = self.TABLE, columns = ('name', 'comment'), rows = (self.name, self.comment))
    
  def all ():
    list_types = []
    for id in read_db (tables = StaffType.TABLE, columns = 'id', case = 'id > 0', type = 'all'):
      list_types.append (StaffType (id = id [0]))
    return list_types

class StaffPeriod (object):
  '''Период обслуживания'''
  TABLE = 'staff_periods'

  def __init__ (self, id = 0, host = None, type = None, period = 0):
    try:
      self.get (id = id, host = host, type = type)
    except:
      self.id     = id
      self.host   = host
      self.type   = type
      self.period = period

  def __str__ (self):
    return 'Staff period %d: %s / %s - %d' % (self.id, self.host.name, self.type.name, self.period)

  def get (self, id = None, host = None, type = None):
    if not id and (host and type):
      self.id, self.period = read_db (tables = self.TABLE, columns = 'id, period', case = 'host = %d AND type = %d' % (host.id, type.id), type = 'row')
      self.host = host
      self.type = type
    elif id and not (host and type):
      self.host, self.type, self.period = read_db (tables = self.TABLE, columns = 'host, type, period', case = 'id = %d' % id, type = 'row')
      self.id = id
      self.host = Host      (id = self.host)
      self.type = StaffType (id = self.type)
    elif id and (host and type):
      self.period = read_db (tables = self.TABLE, columns = 'period', case = 'id = %d AND host = %d AND type = %d' % (id, host.id, type.id), type = 'val')
      self.id   = id
      self.host = host
      self.type = type

  def is_find (self):
    return bool (read_db (tables = self.TABLE, columns = 'id', case = 'id = %d AND host = %d AND type = %d' % (self.id, self.host.id, self.type.id), type = 'val'))

  def all ():
    list_periods = []
    for id in read_db (tables = StaffPeriod.TABLE, columns = 'id', case = 'id > 0', type = 'all'):
      list_periods.append (StaffPeriod (id = id [0]))
    return list_periods

class StaffLog (object):
  '''Логирование обслуживания'''
  TABLE = 'staff_log'

  def __init__ (self, id = 0, host = None, type = None, data = None, time = None):
    try:
      self.get (id = id)
    except:
      self.id   = id
      self.host = host
      self.type = type
      self.date = data
      self.time = time

  def __str__ (self):
    return 'Staff log %d: %s / %s - %s / %s' % (self.id, self.host.name, self.type.name, self.data, self.time)

  def get (self, id = None, host = None, type = None, date = None):
    if not id and (host and type and date):
      self.id, self.time = read_db (tables = self.TABLE, columns = 'id, time', case = 'host = %d AND type = %d AND date = "%s"' % (host.id, type.id, date), type = 'row')
      self.host = host
      self.type = type
      self.date = date
    elif id and not (host and type and date):
      self.host, self,type, self.date, self.time = read_db (tables = self.TABLE, columns = 'host, type, date, time', case = 'id = %d' % id, type = 'row')
      self.id   = id
      self.host = Host      (id = self.host)
      self.type = StaffType (id = self.type)
    elif id and (host and type and date):
      self.id   = id
      self.host = host
      self.type = type
      self.date = date
      self.time = time

  def is_find (self):
    return bool (read_db (tables = self.TABLE, columns = 'id', case = 'host = %d AND type = %d AND date = "%s"' % (self.host.id, self.type.id, self.date), type = 'val'))

  def last (self, host, type):
    return read_db (tables = self.TABLE, columns = 'max(date)', case = 'host = %d AND type = %d' % (host.id, type.id), type = 'val')

  def write (self):
    write_db (table = self.TABLE, columns = ('host', 'type', 'date', 'time'), row = (self.host.id, self.type.id, str (self.data), str (self.time)))

class Host (object):
  '''Хост'''
  TABLE = 'hosts'

  def __init__ (self, id = 0, name = None, ip = None):
    try:
      self.get (id = id, name = name, ip = ip)
    except:
      self.id   = id
      self.name = name
      self.ip   = ip

  def __str__ (self):
    return 'Host %d: %s - %s' % (self.id, self.name, self.ip)

  def get (self, id = None, name = None, ip = None):
    if not id and not name and ip:
      self.id, self.name = read_db (tables = self.TABLE, columns = 'id, name', case = 'ip = "%s"' % ip, type = 'row')
      self.ip = ip
    elif not id and name and not ip:
      self.id, self.ip = read_db (tables = self.TABLE, columns = 'id, ip', case = 'name = "%s"' % name, type = 'row')
      self.name = name
    elif not id and name and ip:
      self.id   = read_db (tables = self.TABLE, columns = 'id', case = 'name = "%s" AND ip = "%s"' % (name, ip), type = 'val')
      self.name = name
      self.ip   = ip
    elif id and not name and not ip:
      self.name, self.ip = read_db (tables = self.TABLE, columns = 'name, ip', case = 'id = %d' % id, type = 'row')
      self.id = id
    elif id and not name and ip:
      self.name = read_db (tables = self.TABLE, columns = 'name', case = 'id = %d AND ip = "%s"' % (id, ip), type = 'val')
      self.id   = id
      self.ip   = id
    elif id and name and not ip:
      self.ip   = read_db (tables = self.TABLE, columns = 'ip', case = 'id = %d AND name = "%s"' % (id, name), type = 'val')
      self.id   = id
      self.name = name
    elif id and name and ip:
      self.id   = id
      self.name = name
      self.ip   = ip

  def is_find (self):
    return bool (read_db (tables = self.TABLE, columns = 'id', case = 'id = %d AND name = "%s" AND ip = "%s"', type = 'val'))

  def all ():
    list_hosts = []
    for id in read_db (tables = Host.TABLE, columns = 'id', case = 'id > 0', type = 'all'):
      list_hosts.append (Host (id = id [0]))
    return list_hosts

  def filter (name = None, ip = None):
    list_hosts = []
    for id in read_db (tables = Host.TABLE, columns = 'id', case = 'id > 0', type = 'all'):
      host = Host (id = id [0])
      if (host.name == name) or (host.ip == ip):
        list_hosts.append (host)
    return list_hosts

class StaffNeed (object):
  '''Необходимость обслуживания'''
  TABLE = 'staff_need'

  def __init__ (self, id = 0, host = None, type = None, is_need = False, last_control = None):
    try:
      self.get (id = id, host = host, type = type)
    except:
      self.id           = id
      self.host         = host
      self.type         = type
      self.is_need      = is_need
      self.last_control = last_control

  def __str__(self):
    return 'Staff need %d: %s / %s - %s (%s)' % (self.id, self.host.name, self.type.name, self.is_need, self.last_control)

  def get (self, id = None, host = None, type = None):
    if not id and (host and type):
      self.id, self.is_need, self.last_control = read_db (tables = self.TABLE, columns = 'id, is_need, last_control', case = 'host = %d AND type = %d' % (host.id, type.id), type = 'row')
      self.host = host
      self.type = type
      self.is_need = bool (self.is_need)
    elif id and not (host and type):
      self.host, self.type, self.is_need, self.last_control = read_db (tables = self.TABLE, columns = 'host, type, is_need, last_control', case = 'id = %d' % id, type = 'row')
      self.id   = id
      self.host = Host      (id = self.host)
      self.type = StaffType (id = self.type)
      self.is_need = bool (self.is_need)
    elif id and (host and type):
      self.is_need, self.last_control = read_db (tables = self.TABLE, columns = 'is_need, last_control', case = 'id = %d AND host = %d AND type = %d' % (id, host.id, type.id), type = 'row')
      self.id   = id
      self.host = host
      self.type = type
      self.is_need = bool (self.is_need)

  def is_find (self):
    return bool (read_db (tables = self.TABLE, columns = 'id', case = 'id = %d AND host = %d AND type = %d' % (self.id, self.host.id, self.type.id), type = 'val'))

  def write (self):
    if self.is_find ():
      update_db (table = self.TABLE, column = 'is_need',      value = int (self.is_need), case = 'id = %d' % self.id)
      update_db (table = self.TABLE, column = 'last_control', value = self.last_control, case = 'id = %d' % self.id)
    else:
      write_db (table = self.TABLE, columns = ('host', 'type', 'is_need', 'last_control'), row = (self.host.id, self.type.id, int (self.is_need), self.last_control))

  def filter (host = None, type = None, is_need = None):
    list_staff_need = []
    for id in read_db (tables = StaffNeed.TABLE, columns = 'id', case = 'id > 0', type = 'all'):
      staff_need = StaffNeed (id = id [0])
      if   host and (staff_need.host.id == host.id): list_staff_need.append (staff_need)
      elif type and (staff_need.type.id == type.id): list_staff_need.append (staff_need)
    return list_staff_need

class SystemCommand (object):
  '''Системная команда'''
  TABLE = 'system_commands'

  def __init__ (self, id = 0, name = None, text = None):
    try:
      self.get (id = id, name = name, text = text)
    except:
      self.id   = id
      self.name = name
      self.text = text

  def __str__ (self):
    return 'System command %d: %s - %s' % (self.id, self.name, self.text)

  def get (self, id = 0, name = None, text = None):
    if id and not (name and text):
      self.name, self.text = read_db (tables = self.TABLE, columns = 'name, text', case = 'id = %d' % id, type = 'row')
      self.id = id
    elif not id and (name and text):
      self.id   = read_db (tables = self.TABLE, columns = 'id', case = 'name = "%s" AND text = "%s"' % (name, text), type = 'val')
      self.id   = self.id [0]
      self.name = name
      self.text = text
    elif id and (name and text):
      self.id   = id
      self.name = name
      self.text = text

  def is_find (self):
    return bool (read_db (tables = self.TABLE, columns = 'id', case = 'id = %d AND name = %s AND text = %s' % (self.id, self.name, self.text), type = 'val'))

class StaffDoing (object):
  '''Действие по регламенту'''
  TABLE = 'staff_doings'

  def __init__ (self, id = 0, code = None, command = None, task = None, is_need = False, comment = None, type = None, is_args = False, is_loop = False):
    try:
      self.get (id = id, code = code, command = command, type = type)
    except:
      self.id      = id
      self.code    = code
      self.command = command
      self.task    = task
      self.is_need = is_need
      self.comment = comment
      self.type    = type
      self.is_args = is_args
      self.is_loop = is_loop

  def __str__ (self):
    string = 'Staff doing %d: %d - %s (%s)' % (self.id, self.code, self.command.text, self.command.name)
    if self.is_need: string += ', need'
    if self.is_args: string += ', args'
    if self.is_loop: string += ', loop'
    return string

  def get (self, id = 0, code = None, type = None, command = None):
    if not id and not (code and type) and not (code and command) and (type and command):
      self.id, self.code, self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'id, code, task, is_need, comment, is_args, is_loop', case = 'command = %d AND type = %d' % (type, command), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.command = command
      self.type    = type
    elif not id and not (code and type) and (code and command) and not (type and command):
      self.id, self.task, self.is_need, self.comment, self.type, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'id, task, is_need, comment, type, is_args, is_loop', case = 'code = %d AND command = %d' % (code, command.id), type = 'row')
      self.type    = StaffType (id = self.type)
      self.is_need = bool      (self.is_need)
      self.is_args = bool      (self.is_args)
      self.is_need = bool      (self.is_loop)
      self.code    = code
      self.command = command
    elif not id and not (code and type) and (code and command) and (type and command):
      self.id, self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'id, task, is_need, comment, is_args, is_loop', case = 'code = %d AND command = %d AND type = %d' % (code, command.id, type.id), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.code    = code
      self.command = command
      self.type    = type
    elif not id and (code and type) and not (code and command) and not (type and command):
      self.id, self.command, self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'id, command, task, is_need, comment, is_args, is_loop', case = 'code = %d AND type = %d' % (code, type.id), type = 'row')
      self.command = SystemCommand (id = self.command)
      self.is_need = bool          (self.is_need)
      self.is_args = bool          (self.is_args)
      self.is_loop = bool          (self.is_loop)
      self.code = code
      self.type = type
    elif not id and (code and type) and not (code and command) and (type and command):
      self.id, self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'id, task, is_need, comment, is_args, is_loop', case = 'code = %d AND command = %d AND type = %d' % (code, command.id, type.id), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.code    = code
      self.command = command
      self.type    = type
    elif not id and (code and type) and (code and command) and not (type and command):
      self.id, self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'id, task, is_need, comment, is_args, is_loop', case = 'code = %d AND command = %d AND type = %d' % (code, command.id, type.id), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.code    = code
      self.command = command
      self.type    = type
    elif not id and (code and type) and (code and command) and (type and command):
      self.id, self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'id, task, is_need, comment, is_args, is_loop', case = 'code = %d AND command = %d AND type = %d' % (code, command.id, type.id), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.code    = code
      self.command = command
      self.type    = type
    elif id and not (code and type) and not (code and command) and not (type and command):
      self.code, self.command, self.task, self.is_need, self.comment, self.type, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'code, command, task, is_need, comment, type, is_args, is_loop', case = 'id = %d' % id, type = 'row')
      self.id = id
      self.command = SystemCommand (id = self.command)
      self.type    = StaffType     (id = self.type)
      self.is_need = bool          (self.is_need)
      self.is_args = bool          (self.is_args)
      self.is_loop = bool          (self.is_loop)
    elif id and not (code and type) and not (code and command) and (type and command):
      self.code, self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'code, task, is_need, comment, is_args, is_loop', case = 'id = %d AND command = %d AND type = %d' % (id, command.id, type.id), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.id      = id
      self.command = command
      self.type    = type
    elif id and not (code and type) and (code and command) and not (type and command):
      self.task, self.is_need, self.comment, self.type, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'task, is_need, comment, type, is_args, is_loop', case = 'id = %d AND code = %d AND command = %d' % (id, code, command.id), type = 'row')
      self.type    = StaffType (id = self.type)
      self.is_need = bool      (self.is_need)
      self.is_args = bool      (self.is_args)
      self.is_loop = bool      (self.is_loop)
      self.id      = id
      self.code    = code
      self.command = command
    elif id and not (code and type) and (code and command) and (type and command):
      self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'task, is_need, comment, is_args, is_loop', case = 'id = %d AND code = %d AND command = %d AND type = %d' % (id, code, command.id, type.id), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.id      = id
      self.code    = code
      self.command = command
      self.type    = type
    elif id and (code and type) and not (code and command) and not (type and command):
      self.command, self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'command, task, is_need, comment, is_args, is_loop', case = 'id = %d AND code = %d AND type = %d' % (id, code, type.id), type = 'row')
      self.command = SystemCommand (id = self.command)
      self.is_need = bool          (self.is_need)
      self.is_args = bool          (self.is_args)
      self.is_loop = bool          (self.is_loop)
      self.id      = id
      self.code    = code
      self.type    = type
    elif id and (code and type) and not (code and command) and (type and command):
      self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'task, is_need, comment, is_args, is_loop', case = 'id = %d AND code = %d AND command = %d AND type = %d' % (id, code, command.id, type.id), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.id      = id
      self.code    = code
      self.command = command
      self.type    = type
    elif id and (code and type) and (code and command) and not (type and command):
      self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'task, is_need, comment, is_args, is_loop', case = 'id = %d AND code = %d AND command = %d AND type = %d' % (id, code, command.id, type.id), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.id      = id
      self.code    = code
      self.command = command
      self.type    = type
    elif id and (code and type) and (code and command) and (type and command):
      self.task, self.is_need, self.comment, self.is_args, self.is_loop = read_db (tables = self.TABLE, columns = 'task, is_need, comment, is_args, is_loop', case = 'id = %d AND code = %d AND command = %d AND type = %d' % (id, code, command.id, type.id), type = 'row')
      self.is_need = bool (self.is_need)
      self.is_args = bool (self.is_args)
      self.is_loop = bool (self.is_loop)
      self.id = id
      self.code = code
      self.command = command
      self.type = type

  def is_find (self):
    return bool (read_db (tables = self.TABLE, columns = 'id', case = 'id = %d AND code = %d and command = %d AND is_need = %d AND type = %d AND is_args = %d AND is_loop = %d' % (self.id, self.code, self.command.id, int (self.is_need), self.type.id, int (self.is_args), int (self.is_loop))))

  def filter (type):
    list_staff_doing = []
    for id in read_db (tables = StaffDoing.TABLE, columns = 'id', case = 'id > 0', type = 'all'):
      staff_doing = StaffDoing (id = id [0])
      if staff_doing.type.id == type.id: list_staff_doing.append (staff_doing)
    for i in range (len (list_staff_doing)):
      for j in range (i + 1, len (list_staff_doing)):
        if list_staff_doing [i].code > list_staff_doing [j].code:
          tmp                  = list_staff_doing [j]
          list_staff_doing [j] = list_staff_doing [i]
          list_staff_doing [i] = tmp
    return list_staff_doing
      
