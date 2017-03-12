#!/bin/python

from os  import uname, system as bash
from sys import path

path.append ('/data/git/Python/moduls')

from reglament_classes import SystemCommand, StaffDoing, StaffType, Host, StaffNeed

THIS_HOST = Host (name = uname ().nodename)

staff_needs = StaffNeed.filter (host = THIS_HOST)

for staff_need in staff_needs:
  if staff_need.is_need:
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