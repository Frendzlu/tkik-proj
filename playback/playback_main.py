import random

import numpy as np
import concurrent.futures

from time import time

from chord_notation_interpreter.Instruments import Instruments
from playback.Instrument import Instrument
from playback.NToneTemperament import NToneTemperament
from playback.SoundPlayer import SoundPlayer


def generate_sound(chords_and_sound_fn):
	freq, duration = chords_and_sound_fn[0]
	sound_fn = chords_and_sound_fn[1]
	return Instrument(sound_fn).sound_from_frequencies(freq, duration)


if __name__ == '__main__':
	tet12 = NToneTemperament(n=12, freq=440, ratio=2)
	aa = tet12.frequencies([-24, 0], 0)
	print(aa.frequencies)
	cmaj = tet12.frequencies([-21, -9, -5, -2], -21)
	fmaj = tet12.frequencies([-16, -9, -4, 0], -16)
	gmaj8 = tet12.frequencies([-14, -10, -7, -2], -14)
	gmaj7 = tet12.frequencies([-14, -10, -7, -4], -14)
	am = tet12.frequencies([-12, -9, -9, -5], -12)
	fmaj8 = tet12.frequencies([-16, -12, -9, -4], -16)
	fmaj6 = tet12.frequencies([-16, -12, -9, -7], -16)
	gmaj64 = tet12.frequencies([-14, -14, -9, -5], -14)
	gmaj53 = tet12.frequencies([-26, -16, -10, -7], -14)
	cmajno5 = tet12.frequencies([-21, -17, -9, -9], -21)

	inst = Instrument(Instruments.default)
	sound_from_freq_time = time()
	chords = [
		(cmaj, 1),
		(fmaj, 1),
		(gmaj8, 0.5),
		(gmaj7, 0.5),
		(am, 1),
		(fmaj8, 0.5),
		(fmaj6, 0.5),
		(gmaj64, 1),
		(gmaj53, 1),
		(cmajno5, 2)
	]

	# with concurrent.futures.ProcessPoolExecutor() as executor:
		# args =  [(chord, inst2) for chord in chords]
		# results = list(executor.map(generate_sound, args))

	args =  [(chord, Instruments.default) for chord in chords]
	results = list(map(generate_sound, args))
	print(f"sound from frequencies init time: {time()-sound_from_freq_time}")
	player = SoundPlayer(32, 48000)
	player.play(results, inst)

