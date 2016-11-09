try:
    import cPickle as pickle
except ImportError:
    import pickle

import sys

try:
    filename = sys.argv[1]
except IndexError:
    print "No file"

lis = pickle.load(open(filename, 'rb'))
print "Enter Audio length : "
audiolen = sys.argv[2]
lastframe = lis[len(lis)-1][2]

finaltranscript = []
for x in lis:
    word = x[0]
    start = x[1]
    end = x[2]
    start = float(start)*audiolen/lastframe
    end = float(end)*audiolen/lastframe
    finaltranscript.append((word, start, end))
print "Dumping the final transcript"
pickle.dump(finaltranscript, open(filename+'sec', 'wb'))
print "Transcript dumped successfully"
#print finaltranscript
