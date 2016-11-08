from scipy.io.wavfile import read
import matplotlib.pyplot as plt
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

    # for i in range(10):
    #     print seconds_list[i*100: (i+1)*100]

    grouped_list = []
    group = []
    i=0
    while(i<len(seconds_list)):
        del group[:]
        while(i<len(seconds_list)-1 and (seconds_list[i+1] - seconds_list[i])< 0.2 ):
            group.append(seconds_list[i])
            i+=1

        if(group!=[]):
            grouped_list.append( mean(group) )
        i+=1
    print "printing grouped list:"
    print "length :" + str(len(grouped_list))
    print grouped_list

def plot_original_graph(abs_list):
    plt.plot(abs_list)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.title("Sample Wav")
    plt.show()

def plot_cleaned_graph(abs_list):
    val = input("enter threshold value: ")
    new_l = []
    index_list = []

    for (index, element) in enumerate(abs_list):
        if (int(element) < val):
            new_l.append(0)
        else:
            new_l.append(element)
            index_list.append(index)

    to_time(index_list)     # return index list

    plt.plot(new_l)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.title("Sample Wav")
    plt.show()
    print "graph successfully plotted"

def find_audio_length(ls):
    print "audio length is: " + str( (len(ls)+ 0.0) /frequency )

find_audio_length(abs_list)
plot_original_graph(abs_list)
plot_cleaned_graph(abs_list)


