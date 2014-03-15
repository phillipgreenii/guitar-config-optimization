import unittest
from semitone import determine_step_difference
import semitone

class SemitoneFunctionsDetermineStepDifferenceTest(unittest.TestCase):

  def test_determine_step_difference_with_start_note_longer_than_1_should_raise_value_error(self):
    self.assertRaises(ValueError,determine_step_difference,semitone.NOTE_DISTANCES,'Bb', 'C')

  def test_determine_step_difference_with_end_note_longer_than_1_should_raise_value_error(self):
    self.assertRaises(ValueError,determine_step_difference,semitone.NOTE_DISTANCES,'C', 'Bb')


  def test_determine_step_difference_with_invalid_start_note_should_raise_value_error(self):
    self.assertRaises(ValueError,determine_step_difference,semitone.NOTE_DISTANCES,'X', 'C')

  def test_determine_step_difference_with_invalid_end_note_should_raise_value_error(self):
    self.assertRaises(ValueError,determine_step_difference,semitone.NOTE_DISTANCES,'C', 'X')

  def test_determine_step_difference_with_empty_start_note_should_raise_value_error(self):
    self.assertRaises(ValueError,determine_step_difference,semitone.NOTE_DISTANCES,'', 'C')

  def test_determine_step_difference_with_empty_end_note_should_raise_value_error(self):
    self.assertRaises(ValueError,determine_step_difference,semitone.NOTE_DISTANCES,'C', '')

  def test_determine_step_difference_with_None_start_note_should_raise_value_error(self):
    self.assertRaises(ValueError,determine_step_difference,semitone.NOTE_DISTANCES,None, 'C')

  def test_determine_step_difference_with_None_end_note_should_raise_value_error(self):
    self.assertRaises(ValueError,determine_step_difference,semitone.NOTE_DISTANCES,'C', None)


scenarios = [
  ('A', 'A', 0),
  ('A', 'B', 2),
  ('A', 'C', 3),
  ('A', 'E', -5),
  ('A', 'G', -2),
  ('B', 'A', -2),
  ('C', 'A', -3),
  ('G', 'B', 4),
  ('E', 'F', 1),
  ('F', 'E', -1),
]

def create_test (start_note, end_note, expected_distance):
  def do_test_expected(self):
      self.assertEqual(determine_step_difference(semitone.NOTE_DISTANCES,start_note, end_note), expected_distance)
  return do_test_expected

def clean_root(root):
  if(len(root) > 1):
    root = root[0] + ('_sharp' if root[1] == '#' else '_flat')
  return root

for start_note, end_note, expected_distance in scenarios:
    test_method = create_test(start_note, end_note, expected_distance)
    test_method.__name__ = 'test_determine_step_difference_from_%s_to_%s_should_work' % (start_note, end_note)
    setattr (SemitoneFunctionsDetermineStepDifferenceTest, test_method.__name__, test_method)
  
  

if __name__ == '__main__':
    unittest.main()