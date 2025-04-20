import math
import numpy as np
from time import time

from playback.Sound import Sound


class Instrument:
	def __init__(self, sound_fn, bits=16, sample_rate=44100):
		self.sound_fn = sound_fn
		self.bits = bits
		self.sample_rate = sample_rate
		self.amplitude = 2 ** (self.bits - 1) - 1


	def make_buf(self, numSamples, amplitude, freq):
		t = np.arange(numSamples) / self.sample_rate
		samples = self.sound_fn(amplitude, t, freq)

		# consider moving fade_duration, possibly making it a default arg
		fade_duration = 0.05
		fade_samples = int(fade_duration * self.sample_rate)
		if fade_samples > 0 and fade_samples < len(samples):
			# fade_curve = np.linspace(1.0, 0.0, fade_samples)
			fade_curve = 0.5 * (1 + np.cos(np.linspace(0, np.pi, fade_samples)))
			# fade_curve = np.exp(-np.linspace(0, 5, fade_samples))
			samples[-fade_samples:] = (samples[-fade_samples:] * fade_curve)

		buf = np.column_stack((samples, samples))
		return buf.astype(np.dtype(f"i{int(self.bits / 8)}"))

	def unite_buffers(self, buffers):
		new_buffer = np.stack(buffers)
		return np.mean(new_buffer, axis=0).astype(np.dtype(f"i{int(self.bits/8)}"))

	def sound_from_frequencies(self, ntt_fgroup, duration, runtime=[0]):
		start = time()
		num_samples = int(round(duration * self.sample_rate))

		frequencies = ntt_fgroup.frequencies

		if type(frequencies) == list:
			buffers = []
			for freq in frequencies:
				if type(freq) in [int, float, np.int8, np.float64]:
					buffers.append(self.make_buf(num_samples, self.amplitude, freq))
				else:
					raise TypeError("Frequency should be a number or a list of numbers")

			runtime[0] += time()-start
			print(f"runtime: {runtime}  |  current sound: {time()-start}")
			return Sound(self.unite_buffers(buffers), self.bits, self.sample_rate, duration)

		elif type(frequencies) in [int, float, np.int8]:
			runtime[0] += time()-start
			print(f"runtime: {runtime}  |  current sound: {time()-start}")
			return Sound(self.unite_buffers([self.make_buf(num_samples, self.amplitude, frequencies)]),
			             self.bits, self.sample_rate, duration)
		else:
			raise TypeError("Frequency should be a number or a list of numbers")