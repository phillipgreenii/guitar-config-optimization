
import unittest
import guitar
from chord import ChordLocator
from semitone import Semitone


class TestChordLocator(unittest.TestCase):

    def test_locate_should_generate_open_d_major_chord(self):
        instance = ChordLocator(guitar.STANDARD_TUNING)

        semitone = Semitone.from_string('D')
        open_chord = (None, None, 0, 2, 3, 2)

        result = instance.locate(semitone, 'major')

        self.assertIn(open_chord, result)

    def test_locate_should_generate_open_g_major_chord(self):
        instance = ChordLocator(guitar.STANDARD_TUNING)

        semitone = Semitone.from_string('G')
        open_chord = (3, 2, 0, 0, 0, 3)

        result = instance.locate(semitone, 'major')
        
        self.assertIn(open_chord, result)

if __name__ == '__main__':
    unittest.main()
