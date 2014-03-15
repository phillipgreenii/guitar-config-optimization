import unittest
from scale_generator import ScaleGenerator


class TestScaleGenerator(unittest.TestCase):
  pass

scenarios = [
  ('C', 'major', ('C', 'D', 'E', 'F', 'G', 'A', 'B', 'C')),
  ('C', 'minor', ('C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C')),
  ('A', 'major', ('A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A')),
  ('A', 'minor', ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'A')),
  ('E', 'major', ('E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E')),
  ('E', 'minor', ('E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E')),
  ('Fb', 'major', ('Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Eb', 'Fb')),
  ('Fb', 'minor', ('Fb', 'Gb', 'Abb', 'Bbb', 'Cb', 'Dbb', 'Ebb', 'Fb')),
  ('C#', 'major', ('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'C#')),
  ('C#', 'minor', ('C#', 'D#', 'E', 'F#', 'G#', 'A', 'B', 'C#'))
]

def create_test(root, scale_type, expected_scale):
  def do_test_expected(self):
      instance = ScaleGenerator()
      self.assertEqual(instance.generate(root, scale_type), expected_scale)
  return do_test_expected

def clean_root_for_test_name(root):
  if(len(root) > 1):
    root = root[0] + ('_sharp' if root[1] == '#' else '_flat')
  return root

for root, scale_type, expected_scale in scenarios:
    test_method = create_test(root, scale_type, expected_scale)
    test_method.__name__ = 'test_generate_with_%s_type_and_root_%s_should_work' % (scale_type, clean_root_for_test_name(root))
    setattr (TestScaleGenerator, test_method.__name__, test_method)

if __name__ == '__main__':
    unittest.main()
