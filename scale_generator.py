import collections

from semitone import Semitone

chord_descriptors = {
  'major': (2, 2, 1, 2, 2, 2, 1),
  'minor': (2, 1, 2, 2, 1, 2, 2)
}

tonal_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

class ScaleGenerator:

  def generate(self, root, type):
    current_semitone = Semitone.from_string(root)
    semi_tones = [current_semitone]

    for step_size in chord_descriptors[type]:
      for i in range(step_size):
        current_semitone = current_semitone.sharpen()
      semi_tones.append(current_semitone.normalize())
    scale = []
    ordered_tonal_notes = collections.deque(tonal_notes)
    ordered_tonal_notes.rotate(-tonal_notes.index(semi_tones[0].note))
    ordered_tonal_notes.append(ordered_tonal_notes[0])

    for note, semi_tone in zip(ordered_tonal_notes, semi_tones):
      scale.append(semi_tone.as_note(note))

    return tuple(map(str, scale))
