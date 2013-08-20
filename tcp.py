#!/usr/bin/env python

from stat import ST_ATIME, ST_MTIME
import sys
import os

assert len(sys.argv) == 3

a = sys.argv[1]
b = sys.argv[2]

st = os.stat(a)
os.utime(b, (st[ST_ATIME], st[ST_MTIME]))
