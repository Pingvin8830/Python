import urwid

from graphs.pictures import BONE_PICTURE, TOP_PICTURE

class TitlePicture(urwid.Padding):
  def __init__(self):
    self.color = 'brown_dark red'
    text = urwid.Text(TOP_PICTURE, align='center')
    attr_map = urwid.AttrMap(text, self.color)
    super(TitlePicture, self).__init__(attr_map, width=63, align='center')

class TitleDivider(urwid.Padding):
  def __init__(self):
    self.color = 'brown_dark magenta'
    divider = urwid.Divider('─')
    attr_map = urwid.AttrMap(divider, self.color)
    super(TitleDivider, self).__init__(attr_map, width=63, align='center')

class Title(urwid.Padding):
  def __init__(self, title):
    self.color = 'brown_dark magenta'
    text = urwid.Text(title, align='center')
    attr_map = urwid.AttrMap(text, self.color)
    super(Title, self).__init__(attr_map, width=63, align='center')

class MenuItem(urwid.Button):
  def __init__(self, id, text, callback):
    self.colors = {
      'nofocus': 'dark blue_dark cyan',
      'focus': 'dark cyan_dark blue'
    }
    self.id = id
    super(MenuItem, self).__init__("")
    if callback: urwid.connect_signal(self, 'click', callback)
    self._w = urwid.Padding(
      urwid.AttrMap(
        urwid.SelectableIcon(text),
        self.colors['nofocus'],
        self.colors['focus']
      ),
      width=63,
      align='center'
    )

class BoneButton(urwid.Button):
  def __init__(self):
    self.colors = {
      'nofocus': 'brown_black',
      'focus': 'black_brown'
    }
    self.orientation = 'horizontal'
    self.width = 13
    super(BoneButton, self).__init__("")
    self._w = urwid.Padding(
      urwid.AttrMap(
        urwid.SelectableIcon(BONE_PICTURE[self.orientation]),
        self.colors['nofocus'],
        self.colors['focus']
      ),
      width=self.width
    )

  def rotate(self):
    if self.orientation == 'horizontal':
      self.orientation = 'vertical'
      self.width = 7
      self._w = urwid.Padding(
        urwid.AttrMap(
          urwid.SelectableIcon(BONE_PICTURE[self.orientation]),
          self.colors['nofocus'],
          self.colors['focus']
        ),
        width=self.width
      )
    else:
      self.orientation = 'horizontal'
      self.width = 13
      self._w = urwid.Padding(
        urwid.AttrMap(
          urwid.SelectableIcon(BONE_PICTURE[self.orientation]),
          self.colors['nofocus'],
          self.colors['focus']
        ),
        width=self.widht
      )

