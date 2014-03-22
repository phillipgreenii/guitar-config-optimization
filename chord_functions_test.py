
import unittest
import guitar
from chord import generate_chord_combinations
from chord import is_split_chord
from chord import fingers_required
from chord import fret_span
from semitone import Semitone


class TestChordFunctions(unittest.TestCase):

    def test_generate_chord_combinations_should_generate_all_possibilities_when_zero_strings(self):
        frets_per_string_by_type = ()

        expected_result = ()

        result = tuple(generate_chord_combinations(frets_per_string_by_type))

        self.assertEquals(result, expected_result)

    def test_generate_chord_combinations_should_generate_all_possibilities_when_one_string(self):
        string_one = ((0, 2), (4, 6), (8, 10))
        frets_per_string_by_type = (string_one,)

        expected_result = ((None,), (0,), (2,), (4,), (6,), (8,), (10,))

        result = tuple(generate_chord_combinations(frets_per_string_by_type))

        self.assertEquals(result, expected_result)

    def test_generate_chord_combinations_should_generate_all_possibilities_when_two_string(self):
        string_one = ((1, 3), (5, 7), (9, 11))
        string_two = ((0, 2), (4, 6), (8, 10))
        frets_per_string_by_type = (string_one, string_two)

        expected_result = ((None, None),
                           (None, 0),
                           (None, 2),
                           (None, 4),
                           (None, 6),
                           (None, 8),
                           (None, 10),
                           (1, None),
                           (1, 0),
                           (1, 2),
                           (1, 4),
                           (1, 6),
                           (1, 8),
                           (1, 10),
                           (3, None),
                           (3, 0),
                           (3, 2),
                           (3, 4),
                           (3, 6),
                           (3, 8),
                           (3, 10),
                           (5, None),
                           (5, 0),
                           (5, 2),
                           (5, 4),
                           (5, 6),
                           (5, 8),
                           (5, 10),
                           (7, None),
                           (7, 0),
                           (7, 2),
                           (7, 4),
                           (7, 6),
                           (7, 8),
                           (7, 10),
                           (9, None),
                           (9, 0),
                           (9, 2),
                           (9, 4),
                           (9, 6),
                           (9, 8),
                           (9, 10),
                           (11, None),
                           (11, 0),
                           (11, 2),
                           (11, 4),
                           (11, 6),
                           (11, 8),
                           (11, 10))

        result = tuple(generate_chord_combinations(frets_per_string_by_type))

        self.assertEquals(result, expected_result)

    def test_is_split_chord_should_return_false_if_skipped_strings_are_on_bottom_strings(self):
        frets = (None, None, 3, 4, 5, 6)

        result = is_split_chord(frets)

        self.assertFalse(result)

    def test_is_split_chord_should_return_false_if_skipped_strings_are_on_top_strings(self):
        frets = (1, 2, 3, 4, None, None)

        result = is_split_chord(frets)

        self.assertFalse(result)

    def test_is_split_chord_should_return_false_if_all_strings_are_skipped(self):
        frets = (None, None, None, None, None, None)

        result = is_split_chord(frets)

        self.assertFalse(result)

    def test_is_split_chord_should_return_false_if_no_strings_are_skipped(self):
        frets = (1, 2, 3, 4, 5, 6)

        result = is_split_chord(frets)

        self.assertFalse(result)

    def test_is_split_chord_should_return_false_if_skipped_strings_on_top_and_bottom(self):
        frets = (None, None, 3, 4, 5, None)

        result = is_split_chord(frets)

        self.assertFalse(result)

    def test_is_split_chord_should_return_true_if_is_split_chord_in_the_middle(self):
        frets = (None, 2, None, 4, None, None)

        result = is_split_chord(frets)

        self.assertTrue(result)

    def test_fingers_required_should_not_count_None(self):
        frets = (None, 2, 3, 4, 5, 6)

        expected_result = 5
        result = fingers_required(frets)

        self.assertEquals(result, expected_result)

    def test_fingers_required_should_not_count_open(self):
        frets = (0, 2, 3, 4, 5, 0)

        expected_result = 4
        result = fingers_required(frets)

        self.assertEquals(result, expected_result)

    def test_fingers_required_should_count_frets(self):
        frets = (1, 2, 3, 4, 5, 6)

        expected_result = 6
        result = fingers_required(frets)

        self.assertEquals(result, expected_result)

    def test_fret_span_should_return_zero_for_only_one_played_strings(self):
        frets = (1, None, None, None, None, None)

        expected_result = 0
        result = fret_span(frets)

        self.assertEquals(result, expected_result)

    def test_fret_span_should_return_zero_for_only_one_fret(self):
        frets = (1, 1, 1, 1, 1, 1)

        expected_result = 0
        result = fret_span(frets)

        self.assertEquals(result, expected_result)

    def test_fret_span_should_return_zero_for_all_unplayed_strings(self):
        frets = (None, None, None, None, None, None)

        expected_result = 0
        result = fret_span(frets)

        self.assertEquals(result, expected_result)

    def test_fret_span_should_not_count_open_notes(self):
        frets = (0, 1, 1, 2, 2, 3)

        expected_result = 2
        result = fret_span(frets)

        self.assertEquals(result, expected_result)

    def test_fret_span_should_not_count_unplayed_strings(self):
        frets = (None, 2, 3, 4, None, None)

        expected_result = 2
        result = fret_span(frets)

        self.assertEquals(result, expected_result)

    def test_fret_span_should_count_played_strings(self):
        frets = (2, 2, 3, 3, 5, 5)

        expected_result = 3
        result = fret_span(frets)

        self.assertEquals(result, expected_result)

if __name__ == '__main__':
    unittest.main()
