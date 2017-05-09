#!/bin/python

from os   import system as bash
from time import sleep

TMP_FILE     = '/data/tmp/temperature.tmp'
list_devices = []

class Device (object):
  '''Устройство'''
  def __init__ (self, name, adapter = None):
    self.name         = name
    self.adapter      = adapter
    self.list_sensors = []

  def __str__ (self):
    string = 'Устройство: %s, адаптер: %s, сенсоров: %d' % (self.name, self.adapter, len (self.list_sensors))
    return string

  def add_sensor (self, sensor):
    self.list_sensors.append (sensor)

  def replace_sensor (self, new_sensor):
    for i in range (len (self.list_sensors)):
      sensor = self.list_sensors [i]
      if sensor.name == new_sensor.name:
        self.list_sensors [i] = new_sensor

class Sensor (object):
  '''Датчик'''
  def __init__ (
    self,
    name,
    type           = None,
    input          = None,
    max            = None,
    crit           = None,
    crit_alarm     = None,
    min            = None,
    max_hyst       = None,
    crit_hyst      = None,
    emergency      = None,
    emergency_hyst = None,
  ):
    self.name           = name
    self.type           = type
    self.input          = input
    self.max            = max
    self.crit           = crit
    self.crit_alarm     = crit_alarm
    self.min            = min
    self.max_hyst       = max_hyst
    self.crit_hyst      = crit_hyst
    self.emergency      = emergency
    self.emergency_hyst = emergency_hyst

  def __str__ (self):
    string = '  Сенсор: %s, тип: %s' % (self.name, self.type)
    return string

  def print_parms (self):
    string = '''    Текущее значение:                %s
    Максимально допустимое значение: %s
    Критическое значение:            %s
    Crit_alarm:                      %s
    Минимально допустимое значение:  %s
    Max_hyst:                        %s
    Crit_hyst:                       %s
    Emergency:                       %s
    Emergency_hyst:                  %s''' % (
      str (self.input),
      str (self.max),
      str (self.crit),
      str (self.crit_alarm),
      str (self.min),
      str (self.max_hyst),
      str (self.crit_hyst),
      str (self.emergency),
      str (self.emergency_hyst),
    )
    print (string)

bash ('sensors -u | grep -v ^$ > %s' % TMP_FILE)

with open (TMP_FILE, 'r') as file:
  lines = file.readlines ()
  for line in lines:
    line = line.replace ('\n', '')
    if  ('Adapter: '       not in line) and \
        ('input:'          not in line) and \
        ('max:'            not in line) and \
        ('crit:'           not in line) and \
        ('crit_alarm:'     not in line) and \
        ('min:'            not in line) and \
        ('max_hyst:'       not in line) and \
        ('crit_hyst:'      not in line) and \
        ('emergency:'      not in line) and \
        ('emergency_hyst:' not in line):
          if ':' not in line:
            device = Device (name = line)
            list_devices.append (device)
          else:
            sensor = Sensor (name = line.replace (':', ''))
            device.add_sensor (sensor)
    elif 'Adapter: ' in line:
      device.adapter = line.replace ('Adapter: ', '')
    elif 'input:' in line:
      if 'temp' in line: sensor.type = 'temp'
      elif 'in' in line: sensor.type = 'volt'
      name, value = line.split ('_input:')
      sensor.input = float (value)
      device.replace_sensor (sensor)
    elif 'max:' in line:
      if 'temp' in line: sensor.type = 'temp'
      elif 'in' in line: sensor.type = 'volt'
      name, value = line.split ('_max:')
      sensor.max = float (value)
      device.replace_sensor (sensor)
    elif 'crit:' in line:
      name, value = line.split ('_crit:')
      sensor.crit = float (value)
      device.replace_sensor (sensor)
    elif 'crit_alarm:' in line:
      name, value = line.split ('_crit_alarm:')
      sensor.crit_alarm = float (value)
      device.replace_sensor (sensor)
    elif 'min:' in line:
      name, value = line.split ('_min:')
      sensor.min = float (value)
      device.replace_sensor (sensor)
    elif 'max_hyst:' in line:
      name, value = line.split ('_max_hyst:')
      sensor.max_hyst = float (value)
      device.replace_sensor (sensor)
    elif 'crit_hyst:' in line:
      name, value = line.split ('_crit_hyst:')
      sensor.crit_hyst = float (value)
      device.replace_sensor (sensor)
    elif 'emergency:' in line:
      name, value = line.split ('_emergency:')
      sensor.emergency = float (value)
      device.replace_sensor (sensor)
    elif 'emergency_hyst:' in line:
      name, value = line.split ('_emergency_hyst:')
      sensor.emergency_hyst = float (value)
      device.replace_sensor (sensor)

while True:
  for device in list_devices:
    for sensor in device.list_sensors:
      if sensor.input:
        res = 'good'
        if   sensor.min  and (sensor.input <  sensor.min):  res = 'Значение ниже допустимого!'
        elif sensor.crit and (sensor.input >= sensor.crit): res = 'Значение критическое!!!'
        elif sensor.max  and (sensor.input >  sensor.max):  res = 'Значение выше допустимого!'
      else:
        res = 'good'
      if res != 'good':
        bash ('notify-send "%s %s %s"' % (device, sensor, res))
  sleep (10)
