import time

import pysinewave

sineA = pysinewave.SineWave(pitch=440)
sineE = pysinewave.SineWave(pitch=329.63)
sineCs = pysinewave.SineWave(pitch=277.18)

sineA.play()
sineE.play()
sineCs.play()

time.sleep(2)

sineA.stop()
sineE.stop()
sineCs.stop()