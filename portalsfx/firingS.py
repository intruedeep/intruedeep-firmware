# As far as I can tell, somehow repeatedly opening .wav files does not cause a memory leak
# and you do not need to close the file.

import pyaudio
import wave
import sys
import random

p = pyaudio.PyAudio()

while (True):
    num = random.randint(1,3)

    if (num == 1):
        wf = wave.open('wavs/Turret_turret_fire_4x_01.wav', 'rb')
    elif (num == 2):
        wf = wave.open('wavs/Turret_turret_fire_4x_02.wav', 'rb')
    elif (num == 3):
        wf = wave.open('wavs/Turret_turret_fire_4x_03.wav', 'rb')

    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()), \
                    channels = wf.getnchannels(), \
                    rate = wf.getframerate(), \
                    output = True)

    data = wf.readframes(1024)

    while (data != ''):
        stream.write(data)
        data = wf.readframes(1024)

    stream.stop_stream()
    stream.close()
    
p.terminate()
