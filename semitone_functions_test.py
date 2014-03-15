import unittest
import semitone

class SemitoneFunctionsTest(unittest.TestCase):

  def test_generate_step_differences_as_table_should_generate_correct_table(self):
    expected_table ="""
     A    B    C    D    E    F    G
A    0    2    3    5   -5   -4   -2
B   -2    0    1    3    5    6   -4
C   -3   -1    0    2    4    5   -5
D   -5   -3   -2    0    2    3    5
E    5   -5   -4   -2    0    1    3
F    4   -6   -5   -3   -1    0    2
G    2    4    5   -5   -3   -2    0
""".strip('\n')
    actual_table = semitone.generate_step_differences_as_table(semitone.STEP_DIFFERENCES)
    self.assertEquals(actual_table,expected_table)


  def test_determine_zero_offset_column_position(self):
    note_normalization = [(-5, 'D'), (-3, 'E'), (-2, 'F'), (0, 'G'), (2, 'A'), (4, 'B'), (5, 'C')]

    expected_offset = 3
    result = semitone.determine_zero_offset_column_position(note_normalization)

    self.assertEquals(result, expected_offset)


  def test_generate_note_normalizations_as_table_should_generate_correct_table(self):
    expected_table ="""
A           -5=>E   -4=>F   -2=>G    0=>A    2=>B    3=>C    5=>D
B           -6=>F   -4=>G   -2=>A    0=>B    1=>C    3=>D    5=>E    6=>F
C           -5=>G   -3=>A   -1=>B    0=>C    2=>D    4=>E    5=>F
D           -5=>A   -3=>B   -2=>C    0=>D    2=>E    3=>F    5=>G
E           -5=>B   -4=>C   -2=>D    0=>E    1=>F    3=>G    5=>A
F   -6=>B   -5=>C   -3=>D   -1=>E    0=>F    2=>G    4=>A    6=>B
G           -5=>D   -3=>E   -2=>F    0=>G    2=>A    4=>B    5=>C
""".strip('\n')
    actual_table = semitone.generate_note_normalizations_as_table(semitone.NOTE_NORMALIZATIONS)
    self.assertEquals(actual_table,expected_table)

if __name__ == '__main__':
    unittest.main()