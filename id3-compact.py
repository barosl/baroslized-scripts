#!/usr/bin/env python

import os
import sys
from mutagen.id3 import ID3
from stat import ST_ATIME, ST_MTIME

def compact(fpath):
	if os.path.isdir(fpath):
		for fname in os.listdir(fpath):
			compact(fpath+'/'+fname)
	elif fpath.lower().endswith('.mp3'):
		print '* %s' % os.path.basename(fpath)

		tag = ID3(fpath)

		saved = {}
		for key, val in tag.iteritems():
			saved[key] = val

		st = os.stat(fpath)

		tag.delete()
		for key, val in saved.iteritems():
			tag[key] = val
		tag.save()

		os.utime(fpath, (st[ST_ATIME], st[ST_MTIME]))

def main():
	for fpath in sys.argv[1:]:
		compact(fpath)

if __name__ == '__main__':
	main()
