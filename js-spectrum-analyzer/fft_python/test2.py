import pysox
import numpy as np;

#open an audio file
testwav = pysox.CSoxStream("skyfall.wav")
readFile = pysox.sox.CSoxStream.open_read(testwav,"skyfall.wav");
signal = testwav.get_signal()
print(type(readFile))
