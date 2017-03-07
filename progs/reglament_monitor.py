#!/bin/python

from datetime import datetime, time, date, timedelta
from sys      import path

path.append ('/data/git/Python/moduls')

from reglament_classes import StaffType, Host, StaffNeed, StaffPeriod, StaffLog
from reglament_defs    import write_db, update_db, read_db

NOW = datetime.today ()
#print (NOW)
#input ()

for host in Host.all ():
  for staff_type in StaffType.all ():
    staff_period = StaffPeriod (host = host, type = staff_type)
    if not staff_period.is_find (): continue
    log = StaffLog ()
    last = log.last (host = host, type = staff_type)
    if not last: last = date (1, 1, 1)
    control_date = datetime.combine (last, time (0, 0, 0)) + timedelta (days = staff_period.period)
    staff_need = StaffNeed (host = host, type = staff_type)
    staff_need.last_control = NOW
    staff_need.is_need = False
    if NOW >= control_date:
      staff_need.is_need = True
    staff_need.write ()
#    print (
#      '''
#Host:         %s
#Staff:        %s
#Period:       %d
#Last:         %s
#Control date: %s
#Is need:      %s
#      ''' % (host.name, staff_type.name, staff_period.period, last, control_date, staff_need.is_need)
#    )

