from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from numpy import mean
import sys
import cPickle as pickle
import Tkinter as tk



filename = sys.argv[1]          ## input audio file ##
input_data = read(filename)
audio = input_data[1]
frequency = input_data[0]
abs_list = abs(audio[:, 1])     ## taking the mod of the values ##

def to_time(num_list):                                      ## function to return the timestamps of peaks ##
                                                            ## in the graph of stressed-upon words        ##
    ## converting the index of points to seconds ##
    seconds_list = []
    for i in num_list:
        seconds_list.append((i+0.0)/frequency)

    grouped_list = []
    group = []
    i=0

    ## grouping the peaks and returning the mean value ##
    while(i<len(seconds_list)):
        del group[:]
        while(i<len(seconds_list)-1 and (seconds_list[i+1] - seconds_list[i])< 0.2 ):
            group.append(seconds_list[i])
            i+=1

        if(group!=[]):
            grouped_list.append( mean(group) )
        i+=1

    ## dumping the time stamps into a binary file ##
    try:
        import cPickle as pickle
    except ImportError:
        import pickle
    pickle.dump(grouped_list, open('timelist', 'wb'))

def plot_original_graph(abs_list):               ## plotting the initial graph ##
    plt.plot(abs_list)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.title("Sample Wav")
    plt.show()

def plot_cleaned_graph(abs_list, input_value):
    val = int(input_value)  
    new_l = []
    index_list = []

    for (index, element) in enumerate(abs_list):
        if (int(element) < val):
            new_l.append(0)
        else:
            new_l.append(element)
            index_list.append(index)

    to_time(index_list)

    plt.plot(new_l)                 ## plotting the points above threshold values ##
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.title("Sample Wav")
    plt.show()
    print "graph successfully plotted"

def find_audio_length(ls):
    length = str( (len(ls)+ 0.0) /frequency )       ## finding the total time of audio file ##
    print "audio length is: " + str( length )
    pickle.dump(float(length), open('audiolength', 'wb'))

def ask_input_gui():                  ## pop up a gui box to get the input from the user ##

    class MyDialog:
        def __init__(self, parent):
            # top = self.top = tk.Toplevel(parent)
            self.myLabel = tk.Label(parent, text='Enter threshold value,Submit and Close')
            self.myLabel.pack()
            self.myEntryBox = tk.Entry(parent)
            self.myEntryBox.pack()
            self.mySubmitButton = tk.Button(parent, text='Submit', command=self.send)
            self.mySubmitButton.pack()

        def send(self):
            self.username = self.myEntryBox.get()

    def onClick():
        root = tk.Tk()
        inputDialog = MyDialog(root)
        root.mainloop()
        return inputDialog.username

    val = onClick()
    return val


find_audio_length(abs_list)
plot_original_graph(abs_list)
input_value = ask_input_gui()
plot_cleaned_graph(abs_list, input_value)


