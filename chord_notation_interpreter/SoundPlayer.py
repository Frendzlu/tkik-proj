import time
from time import sleep

import pygame

from chord_notation_interpreter.Sound import Sound


class SoundPlayer:
    def __init__(self, bits, sample_rate):
        self.bits = bits
        self.sample_rate = sample_rate
        pygame.init()
        pygame.mixer.pre_init(self.sample_rate, self.bits)

    def play(self, sounds: list[Sound], instrument):
        for sound in sounds:
            print(sound)
            if type(sound) == str:
                exec(sound)
                continue
            pysound = pygame.sndarray.make_sound(sound.buf)
            pysound.play(loops=1, maxtime=int(sound.duration * 1000))
            time.sleep(sound.duration)
        # if instrument.bits != self.bits:
        # 	raise ValueError("Instrument bits doesn't match")
        # if instrument.sample_rate != self.sample_rate:
        # 	raise ValueError("Instrument sample rate doesn't match")
