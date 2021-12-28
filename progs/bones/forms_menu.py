#!/usr/bin/python

import urwid

pyramid_bttn = urwid.Button(
  '''Pyramid
  ┌┬┐
  └┴┘
┌┬┐ ┌┬┐
└┴┘ └┴┘
-------'''
)
square_bttn = urwid.Button(
'''Square
┌┐ ┌┬┐
├┤ └┴┘
└┘  ┌┐
┌┬┐ ├┤
└┴┘ └┘
------'''
)
grave_bttn = urwid.Button(
'''Grave
  ┌┐
  ├┤
  └┘
┌┬┐┌┬┐
└┴┘└┴┘
------'''
)
solitare_bttn = urwid.Button(
'''Solitare
┌┬┐┌┬┐
└┴┘└┴┘
   ┌┬┐
   └┴┘
------'''
)
exit_bttn = urwid.Button('Exit')

pile = urwid.Pile([pyramid_bttn, square_bttn, grave_bttn, solitare_bttn, urwid.Divider(), exit_bttn])
fill = urwid.Filler(pile)

def on_exit_clicked(button):
  raise urwid.ExitMainLoop()

urwid.connect_signal(exit_bttn, 'click', on_exit_clicked)

urwid.MainLoop(fill).run()

