
import unittest
from score_guitar import score_chord


class TestGuitarScorerScoreChord(unittest.TestCase):
    pass

scenarios = [
    #chord, fingers, expected_score
    ((None, None, None, None, None, None), 4, 0.0),
    ((0, 0, 0, 0, 0, 0), 4, 1.0),
    ((None, 0, 0, 0, 0, 0), 4, 2.0),
    ((1, 0, 0, 0, 0, 0), 4, 1.5),
    ((1, 1, 0, 0, 0, 0), 4, 2.0),
    ((1, 1, 1, 0, 0, 0), 4, 2.5),
    ((1, 1, 1, 1, 0, 0), 4, 3.0),
    ((1, 2, 0, 0, 0, 0), 4, 2.0),
    ((1, 2, 3, 0, 0, 0), 4, 3.5),
    ((1, 2, 3, 4, 0, 0), 4, 5.0),
    ((1, 0, 2, 0, 3, 0), 4, 3.5),
    ((0, 1, 0, 2, 0, 3), 4, 3.5),
    ((1, 0, 2, 0, 3, 4), 4, 5.0),
    ((1, 1, 2, 2, 0, 0), 4, 3.0),
    ((1, 2, 3, 5, 0, 0), 4, 6.0),
    ((1, 3, 4, 6, 0, 0), 4, 7.0),
]


def create_test(chord, fingers, expected_score):
    def do_test_expected(self):
        result = score_chord(chord, fingers)
        self.assertEquals(result, expected_score)
    return do_test_expected


def format_chord_as_tab(chord):
    return "".join([("X" if f is None else str(f)) for f in chord])

for chord, fingers, expected_score in scenarios:
    test_method = create_test(chord, fingers, expected_score)
    test_method.__name__ = 'test_score_chord_with_%i_fingers_and_%s_should_work' % (
        fingers, format_chord_as_tab(chord))
    setattr(TestGuitarScorerScoreChord, test_method.__name__, test_method)

if __name__ == '__main__':
    unittest.main()
