import cPickle as pickle

import sys

filename = sys.argv[1]
data = pickle.load(open(filename, 'rb'))

words = ""

for x in data:
    word = x[0]
    if word[0] == '<' or word[0] == '[':
        if word == '<sil>' or word == '<s>':
            words = words + '. '
        continue
    t = word.find('(')
    if t != -1:     
        word = word[:t]
    words = words + word + " "

print words

