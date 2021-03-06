#!/bin/python

from os   import system as bash
from sys  import path
from time import sleep

path.append ('/data/git/Python/moduls')

from reglament_classes import Host, StaffType, StaffNeed

def not_ping_server ():
  error = bool (bash ('ping -c 1 HomeServer 1>&- 2>&-'))
  if error: bash ('notify-send "Нет связи с сервером"')
  return error

def is_notify ():
  doing = False
  for host in Host.all ():
    try:
      list_staff_needs = StaffNeed.filter (host = host)
      if not list_staff_needs: doing = True
      for staff_need in list_staff_needs:
        if staff_need.is_need:
          doing = True
          bash ('notify-send "%s требуется %s"' % (host.name, staff_need.type.comment))
    except:
      doing = True
      bash ('notify-send "Ошибка получения данных с сервера"')
  return doing

while not_ping_server ():
  sleep (10)
  
while is_notify ():
  sleep (10)

bash ('notify-send "Обслуживание не требуется"')
