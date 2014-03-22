import collections

from operator import itemgetter

def normalize_str_note(note, note_name='note'):
  if (note not in set('ABCDEFGabcdefg')):
      raise ValueError("'%s' must one of the following: A, B, C, D, E, F, G" % note_name)
  return note.upper()

def determine_step_difference(note_distances, start_note, end_note):
    start_note = normalize_str_note(start_note, 'start_note')
    end_note = normalize_str_note(end_note, 'end_note')

    if start_note == end_note:
      return 0

    if(start_note > end_note):
      invert = True
      (start_note, end_note) = (end_note, start_note)
    else:
      invert = False

    steps = 0
    current_note = start_note
    while current_note != end_note:
      row = next(x for x in note_distances if x[0] == current_note)
      steps = steps + row[2]
      current_note = row[1]

    if steps > 6:
      steps = steps - 12

    return steps * (-1 if invert else 1)

def generate_step_differences_table(note_distances):
  notes = map(lambda row: row[0], note_distances)

  table = collections.defaultdict(collections.defaultdict)
  for start_note in notes:
    for end_note in notes:
      table[start_note][end_note] = determine_step_difference(note_distances, start_note, end_note)

  return table

def generate_note_normalizations(step_differences):
  note_normalizations = dict()
  for start_note, other in step_differences.items():
    pairs = []
    for end_note, step in other.items():
      pairs.append((step, end_note))
      # 6 and -6 are the same, so make sure both are added
      if abs(step) == 6:
        pairs.append((-step, end_note))
    note_normalizations[start_note] = sorted(pairs)  
  return note_normalizations


NOTE_DISTANCES = (('A', 'B', 2), 
                 ('B', 'C', 1),
                 ('C', 'D', 2),
                 ('D', 'E', 2),
                 ('E', 'F', 1),
                 ('F', 'G', 2),
                 ('G', 'A', 2))

STEP_DIFFERENCES = generate_step_differences_table(NOTE_DISTANCES)

NOTE_NORMALIZATIONS = generate_note_normalizations(STEP_DIFFERENCES)

NOTES = ('A','B','C','D','E','F','G')

def generate_step_differences_as_table(step_differences):
  header = " " + "".join(["%5s" % n for n in NOTES])
  lines = [header]

  for start in NOTES:
    line= [start] + ["%5i"  % step_differences[start][end] for end in NOTES]
    lines.append("".join(line))
  return "\n".join(lines)


def determine_zero_offset_column_position(note_normalization):
  return [i for i,t in enumerate(note_normalization) if t[0] == 0][0]

def generate_note_normalizations_as_table(note_normalizations):
  max_columns_unto_zero_offset =   max(map(determine_zero_offset_column_position,note_normalizations.values()))

  lines = []
  for note in NOTES:
    padding_columns_to_add = max_columns_unto_zero_offset - determine_zero_offset_column_position(note_normalizations[note])
    padding = ("%8s" % "") * padding_columns_to_add
    
    line = [note,padding]
    for step,other_note in note_normalizations[note]:
      column = "%i=>%s"  % (step,other_note)
      line.append("%8s" % column)
    lines.append("".join(line))
  return "\n".join(lines)

class Semitone:
  def __init__(self,note,sharps=0,flats=0):
    self.note = normalize_str_note(note)
    self.sharps = sharps
    self.flats = flats

  def sharpen(self):
    if(self.flats > 0):
      return Semitone(self.note,sharps=self.sharps,flats=self.flats-1)      
    else:
      return Semitone(self.note,sharps=self.sharps+1,flats=self.flats)

  def flatten(self):
    if(self.sharps > 0):
      return Semitone(self.note,sharps=self.sharps-1,flats=self.flats)
    else:
      return Semitone(self.note,sharps=self.sharps,flats=self.flats+1)

  def normalize(self):
    if(self.flats > self.sharps):
      normalized_accidentals = Semitone(self.note,flats=((self.flats-self.sharps)%12))
    else:
      normalized_accidentals = Semitone(self.note,sharps=((self.sharps-self.flats)%12)) 
    
    if normalized_accidentals.sharps > 0:
      desired_step = normalized_accidentals.sharps-normalized_accidentals.flats
      
      possible_offsets = filter(lambda t: t[0] <= desired_step,NOTE_NORMALIZATIONS[normalized_accidentals.note])
      
      (offset,new_note) = max(possible_offsets,key=itemgetter(0))
      
      return Semitone(new_note,sharps=(normalized_accidentals.sharps-offset)) 
    else:
      desired_step = normalized_accidentals.flats-normalized_accidentals.sharps

      possible_offsets = filter(lambda t: t[0] >= -desired_step,NOTE_NORMALIZATIONS[normalized_accidentals.note])
      
      (offset,new_note) = min(possible_offsets,key=itemgetter(0))

      return Semitone(new_note,flats=(normalized_accidentals.flats- -offset)) 

  def as_note(self,note):
    note = normalize_str_note(note)
    difference = self.sharps - self.flats -  STEP_DIFFERENCES[self.note][note]
    if difference > 0:
      normalized_difference = difference % 12
      if normalized_difference > 6:
        normalized_difference = normalized_difference - 12
    elif difference < 0:
      normalized_difference = difference % -12
      if normalized_difference < -6:
        normalized_difference = normalized_difference + 12
    else:
      normalized_difference = difference

    if normalized_difference > 0:
      return Semitone(note,sharps=normalized_difference)
    elif normalized_difference < 0:
      return Semitone(note,flats=-normalized_difference)
    else:
      return Semitone(note)
      

  def __str__(self):
    return "%s%s%s" % (self.note,"#"*self.sharps,"b"*self.flats)

  def __repr__(self):
    return "Semitone(note='%s',sharps=%i,flats=%i)" % (self.note,self.sharps,self.flats)

  def is_same(self,other):
    if isinstance(other, Semitone):
      return self.note == other.note and self.sharps == other.sharps and self.flats == other.flats
    else:
      return False

  @property
  def is_natural(self):
    return self.flats == self.sharps

  @property
  def is_flat(self):
    return self.flats > self.sharps

  @property
  def is_sharp(self):
    return self.flats < self.sharps

  def __eq__(self, other):
      if isinstance(other, Semitone):
        return self.normalize().is_same(other.normalize())
      return NotImplemented

  def __ne__(self, other):
      result = self.__eq__(other)
      if result is NotImplemented:
          return result
      return not result

  def __sub__(self,other):
      base_difference = STEP_DIFFERENCES[other.note][self.note]
      accidental_difference = (self.sharps-other.sharps) - (self.flats-other.flats)
      return base_difference + accidental_difference

  @classmethod
  def from_string(cls,str):
    note = str[0]
    sharps = str[1:].count('#')
    flats = str[1:].count('b')
    return cls(note,sharps=sharps,flats=flats)

