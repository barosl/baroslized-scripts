#!/usr/bin/env python

import sys
from mutagen.id3 import ID3

a_fpath = sys.argv[1]
b_fpath = sys.argv[2]

a = ID3(a_fpath)
b = ID3()

for key, val in a.iteritems():
	b[key] = val

b.save(b_fpath)
