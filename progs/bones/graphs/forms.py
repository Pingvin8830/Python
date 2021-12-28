import urwid

from graphs.widgets import BoneButton

class Form(urwid.Filler):
  def __init__(self):
    self.list_buttons = []
    for i in range(28): self.list_buttons.append(BoneButton())

  def init_filler(self, widget):
    super(Form, self).__init__(widget)

class Pyramide(Form):
  def __init__(self):
    super(Pyramide, self).__init__()
    lines = [
      urwid.Padding(
        urwid.Columns([
            self.list_buttons[0]
        ]), width=13, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[1],
          self.list_buttons[2]
        ]), width=27, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[3],
          self.list_buttons[4],
          self.list_buttons[5]
        ]), width=41, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[6],
          self.list_buttons[7],
          self.list_buttons[8],
          self.list_buttons[9]
        ]), width=55, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[10],
          self.list_buttons[11],
          self.list_buttons[12],
          self.list_buttons[13],
          self.list_buttons[14]
        ]), width=69, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[15],
          self.list_buttons[16],
          self.list_buttons[17],
          self.list_buttons[18],
          self.list_buttons[19],
          self.list_buttons[20]
        ]), width=83, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[21],
          self.list_buttons[22],
          self.list_buttons[23],
          self.list_buttons[24],
          self.list_buttons[25],
          self.list_buttons[26],
          self.list_buttons[27]
        ]), width=97, align='center'
      ),
    ]
    pile = urwid.Pile(lines)
    self.init_filler(pile)

class Grave(Form):
  def __init__(self):
    super(Grave, self).__init__()
    for i in (0, 3, 7): self.list_buttons[i].rotate()
    lines = [
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[0]
        ]), width=7, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[1],
          self.list_buttons[2]
        ]), width=27, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[3]
        ]), width=7, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[4],
          self.list_buttons[5],
          self.list_buttons[6]
        ]), width=41, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[7]
        ]), width=7, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[8],
          self.list_buttons[9]
        ]), width=27, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[10],
          self.list_buttons[11],
          self.list_buttons[12]
        ]), width=41, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[13],
          self.list_buttons[14],
          self.list_buttons[15],
          self.list_buttons[16]
        ]), width=55, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[17],
          self.list_buttons[18],
          self.list_buttons[19],
          self.list_buttons[20],
          self.list_buttons[21]
        ]), width=69, align='center'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[22],
          self.list_buttons[23],
          self.list_buttons[24],
          self.list_buttons[25],
          self.list_buttons[26],
          self.list_buttons[27]
        ]), width=83, align='center'),
    ]
    pile = urwid.Pile(lines)
    self.init_filler(pile)

class Solitare(Form):
  def __init__(self):
    super(Solitare, self).__init__()
    lines = [
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[0],
          self.list_buttons[1],
          self.list_buttons[2],
          self.list_buttons[3],
          self.list_buttons[4],
          self.list_buttons[5],
          self.list_buttons[6]
        ]), width=97, align='right'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[7],
          self.list_buttons[8],
          self.list_buttons[9],
          self.list_buttons[10],
          self.list_buttons[11],
          self.list_buttons[12]
        ]), width=83, align='right'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[13],
          self.list_buttons[14],
          self.list_buttons[15],
          self.list_buttons[16],
          self.list_buttons[17]
        ]), width=69, align='right'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[18],
          self.list_buttons[19],
          self.list_buttons[20],
          self.list_buttons[21]
        ]), width=55, align='right'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[22],
          self.list_buttons[23],
          self.list_buttons[24]
        ]), width=41, align='right'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[25],
          self.list_buttons[26]
        ]), width=27, align='right'
      ),
      urwid.Padding(
        urwid.Columns([
          self.list_buttons[27]
        ]), width=13, align='right'
      )
    ]
    pile = urwid.Pile(lines)
    filler = urwid.Filler(pile)
    self.init_filler(pile)

