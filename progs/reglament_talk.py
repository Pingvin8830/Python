#!/bin/python

from os   import uname, system as bash
from sys  import path
from time import sleep

path.append ('/data/git/Python/moduls')

from reglament_classes import Host, StaffType, StaffNeed

THIS_HOST = uname ().nodename

host = Host (name = THIS_HOST)

def is_notify ():
  doing = False
  list_staff_needs = StaffNeed.filter (host = host)

  error_ping_server = bash ('ping -c 1 HomeServer 1>&- 2>&-')
  if error_ping_server: 
    doing = True
    bash ('notify-send "Нет связи с сервером"')

  for staff_need in list_staff_needs:
    if staff_need.is_need:
      doing = True
      bash ('notify-send "Требуется %s"' % staff_need.type.comment)
  return doing

while is_notify ():
  sleep (10)
