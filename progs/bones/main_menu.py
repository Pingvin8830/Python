#!/usr/bin/python

import urwid

top_picture = '''
              ┌─────┬─────┐
              │* * *│     │
              │     │  *  │
              │* * *│     │
              └─────┴─────┘
       ┌─────┬─────┐ ┌─────┬─────┐
       │█████│█████│ │█████│█████│
       │█████│█████│ │█████│█████│
       │█████│█████│ │█████│█████│
       └─────┴─────┘ └─────┴─────┘
┌─────┬─────┐ ┌─────┬─────┐ ┌─────┬─────┐
│*    │*    │ │     │     │ │*   *│*    │
│  *  │     │ │     │     │ │     │     │
│    *│    *│ │     │     │ │*   *│    *│
└─────┴─────┘ └─────┴─────┘ └─────┴─────┘
'''

top_text = urwid.Text(top_picture)
start_bttn = urwid.Button('Start game')
manual_bttn = urwid.Button('Manual')
exit_bttn = urwid.Button('Exit')

pile = urwid.Pile([top_text, start_bttn, manual_bttn, exit_bttn])
fill = urwid.Filler(pile)

def on_exit_clicked(button):
  raise urwid.ExitMainLoop()

urwid.connect_signal(exit_bttn, 'click', on_exit_clicked)

urwid.MainLoop(fill).run()

