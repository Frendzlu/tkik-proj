from Instruments import Instruments
from Transformer import EvalExpressions
from Instrument import Instrument
from NToneTemperament import NToneTemperament
from SoundPlayer import SoundPlayer
from utils import reader
from lark import Lark
from error_handler import handle_errors

if __name__ == "__main__":
    grammar = reader("grammar.txt")
    chord_code = reader("./cc.txt")

    # chord code parser
    ccp = Lark(rf"{grammar}", start="start", parser='lalr')

    # abstract syntax tree
    ast = ccp.parse(chord_code,  on_error=handle_errors)
    ast2 = ast.copy()
    print(ast2.pretty())
    xyz = EvalExpressions().transform(ast2).children

    tet12 = NToneTemperament(n=12, freq=440, ratio=2)
    to_play = []
    for measure in xyz:
        for chord in measure:
            ap = chord.chord_code + [chord.bass_note] if chord.bass_note else []
            ap = tet12.frequencies(ap)
            to_play.append((ap, chord.duration[0]/chord.duration[1]))

    inst = Instrument(Instruments.default)


    def generate_sound(chords_and_sound_fn):
        freq, duration = chords_and_sound_fn[0]
        print("Fd", freq, duration)
        sound_fn = chords_and_sound_fn[1]
        return Instrument(sound_fn).sound_from_frequencies(freq, duration)

    args = [(chord, Instruments.default) for chord in to_play]
    print(args)
    results = list(map(generate_sound, args))
    print(to_play)
    player = SoundPlayer(32, 48000)
    player.play(results, inst)





