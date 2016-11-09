import speech_recognition as sr
from pprint import pprint
from os import path
try:
    import cPickle as pickle
except:
    import pickle

import sys
try:
    filename = sys.argv[1]
except IndexError:
    print "no file"
    sys.exit(0)

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), filename)

print "Transcribing file"
# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file

try:
    # transcribe using CMU
    decoder = r.recognize_sphinx(audio, show_all=True)
    segm = decoder.seg()
    lis = [(seg.word, seg.start_frame, seg.end_frame) for seg in segm]
    #print lis
    print " DUMPING IN FILE "
    pickle.dump(lis, open(filename+'.trans', 'wb'))
    print "Transcript dumped"
except sr.UnknownValueError:
    print("Damn! Audio is shit")
except sr.RequestError as e:
    print("Error; {0}".format(e))

#try:
#    # enter key to use your api key
#    decoder = r.recognize_google(audio, show_all=True)#, key="")
#    print ("Printing google's result")
#    pprint(decoder)
#except sr.UnknownValueError:
#    print("Google Speech couldnt understand audio")
#except sr.RequestError as e:
#    print("Could not request results from Google Speech Recognition service; {0}".format(e))



#BING_KEY = "948b21ba51054f0e94b63f6bb00aa290"
#try:
#    decoder = r.recognize_bing(audio, key=BING_KEY, show_all=True)
#    pprint(decoder)
#    pickle.dump(decoder, open(filename+'transbing', 'wb'))
#except sr.UnknownValueError:
#    print("Microsoft Bing Voice Recognition could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
