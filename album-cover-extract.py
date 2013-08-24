#!/usr/bin/env python

import sys

import mutagen.id3
import mutagen.flac
import mutagen.mp4

try:
	id3 = mutagen.id3.ID3(sys.argv[1])
	open('/home/barosl/test.jpg', 'wb').write(id3.getall('APIC')[0].data)
except mutagen.id3.ID3NoHeaderError:
	try:
		flac = mutagen.flac.FLAC(sys.argv[1])
		open('/home/barosl/test.jpg', 'wb').write(flac.pictures[0].data)
	except mutagen.flac.FLACNoHeaderError:
		mp4 = mutagen.mp4.MP4(sys.argv[1])
		open('/home/barosl/test.jpg','wb').write(mp4['covr'][0])
