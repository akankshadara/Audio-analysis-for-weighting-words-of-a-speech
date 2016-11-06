from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from pylab import subplot
from numpy import mean

input_data = read("reason_deep_learning.wav")
audio = input_data[1]
frequency = input_data[0]
abs_list = abs(audio[:, 1])
m =  mean(abs_list)

print "mean = " + str(m)

def to_time(num_list):
    seconds_list = []
    for i in num_list:
        seconds_list.append((i+0.0)/frequency)

    for i in range(30):
        print seconds_list[i*100]


def plot_original_graph(abs_list):
    plt.plot(abs_list)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.title("Sample Wav")
    plt.show()

def plot_cleaned_graph(abs_list):
    val = input("enter threshold value: ")
    new_l = []
    time_list = []
    for (index, element) in enumerate(abs_list):
        if (int(element) < val):
            new_l.append(0)
        else:
            new_l.append(element)
            time_list.append(index)

    to_time(time_list)
    plt.plot(new_l)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.title("Sample Wav")
    plt.show()
    print "graph successfully plotted"



plot_original_graph(abs_list)
plot_cleaned_graph(abs_list)


