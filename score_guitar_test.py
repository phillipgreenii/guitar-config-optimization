import unittest
import guitar
from semitone import Semitone
from score_guitar import GuitarScorer


class TestGuitarScorer(unittest.TestCase):

    def test_score_with_standard_guitar_works(self):
        guitar_instance = guitar.Guitar(12, 1,
                                        tuple(
                                            map(Semitone.from_string, ('E', 'D', 'G' 'E'))),
                                        name='Test Tuning')

        instance = GuitarScorer()

        result = instance.score(guitar_instance)

        for scores in result:
            print "%(key_signature)-10s%(root)-3s\t%(count)5i\t%(min_score)3.2f\t%(25_percentile_score)3.2f\t%(mean_score)3.2f\t%(75_percentile_score)3.2f\t%(max_score)3.2f" % scores

        # TODO add assert

if __name__ == '__main__':
    unittest.main()
