class Guitar:
  def __init__(self, fret_count, fret_spacing, open_string_notes, name=None):
    self.fret_count = fret_count
    self.fret_spacing = fret_spacing
    self.open_string_notes = open_string_notes
    self.name = name

  def __str__(self):
    return self.name if self.name else "Guitar:%i;%s;%s" % (self.fret_count, self.fret_spacing, self.open_string_notes)

STANDARD_TUNING = Guitar(24, 1, ('E', 'A', 'D', 'G', 'B', 'E'), name='Standard Tuning')
