PALETTE = []
LIST_FOREGROUND_COLORS = (
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
LIST_BACKGROUND_COLORS = (
  'black',
  'dark red',
  'dark green',
  'brown',
  'dark blue',
  'dark magenta',
  'dark cyan',
  'light gray'
)

for fc in LIST_FOREGROUND_COLORS:
  for bc in LIST_BACKGROUND_COLORS:
    PALETTE.append(('%s_%s' % (fc, bc), fc, bc))

