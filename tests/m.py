import threading

from Sound import *

notes = [(550, 1), (440, 1), (660, 1)]
notes = list(map(lambda f: Sound(f[0], f[1]), notes))
threads = []

nbuf = numpy.zeros((notes[0].num_samples, 2), dtype=numpy.int16)
notesNum = len(notes)
for note in notes:
	for i in range(note.num_samples):
		nbuf[i][0] += note.buf[i][0]/notesNum
		nbuf[i][1] += note.buf[i][1]/notesNum

sound = pygame.sndarray.make_sound(nbuf)
one_sec = 1000  # Milliseconds
sound.play(loops=1, maxtime=int(1 * one_sec))
time.sleep(1)