import pygame.midi
import time

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(12)
player.note_on(60, 127)
player.note_on(64, 127)
player.note_on(67, 127)
time.sleep(1)
player.note_off(60, 127)
player.note_off(64, 127)
player.note_off(67, 127)
del player
pygame.midi.quit()