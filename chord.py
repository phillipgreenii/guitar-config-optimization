from scale_generator import ScaleGenerator
import itertools


def generate_chord_combinations(frets_per_string_by_type):
    if len(frets_per_string_by_type) == 0:
        return ()

    def flatten(l):
        return [item for sublist in l for item in sublist]

    def add_none(l):
        return [None] + l
    frets_per_string = map(add_none, map(flatten, frets_per_string_by_type))
    return itertools.product(*frets_per_string)


def determine_strings_used(chord):
    return map(lambda n: n is not None, chord)


def is_split_chord(chord):
    string_used = determine_strings_used(chord)

    def determine_descriptor(state, cur):
        (prev, desc) = state

        if cur != prev:
            # X for unused
            # N for used
            desc += ("N" if cur else "X")

        return (cur, desc)

    (previous, descriptor) = reduce(
        determine_descriptor, string_used, (None, ""))

    # NXN means split
    return "NXN" in descriptor


def fingers_required(chord):
    # only count strings used (not None) with frets more than 0 (open)
    return len(filter(lambda n: n is not None and n > 0, chord))


def fret_span(chord):
    played_frets = filter(lambda s: s is not None and s > 0, chord)
    if len(played_frets) <= 0:
        return 0
    else:
        return max(played_frets) - min(played_frets)


class ChordLocator:

    def __init__(self, guitar):
        self.guitar = guitar
        self.scale_generator = ScaleGenerator()

    def locate(self, root, type, fingers=4, minimum_notes_for_chord=3, maximum_fret_span=8):
        scale = self.scale_generator.generate(root, type)

        (base, third, fifth) = (scale[0], scale[2], scale[4])

        (base_frets, third_frets, fifth_frets) = map(
            self.guitar.locate_frets_for_semitone, (base, third, fifth))

        frets_per_string_by_type = zip(*(base_frets, third_frets, fifth_frets))

        def is_valid_chord(c):
            return sum(determine_strings_used(c)) >= minimum_notes_for_chord \
                and fingers_required(c) <= fingers \
                and fret_span(c) <= maximum_fret_span\
                and not is_split_chord(c)

        # limit number of strings to number of fingers
        chords = filter(is_valid_chord,
                        generate_chord_combinations(frets_per_string_by_type))

        return tuple(chords)

# frets will be tuple of guitar sting frets

# TODO note for scoring, finger span should be the scoring metric,
# example: distance between notes: a major would be 2 while a minor would
# be 3 there may need to be something extra for extra fret spans (5 or 6
# should be the limit)
