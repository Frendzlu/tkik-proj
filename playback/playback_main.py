import random

import numpy as np
import concurrent.futures

from time import time
from playback.Instrument import Instrument
from playback.NToneTemperament import NToneTemperament
from playback.SoundPlayer import SoundPlayer


def flute(amp, t, freq):
	harmonics = [
		[1, 2],
		[0.9, 3],
		[0.5, 4],
		[0.4, 5],
		[0.4, 6],
		[0.3, 7],
		[0.2, 8],
		[0.1, 9],
	]
	res = np.zeros_like(t, dtype=np.float32)
	for i in range(len(harmonics)):
		harmonics.append([
			harmonics[i][0],
			harmonics[i][1] + ((random.random() - 0.5) / 67)
		])
		harmonics.append([
			harmonics[i][0],
			harmonics[i][1] + ((random.random() - 0.5) / 156)
		])
		harmonics.append([
			harmonics[i][0],
			harmonics[i][1] + ((random.random() - 0.5) / 49)
		])

	w_sum = 0
	for [w, m] in harmonics:
		# print(w, m)
		res += w * np.sin(2 * np.pi * freq * m * t)
		w_sum += w


	res = amp * res / w_sum
	return np.round(res).astype(np.int16)


def generate_sound(chords_and_sound_fn):
	freq, duration = chords_and_sound_fn[0]
	sound_fn = chords_and_sound_fn[1]
	return Instrument(sound_fn).sound_from_frequencies(freq, duration)


if __name__ == '__main__':
	tet12 = NToneTemperament(n=12, freq=420, ratio=2)
	high_c = tet12.frequencies(3)
	cmaj = tet12.frequencies([-21, -9, -5, -2])
	fmaj = tet12.frequencies([-16, -9, -4, 0])
	gmaj8 = tet12.frequencies([-14, -10, -7, -2])
	gmaj7 = tet12.frequencies([-14, -10, -7, -4])
	am = tet12.frequencies([-12, -9, -9, -5])
	fmaj8 = tet12.frequencies([-16, -12, -9, -4])
	fmaj6 = tet12.frequencies([-16, -12, -9, -7])
	gmaj64 = tet12.frequencies([-14, -14, -9, -5])
	gmaj53 = tet12.frequencies([-26, -16, -10, -7])
	cmajno5 = tet12.frequencies([-21, -17, -9, -9])

	inst = Instrument(flute)
	sound_from_freq_time = time()
	chords = [
		(high_c, 5),
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

	args =  [(chord, flute) for chord in chords]
	results = list(map(generate_sound, args))
	print(f"sound from frequencies init time: {time()-sound_from_freq_time}")
	player = SoundPlayer(32, 48000)
	player.play(results, inst)