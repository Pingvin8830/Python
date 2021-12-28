import urwid

from graphs.menu import MainMenu, StartMenu
from graphs.forms import Pyramide, Grave, Solitare
from graphs.palette import PALETTE

class Game(urwid.MainLoop):
  def __init__(self):
    self.screen = MainMenu(self.choice_menu_item)
    super(Game, self).__init__(self.screen, PALETTE)
    self.default_unhandled_input = self.unhandled_input

  def run(self):
    super(Game, self).run()

  def choice_menu_item(self, button):
    choice = button.id
    if choice == 'Exit': raise urwid.ExitMainLoop()
    elif choice == 'Start game': self.widget = StartMenu(self.choice_menu_item)
    elif choice == 'Back': self.widget = MainMenu(self.choice_menu_item)
    else:
      self.unhandled_input = self.back_to_menu
      if choice == 'Pyramide': self.widget = Pyramide()
      elif choice == 'Grave': self.widget = Grave()
      elif choice == 'Solitare': self.widget = Solitare()
      else:
        self.unhandled_input = self.default_unhandled_input
        print('\n\n\n\n\n\n', button.id, '\n')

  def back_to_menu(self, key):
    if key == 'esc':
      self.widget = MainMenu(self.choice_menu_item)
      self.unhandled_input = self.default_unhandled_input
    elif key == 'q': raise urwid.ExitMainLoop()
    

