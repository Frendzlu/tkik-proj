import math
import time

import numpy
import pygame


class Sound:
	def __init__(self, frequency, duration=1):
		pygame.init()
		bits = 16
		sample_rate = 44100
		pygame.mixer.pre_init(sample_rate, bits)

		num_samples = int(round(duration * sample_rate))
		self.frequency = frequency
		self.duration = duration
		self.num_samples = num_samples
		amplitude = 2 ** (bits - 1) - 1

		self.buf = list(map(lambda s: [
			self.sine(amplitude, float(s)/sample_rate),
			self.sine(amplitude, float(s) / sample_rate)
		], numpy.arange(num_samples, dtype=numpy.int16)))

		self.buf = numpy.array(self.buf, dtype=numpy.int16)

	def sine(self, amp, t):
		return int(round(amp * math.sin(2 * math.pi * self.frequency * t)))

	def play(self):
		sound = pygame.sndarray.make_sound(self.buf)
		sound.play(loops=1, maxtime=int(self.duration * 1000))
		time.sleep(self.duration)
