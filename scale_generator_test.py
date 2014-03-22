import unittest
from scale_generator import ScaleGenerator
from semitone import Semitone


class TestScaleGenerator(unittest.TestCase):
    pass


def convert_to_semitones(scenario):
    root = Semitone.from_string(scenario[0])
    scale_type = scenario[1]
    expected_scale = tuple(map(Semitone.from_string, scenario[2]))
    return (root, scale_type, expected_scale)


scenarios = map(convert_to_semitones, [
    ('C', 'major', ('C', 'D', 'E', 'F', 'G', 'A', 'B', 'C')),
    ('C', 'minor', ('C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C')),
    ('A', 'major', ('A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A')),
    ('A', 'minor', ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'A')),
    ('E', 'major', ('E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E')),
    ('E', 'minor', ('E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E')),
    ('Fb', 'major', ('Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Eb', 'Fb')),
    ('Fb', 'minor', ('Fb', 'Gb', 'Abb', 'Bbb', 'Cb', 'Dbb', 'Ebb', 'Fb')),
    ('C#', 'major', ('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'C#')),
    ('C#', 'minor', ('C#', 'D#', 'E', 'F#', 'G#', 'A', 'B', 'C#')),
    ('A', 'harmonic-minor', ('A', 'B', 'C', 'D', 'E', 'F', 'G#', 'A')),
    ('C', 'melodic-minor', ('C', 'D', 'Eb', 'F', 'G', 'A', 'B', 'C'))
])


def create_test(root, scale_type, expected_scale):
    def do_test_expected(self):
        instance = ScaleGenerator()
        self.assertEqual(instance.generate(root, scale_type), expected_scale)
    return do_test_expected


def clean_root_for_test_name(root):

    if(root.is_flat):
        suffix = "_flat" * root.flats
    elif(root.is_sharp):
        suffix = "_sharp" * root.sharps
    else:
        suffix = ""

    return root.note + suffix

for root, scale_type, expected_scale in scenarios:
    test_method = create_test(root, scale_type, expected_scale)
    test_method.__name__ = 'test_generate_with_%s_type_and_root_%s_should_work' % (
        scale_type, clean_root_for_test_name(root))
    setattr(TestScaleGenerator, test_method.__name__, test_method)

if __name__ == '__main__':
    unittest.main()
