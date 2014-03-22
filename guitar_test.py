
import unittest
import guitar
from semitone import Semitone


class TestGuitar(unittest.TestCase):

    def test_locate_frets_for_semitone_on_string_should_work_for_open_note(self):
        instance = guitar.STANDARD_TUNING
        semitone = Semitone.from_string('E')
        expected_result = (0, 12)

        result = instance.locate_frets_for_semitone_on_string(0, semitone)

        self.assertEquals(result, expected_result)

    def test_locate_frets_for_semitone_on_string_should_work_for_non_open_note_sharper_than_open_note(self):
        instance = guitar.STANDARD_TUNING
        semitone = Semitone.from_string('C')
        expected_result = (8, 20)

        result = instance.locate_frets_for_semitone_on_string(0, semitone)

        self.assertEquals(result, expected_result)

    def test_locate_frets_for_semitone_on_string_should_work_for_non_open_note_flatter_than_open_note(self):
        instance = guitar.STANDARD_TUNING
        semitone = Semitone.from_string('G')
        expected_result = (3, 15)

        result = instance.locate_frets_for_semitone_on_string(0, semitone)

        self.assertEquals(result, expected_result)

    def test_locate_frets_for_semitone_on_standard_guitar(self):
        instance = guitar.STANDARD_TUNING
        semitone = Semitone.from_string('G')
        expected_result = ((3, 15), (10, 22), (5, 17),
                           (0, 12), (8, 20), (3, 15))
        result = instance.locate_frets_for_semitone(semitone)
        self.assertEquals(result, expected_result)


if __name__ == '__main__':
    unittest.main()
