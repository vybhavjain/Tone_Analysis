# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:02:24 2019

@author: VYBHAV JAIN
"""
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
#write('output1.wav', fs, myrecording)  # Save as WAV file

import wavio
wavio.write('output2.wav', myrecording, fs ,sampwidth=2)