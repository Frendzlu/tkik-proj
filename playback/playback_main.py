import numpy as np
import concurrent.futures

from time import time
from playback.Instrument import Instrument
from playback.NToneTemperament import NToneTemperament
from playback.SoundPlayer import SoundPlayer


def inst2(amp, t, freq):
	harmonics = [
        1.0,
        1.0,
        0.1,
        0.2,
        0.15,
        0.05,
        0.025,
        0.025
    ]
	res = np.zeros_like(t, dtype=np.float32)
	for i, w in enumerate(harmonics, start=1):
		res += w * np.sin(2 * np.pi * freq * i * t) 

	res = amp * res / sum(harmonics)
	return np.round(res).astype(np.int16)


def generate_sound(chords_and_sound_fn):
	freq, duration = chords_and_sound_fn[0]
	sound_fn = chords_and_sound_fn[1]
	inst = Instrument(sound_fn)
	return inst.sound_from_frequencies(freq, duration)


if __name__ == '__main__':
	tet12 = NToneTemperament(n=12, freq=420)
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

	inst = Instrument(inst2)
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

	args =  [(chord, inst2) for chord in chords]
	results = list(map(generate_sound, args))
	print(f"sound from frequencies init time: {time()-sound_from_freq_time}")
	player = SoundPlayer(16, 44100)
	player.play(results, inst)