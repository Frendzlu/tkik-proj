from chord_notation_interpreter.Chord import Chord


class Measure:
    def __init__(self, chords, subdiv=4, time_signature=(4, 4), segno_number=None, suffix=None):
        self.error_stack = []
        self.chords: list[Chord] = chords
        self.subdiv = subdiv
        self.time_signature = time_signature
        ratio = subdiv / time_signature[1]
        exp_len = time_signature[0]
        real_len = 0

        for chord in self.chords:
            duration, sdiv = chord.duration
            real_len += (duration / sdiv) / ratio

        if abs(real_len - exp_len) > 0.001:
            self.error_stack.append(f"Measure length mismatch: {real_len} != {exp_len}")
