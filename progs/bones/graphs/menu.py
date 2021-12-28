import urwid

from graphs.widgets import MenuItem, TitleDivider, TitlePicture, Title

class Menu(urwid.Filler):
  def __init__(self, list_items, title):
    list_widgets = [
      TitlePicture(),
      TitleDivider(),
      Title(title),
      TitleDivider(),
    ] + list_items
    pile = urwid.Pile(list_widgets)
    super(Menu, self).__init__(pile)

class MainMenu(Menu):
  def __init__(self, callback):
    list_items = [
      MenuItem('Start game', 'Начать игру', callback),
      MenuItem('Settings', 'Настройки', callback),
      MenuItem('Manual', 'Правила', callback),
      MenuItem('Exit', 'Выход', callback)
    ]
    super(MainMenu, self).__init__(list_items, 'Домино-пасьянс')

class StartMenu(Menu):
  def __init__(self, callback):
    list_items = [
      MenuItem('Pyramide', 'Пирамида', callback),
      MenuItem('Square', 'Квадрат', callback),
      MenuItem('Grave', 'Могила', callback),
      MenuItem('Solitare', 'Солитер', callback),
      MenuItem('Back', 'Назад', callback)
    ]
    super(StartMenu, self).__init__(list_items, 'Начать игру. Выберите форму:')

