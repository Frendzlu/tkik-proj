import time
import pygame


class Sound:
	def __init__(self, buf, bits, sample_rate, duration):
		self.buf = buf
		self.bits = bits
		self.sample_rate = sample_rate
		self.duration = duration

	def play(self):
		pygame.init()
		pygame.mixer.pre_init(self.sample_rate, self.bits)
		sound = pygame.sndarray.make_sound(self.buf)
		sound.play(loops=1, maxtime=int(self.duration * 1000))
		time.sleep(self.duration)