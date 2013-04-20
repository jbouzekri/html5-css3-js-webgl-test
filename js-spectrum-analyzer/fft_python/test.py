import wave
import struct
import numpy as np

stream = wave.open('../skyfall.wav',"rb")

num_channels = stream.getnchannels()
print "Nb channel : " + str(num_channels)
sample_rate = stream.getframerate()
print "frequence sample FPS : " + str(sample_rate)
sample_width = stream.getsampwidth()
print "largeur sample : " + str(sample_width)
num_frames = stream.getnframes()
print "nb frames : " + str(num_frames)

print "duree : " + str(num_frames / sample_rate / 60) + "min" + str((num_frames / sample_rate)%60)
print "duree : " + str(num_frames / sample_rate) + "sec"

raw_data = stream.readframes( num_frames )
stream.close()

total_samples = num_frames * num_channels

if sample_width == 1: 
    fmt = "%iB" % total_samples # read unsigned chars
elif sample_width == 2:
    fmt = "%ih" % total_samples # read signed 2 byte shorts
else:
    raise ValueError("Only supports 8 and 16 bit audio formats.")

integer_data = struct.unpack(fmt, raw_data)
del raw_data # Keep memory tidy (who knows how big it might be)

print str(len(integer_data))
print str(sample_width*sample_rate)
total_item_in_one_sec = sample_width*sample_rate
print str(len(integer_data[0:total_item_in_one_sec]))



"""
channels = [ [] for time in range(num_channels) ]

for index, value in enumerate(integer_data):
    bucket = index % num_channels
    channels[bucket].append(value)

print '{n}h'.format(n=r.getnframes())
data = struct.unpack('{n}h'.format(n=r.getnframes()), binary_data)
data=np.array(data)
print (data)
freqs = np.fft.fftfreq(len(data));
print(freqs)
"""