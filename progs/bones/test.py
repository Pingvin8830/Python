#!/usr/bin/python

import urwid

palette = []
list_foreground_colors = (
  'black',
  'dark red',
  'dark green',
  'brown',
  'dark blue',
  'dark magenta',
  'dark cyan',
  'light gray',
  'dark gray',
  'light red',
  'light green',
  'yellow',
  'light blue',
  'light magenta',
  'light cyan',
  'white'
)
list_background_colors = (
  'black',
  'dark red',
  'dark green',
  'brown',
  'dark blue',
  'dark magenta',
  'dark cyan',
  'light gray'
)

list_piles = []
for fc in list_foreground_colors:
  list_columns = []
  for bc in list_background_colors:
    palette.append(('%s_%s' % (fc, bc), fc, bc))
    text = urwid.Text('%s foreground, %s background' % (fc, bc))
    list_columns.append(urwid.AttrMap(text, '%s_%s' % (fc, bc)))
  list_piles.append(urwid.Pile(list_columns))

def exit_program(button):
  raise urwid.ExitMainLoop()

button = urwid.Button('Exit', exit_program)
list_piles.append(button)
column = urwid.Columns(list_piles)
filler = urwid.Filler(column)

mainloop = urwid.MainLoop(filler, palette)

mainloop.run()

