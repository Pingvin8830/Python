
#import urwid
#from top_picture import TOP_PICTURE
#
#def menu_button(caption, callback):
#  button = urwid.Button(caption)
#  urwid.connect_signal(button, 'click', callback)
#  return urwid.AttrMap(button, None, focus_map='reversed')
#
#def sub_menu(caption, choices):
#  contents = menu(caption, choices)
#  def open_menu(button):
#    return top.open_box(contents)
#  return menu_button([caption, u'...'], open_menu)
#
#def menu(title, choices):
#  body = [urwid.Text(title, align='center'), urwid.Divider()]
#  body.extend(choices)
#  return urwid.ListBox(urwid.SimpleFocusListWalker(body))
#
#def item_chosen(button):
#  response = urwid.Text([u'You chose ', button.label, u'\n'])
#  done = menu_button(u'Ok', exit_program)
#  top.open_box(urwid.Filler(urwid.Pile([response, done])))
#
#def exit_program(button):
#  raise urwid.ExitMainLoop()
#
#menu_top = menu(TOP_PICTURE, [
#  sub_menu(u'Start game', [
#    menu_button(u'Pyramide', item_chosen),
#    menu_button(u'Square', item_chosen),
#    menu_button(u'Grove', item_chosen),
#    menu_button(u'Solitare', item_chosen),
#  ]),
#  menu_button(u'Manual', item_chosen),
#  menu_button(u'Exit', exit_program),
#])
#
#class CascadingBoxes(urwid.WidgetPlaceholder):
#  max_box_levels = 4
#
#  def __init__(self, box):
#    super(CascadingBoxes, self).__init__(urwid.SolidFill(u'/'))
#    self.box_level = 0
#    self.open_box(box)
#
#  def open_box(self, box):
#    self.original_widget = urwid.Overlay(urwid.LineBox(box),
#      self.original_widget,
#      align='center', width=('relative', 80),
#      valign='middle', height=('relative', 90),
#      min_width=24, min_height=8,
#      left=self.box_level * 3,
#      right=(self.max_box_levels - self.box_level - 1) * 3,
#      top=self.box_level * 2,
#      bottom=(self.max_box_levels - self.box_level - 1) * 2)
#    self.box_level += 1
#
#  def keypress(self, size, key):
#    if key == 'esc' and self.box_level > 1:
#      self.original_widget = self.original_widget[0]
#      self.box_level -= 1
#    else:
#      return super(CascadingBoxes, self).keypress(size, key)
#
#top = CascadingBoxes(menu_top)
#urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
#
