#!/bin/python

from configparser    import RawConfigParser
from mysql.connector import MySQLConnection, Error

def read_conf ():
  '''Чтение параметров подключения к БД'''
  conf = RawConfigParser ()
  conf.read ('/data/git/Python/confs/mysql.conf')
  DB_CONFIG = {
    'host':     conf.get ('computers', 'host'),
    'database': conf.get ('computers', 'database'),
    'user':     conf.get ('computers', 'user'),
    'password': conf.get ('computers', 'password'),
  }
  return DB_CONFIG

def write_db (table, columns, row):
  '''Запись в БД'''
  try:
    con = MySQLConnection (**read_conf ())
    if con.is_connected ():
      cur = con.cursor ()
      sql = 'INSERT INTO %s %s VALUES %s' % (table, str (columns).replace ("'", ''), row)
      cur.execute (sql)
      con.commit ()

  except Error as e:
    print (e)

  finally:
    cur.close ()
    con.close ()

def update_db (table, column, value, case = None):
  '''Обновление данных в БД'''
  try:
    con = MySQLConnection (**read_conf ())
    if con.is_connected ():
      cur = con.cursor ()
      sql = 'UPDATE %s SET %s = "%s"' % (table, column, value)
      if case: sql += ' WHERE %s' % case
      cur.execute (sql)
      con.commit ()

  except Error as e:
    print (e)

  finally:
    cur.close ()
    con.close ()

def read_db (tables, columns, case = None, type = 'all'):
  '''Чтение из БД'''
  rows = None
  try:
    con = MySQLConnection (**read_conf ())
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

