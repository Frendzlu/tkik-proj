import numpy as np


def construct_instrument(harmonics=((1, 1),)):

	def _t(amp, t, freq):
		res = np.zeros_like(t, dtype=np.float32)

		w_sum = 0
		for [w, m] in harmonics:
			# print(w, m)
			res += w * np.sin(2 * np.pi * freq * m * t)
			w_sum += w

		res = amp * res / w_sum
		return np.round(res).astype(np.int16)

	return _t

class Instruments:
	default = construct_instrument()
	organ = construct_instrument([
		[1, 1],
		[1, 2],
		[0.8, 3],
		[0.5, 4],
		[0.3, 5],
		[0.2, 6],
		[0.1, 7],
		[0.1, 8],
	])