import cPickle as pickle
import sys
filename = sys.argv[1]
times = sys.argv[2]
data = pickle.load(open(filename, 'rb'))
time = pickle.load(open(times, 'rb'))
ans = []
for x in time:
    i = 0
    while i < len(data):
        if data[i][1] < x:
            i+=1
            continue
        ans.append(data[i-1][0])
        ans.append(data[i][0])
        ans.append(data[i+1][0])
        break
#print ans
stop_words = set(["a","able","about","across","after","all","almost",
    "also","am","among","an","and","any","are","as","at","be","because",
    "been","but","by","can","cannot","could","dear","did","do","does",
    "either","else","ever","every","for","from","get","got","had","has",
    "have","he","her","hers","him","his","how","however","i","if","in",
    "into","is","it","its","just","least","let","like","likely","may",
    "me","might","most","must","my","neither","no","nor","not","of",
    "off","often","on","only","or","other","our","own","rather","said",
    "say","says","she","should","since","so","some","than","that","the",
    "their","them","then","there","these","they","this","tis","to","too",
    "twas","us","wants","was","we","were","what","when","where","which",
    "while","who","whom","why","will","with","would","yet","you","your"])

finalans = []

for word in ans:
    if word[0] == '<' or word[0] == '[':
        continue
    t = word.find('(')
    if t == -1:
        if word in stop_words:
            continue
        finalans.append(word)
    else:
        if word[:t] in stop_words:
            continue
        finalans.append(word[:t])
print finalans


