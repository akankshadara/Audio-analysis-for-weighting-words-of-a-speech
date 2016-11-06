from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from pylab import subplot
from numpy import mean, median
# import wave

# read audio samples
input_data = read("deep_learn.wav")
audio = input_data[1]

l = abs(audio[:, 1])

m =  mean(l)
print "mean = " + str(m)

new_l = []
for (index,element) in enumerate(l):
    if (int(element)< 10000):
        new_l.append(0)
    else:
        new_l.append(element)

# print new_l[15:30]

print "plotting the graph..."
subplot(2,1,1)
plt.plot(new_l)
subplot(2,1,2)
plt.plot(l)

plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Sample Wav")
plt.show()
# '''




'''
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('wavfile.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 1:
    print 'Just mono files'
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,signal)
plt.show()
'''

# import Tkinter
# print  Tkinter.Tk().tk.eval('info tclversion')

