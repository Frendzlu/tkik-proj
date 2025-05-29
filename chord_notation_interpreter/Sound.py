import time
import pygame


class Sound:
	duration = 1000

	def __init__(self, buf, bits, sample_rate, duration):
		self.buf = buf
		self.bits = bits
		self.sample_rate = sample_rate
		self.duration = duration