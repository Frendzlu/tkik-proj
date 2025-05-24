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
	_420ed69 = NToneTemperament(n=420, freq=440, ratio=69)
	tet12 = NToneTemperament(n=12, freq=440, ratio=2)
	tet31 = NToneTemperament(n=31, freq=440, ratio=2)

	cmaj = tet31.frequencies([0, 10, 18, 31])
	cmin = tet31.frequencies([0, 8, 18, 31])
	cneu = tet31.frequencies([0, 9, 18, 31])
	csmaj = tet31.frequencies([0, 11, 18, 31])
	csmin = tet31.frequencies([0, 7, 18, 31])

	inst = Instrument(Instruments.default)
	sound_from_freq_time = time()
	chords = [
		(cmin, 2),
		(cmaj, 2),
		(cneu, 2),
		(csmaj, 2),
		(csmin, 2),
	]

	# with concurrent.futures.ProcessPoolExecutor() as executor:
		# args =  [(chord, inst2) for chord in chords]
		# results = list(executor.map(generate_sound, args))

	args =  [(chord, Instruments.default) for chord in chords]
	results = list(map(generate_sound, args))
	print(f"sound from frequencies init time: {time()-sound_from_freq_time}")
	player = SoundPlayer(32, 48000)
	player.play(results, inst)

