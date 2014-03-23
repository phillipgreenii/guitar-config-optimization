from chord import ChordLocator
import itertools
import numpy
from semitone import Semitone
import chord as chord_utils


def string_product(*strings):
    return map(lambda v: "".join(v), itertools.product(*strings))


def score_chord(chord, fingers):
    # TODO note for scoring, finger span should be the scoring metric,
    # example: distance between notes: a major would be 2 while a minor would
    # be 3 there may need to be something extra for extra fret spans (5 or 6
    # should be the limit)
    # TODO should certain chords be modified by placement on the neck?

    strings_used = sum(chord_utils.determine_strings_used(chord))
    fret_span = chord_utils.fret_span(chord)
    all_strings_used = len(chord) == strings_used
    fingers_used = chord_utils.fingers_required(chord)
    score = 0.0
    if strings_used > 0:
        score += fingers_used / 2.0
        score += max((fret_span - 1), 0)
        score += 1 if all_strings_used else 2

    return score


class GuitarScorer:

    def __init__(self, fingers=4):
        self.key_signatures = ['major', 'minor']
        self.roots = map(Semitone.from_string,
                         string_product("ABCDEFG", ("", "b", "#")))
        self.fingers = fingers
        self._score_chord = lambda c: score_chord(c, self.fingers)

    def score(self, guitar):
        chord_locator = ChordLocator(guitar)

        scored_scales = []
        for key_signature in self.key_signatures:
            for root in self.roots:
                chord_scores = map(
                    self._score_chord,
                    chord_locator.locate(root, key_signature))
                (q0, q25, q50, q75, q100) = numpy.percentile(
                    chord_scores, [0, 25, 50, 75, 100])
                scored_scale = {'key_signature': key_signature,
                                'root': root,
                                'count': len(chord_scores),
                                'min_score': q0,
                                '25_percentile_score': q25,
                                'mean_score': q50,
                                '75_percentile_score': q75,
                                'max_score': q100}
                scored_scales.append(scored_scale)

        return scored_scales
