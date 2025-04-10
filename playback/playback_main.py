import math

from playback.Instrument import Instrument
from playback.NToneTemperament import NToneTemperament
from playback.SoundPlayer import SoundPlayer

tet12 = NToneTemperament(n=12, freq=440)
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
print(cmaj)

inst = Instrument(lambda amp, t, freq: int(round(amp * math.sin(2 * math.pi * freq * t))))
cmaj_sound = inst.sound_from_frequencies(cmaj, 1)
fmaj_sound = inst.sound_from_frequencies(fmaj, 1)
gmaj8_sound = inst.sound_from_frequencies(gmaj8, 0.5)
gmaj7_sound = inst.sound_from_frequencies(gmaj7, 0.5)
am_sound = inst.sound_from_frequencies(am, 1)
fmaj8_sound = inst.sound_from_frequencies(fmaj8, 0.5)
fmaj6_sound = inst.sound_from_frequencies(fmaj6, 0.5)
gmaj64_sound = inst.sound_from_frequencies(gmaj64, 1)
gmaj53_sound = inst.sound_from_frequencies(gmaj53, 1)
cmajno5_sound = inst.sound_from_frequencies(cmajno5, 2)
print("what")
player = SoundPlayer(16, 44100)
player.play([
	cmaj_sound,
	fmaj_sound,
	gmaj8_sound,
	gmaj7_sound,
	am_sound,
	fmaj8_sound,
	fmaj6_sound,
	gmaj64_sound,
	gmaj53_sound,
	cmajno5_sound,
], inst)
