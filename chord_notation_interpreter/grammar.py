from pprint import pprint

from chord_notation_interpreter.Instruments import Instruments
from chord_notation_interpreter.Transformer import EvalExpressions
from chord_notation_interpreter.Instrument import Instrument
from chord_notation_interpreter.NToneTemperament import NToneTemperament
from chord_notation_interpreter.SoundPlayer import SoundPlayer
from chord_notation_interpreter.utils import reader
from lark import Lark
from chord_notation_interpreter.error_handler import handle_errors

if __name__ == "__main__":
    grammar = reader("grammar.txt")
    chord_code = reader("test.txt")

    # chord code parser
    ccp = Lark(rf"{grammar}", start="start", parser="lalr", propagate_positions=True)

    # abstract syntax tree
    ast = ccp.parse(chord_code, on_error=handle_errors)
    ast2 = ast.copy()
    print(ast2.pretty())
    ev = EvalExpressions()
    xyz = ev.transform(ast2)

    if not set(ev.used_jump_numbers).issubset(ev.used_segno_numbers.keys()):
        ev.error_stack.append(f"Jump number mismatch")

    pprint(ev.error_stack)

    pprint(xyz)

    tet12 = NToneTemperament(n=12, freq=440, ratio=2)
    to_play = []
    for measure in xyz:
        for chord in measure.chords:
            ap = chord.chord_code + [chord.bass_note] if chord.bass_note else []
            ap = tet12.frequencies(ap)
            to_play.append((ap, chord.duration[0] / chord.duration[1]))

    inst = Instrument(Instruments.default)

    def generate_sound(chords_and_sound_fn):
        freq, duration = chords_and_sound_fn[0]
        print("Fd", freq, duration)
        sound_fn = chords_and_sound_fn[1]
        if len(freq.chord_code) == 0:
            return f"sleep({duration})"
        return Instrument(sound_fn).sound_from_frequencies(freq, duration)

    #
    args = [(chord, Instruments.organ) for chord in to_play]
    print(args)
    results = list(map(generate_sound, args))
    print(results)
    player = SoundPlayer(32, 48000)
    player.play(results, inst)


def run_playback(chord_code):
    grammar = reader("./chord_notation_interpreter/grammar.txt")
    ccp = Lark(rf"{grammar}", start="start", parser="lalr", propagate_positions=True)

    # abstract syntax tree
    ast = ccp.parse(chord_code, on_error=handle_errors)
    ast2 = ast.copy()
    print(ast2.pretty())
    ev = EvalExpressions()
    xyz = ev.transform(ast2)

    if not set(ev.used_jump_numbers).issubset(ev.used_segno_numbers.keys()):
        ev.error_stack.append(f"Jump number mismatch")

    pprint(ev.error_stack)

    pprint(xyz)

    tet12 = NToneTemperament(n=12, freq=440, ratio=2)
    to_play = []
    for measure in xyz:
        for chord in measure.chords:
            ap = chord.chord_code + [chord.bass_note] if chord.bass_note else []
            ap = tet12.frequencies(ap)
            to_play.append((ap, chord.duration[0] / chord.duration[1]))

    inst = Instrument(Instruments.default)

    def generate_sound(chords_and_sound_fn):
        freq, duration = chords_and_sound_fn[0]
        print("Fd", freq, duration)
        sound_fn = chords_and_sound_fn[1]
        if len(freq.chord_code) == 0:
            return f"sleep({duration})"
        return Instrument(sound_fn).sound_from_frequencies(freq, duration)

    #
    args = [(chord, Instruments.organ) for chord in to_play]
    print(args)
    results = list(map(generate_sound, args))
    print(results)
    player = SoundPlayer(32, 48000)
    player.play(results, inst)

    return (xyz, ev.error_stack)


# def measures_to_json(measures):
#     res = []

#     for measure in measures:
#         for chord in measure.chords:
