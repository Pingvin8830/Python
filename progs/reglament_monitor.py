#!/bin/python

from datetime import datetime, time, date, timedelta
from sys      import path

path.append ('/data/git/Python/moduls')

from reglament_classes import StaffType, Host, StaffNeed
from reglament_defs    import write_db, update_db, read_db

NOW = datetime.today ()

for id_host in read_db (tables = 'hosts', columns = 'id', case = 'id > 0', type = 'all'):
  host = Host (id_host [0])

  for id_staff_type in read_db (tables = 'staff_types', case = 'id > 0', columns = 'id', type = 'all'):
    staff_type = StaffType (id_staff_type [0])

    staff_need = read_db (tables = 'staff_need', columns = 'id', case = 'host = %d AND type = %d' % (host.id, staff_type.id), type = 'val')
    if not staff_need: write_db (table = 'staff_need', columns = ('host', 'type', 'is_need'), row = (host.id, staff_type.id, 0))
    else:             update_db (table = 'staff_need', column = 'is_need', value = 0, case = 'host = %d AND type = %d' % (host.id, staff_type.id))

    period     = host.staff_periods [staff_type.name]
    last       = host.staff_lasts   [staff_type.name]

    if not period:
      continue

    if not last: last = date (1, 1, 1)
    control_date = datetime.combine ((last + timedelta (days = period)), time (0, 0, 0))
    if NOW > control_date:
      update_db (table = 'staff_need', column = 'is_need', value = 1, case = 'host = %d AND type = %d' % (host.id, staff_type.id))

