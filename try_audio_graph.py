from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from pylab import subplot
from numpy import mean, median
# import wave

# read audio samples
input_data = read("deep_learn.wav")
audio = input_data[1]

l = abs(audio[:, 1])

m =  mean(l)           #printing the mean value ; usually turns out to be very less
print "mean = " + str(m)

new_l = []             #enumerating each point in list 'l' ; 
for (index,element) in enumerate(l):
    if (int(element)< 10000):       #setting the threshold to be 10,000 here ; if value is less than threshold than set the
        new_l.append(0)             # .. new value to 0 in the new list 'new_l'
    else:   
        new_l.append(element)       # else set the original value in the new_list


print "plotting the graph..."       # plotting the graph of this new list
subplot(2,1,1)
plt.plot(new_l)
subplot(2,1,2)
plt.plot(l)

plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Sample Wav")
plt.show()
# '''

# initial try for implementing the code.
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

