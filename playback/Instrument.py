import math
import numpy as np

from playback.Sound import Sound


class Instrument:
	def __init__(self, sound_fn, bits=16, sample_rate=44100):
		self.sound_fn = sound_fn
		self.bits = bits
		self.sample_rate = sample_rate
		self.amplitude = 2 ** (self.bits - 1) - 1

	def make_buf(self, numSamples, amplitude, freq):
		buf = np.arange(numSamples, dtype=np.dtype(f"i{int(self.bits/8)}"))
		return list(map(lambda s: [
			self.sound_fn(amplitude, float(s) / self.sample_rate, freq),
			self.sound_fn(amplitude, float(s) / self.sample_rate, freq)
		], buf))

	def unite_buffers(self, buffers, num_samples):
		new_buffer = np.zeros((num_samples, 2), dtype=np.dtype(f"i{int(self.bits / 8)}"))
		for buf in buffers:
			for i in range(num_samples):
				new_buffer[i][0] += buf[i][0] / len(buffers)
				new_buffer[i][1] += buf[i][1] / len(buffers)
		return new_buffer

	def sound_from_frequencies(self, frequencies, duration):
		num_samples = int(round(duration * self.sample_rate))
		if type(frequencies) == list:
			buffers = []
			for freq in frequencies:
				if type(freq) in [int, float]:
					buffers.append(self.make_buf(num_samples, self.amplitude, freq))
				else:
					raise TypeError("Frequency should be a number or a list of numbers")

			return Sound(self.unite_buffers(buffers, num_samples), self.bits, self.sample_rate, duration)

		elif type(frequencies) in [int, float]:
			return Sound(self.unite_buffers([self.make_buf(num_samples, self.amplitude, frequencies)], num_samples),
			             self.bits, self.sample_rate, duration)
		else:
			raise TypeError("Frequency should be a number or a list of numbers")