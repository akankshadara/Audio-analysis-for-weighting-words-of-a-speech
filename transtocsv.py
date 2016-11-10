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

newwords = ""
i=0
newwords += words[0]
#print len(words)
while True:
    if i == len(words)-1:
        break
    if words[i] == '.' and words[i+1] == '.':
        newwords += '.'
        i+=1
    else:
        newwords += words[i]
    i+=1

#print newwords

listsent = newwords.split('.')
from pprint import pprint 
newlist = []
for x in listsent:
    if len(x) == 1 and len(x) == 0:
        continue
    else:
        newlist.append(x)
#pprint(newlist)
i = 1
j = 1
againnewlist = []
againnewlist.append(newlist[0])
while i < len(newlist):
    if len(newlist[i]) <= 17:
        againnewlist[j-1] += newlist[i]
        i+=1
    else:
        againnewlist.append(newlist[i])
        i+=1
        j+=1

final = []
for x in againnewlist:
    if len(x) < 2:
        continue
    else:
        final.append(x)
#print final
finalstr = ""
for x in final:
    finalstr += x+'. '
print finalstr
