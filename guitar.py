from semitone import Semitone


class Guitar:

    def __init__(self, fret_count, fret_spacing, open_string_semitones,
                 name=None):
        self.fret_count = fret_count
        self.fret_spacing = fret_spacing
        self.open_string_semitones = open_string_semitones
        self.name = name

    def locate_frets_for_semitone(self, semitone):
        return tuple(
            map(lambda i: self.locate_frets_for_semitone_on_string(i, semitone),
                range(len(self.open_string_semitones))))

    def locate_frets_for_semitone_on_string(self, string, semitone):
        open_note = self.open_string_semitones[string]
        offset = semitone - open_note
        if offset < 0:
            offset += 12

        frets = []
        while offset < self.fret_count:
            frets.append(offset)
            offset += 12 / self.fret_spacing

        return tuple(frets)

    def __str__(self):
        return self.name if self.name else "Guitar:%i;%s;%s" % (self.fret_count, self.fret_spacing, self.open_string_semitones)

STANDARD_TUNING = Guitar(24, 1, tuple(
    map(Semitone.from_string, ('E', 'A', 'D', 'G', 'B', 'E'))), name='Standard Tuning')
