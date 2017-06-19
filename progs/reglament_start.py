#!/bin/python

from datetime import datetime
from os       import uname, system as bash
from sys      import path, argv

path.append ('/data/git/Python/moduls')

from reglament_classes import SystemCommand, StaffDoing, StaffType, Host, StaffNeed, StaffLog

FORCE     = False
THIS_HOST = Host (name = uname ().nodename)
NOW       = datetime.today ()

staff_needs = StaffNeed.filter (host = THIS_HOST)

while len (argv) > 1:
  if argv [1] == '-f' or argv [1] == '--force':
    FORCE = True
  del argv [1]

for staff_need in staff_needs:
  if staff_need.is_need or FORCE:
    success      = True
    staff_type   = staff_need.type
    staff_doings = StaffDoing.filter (type = staff_type)
    for staff_doing in staff_doings:
      command = staff_doing.command
      doing = input (command.name + ' (y / n)? ')
      if doing.lower () == 'y':
        if staff_doing.is_args:
          arg = input (staff_doing.task + ': ')
          while arg:
            error = bash (command.text + ' %s' % arg)
            if error and staff_doing.is_need: success = False
            arg = input (staff_doing.task + ': ')
        else:
          error = bash (command.text)
          if error and staff_doing.is_need: success = False
      else:
        if staff_doing.is_need: success = False
      print ('Success:', success)
      print ()
    if success:
      log = StaffLog ()
      log.id = 0
      log.host = THIS_HOST
      log.type = staff_type
      log.data = NOW.date ()
      log.time = NOW.time ()
      log.write ()
      staff_need.is_need      = False
      staff_need.last_control = NOW
      staff_need.write ()
