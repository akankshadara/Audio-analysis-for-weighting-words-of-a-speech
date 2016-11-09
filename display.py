import cPickle as pickle
import sys

filename = sys.argv[1]

from pprint import pprint

pprint(pickle.load(open(filename, 'rb')))
