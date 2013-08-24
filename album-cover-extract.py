#!/usr/bin/env python

import sys

import mutagen.id3
import mutagen.flac

try:
	id3 = mutagen.id3.ID3(sys.argv[1])
	open('/home/barosl/test.jpg', 'wb').write(id3.getall('APIC')[0].data)
except mutagen.id3.ID3NoHeaderError:
	flac = mutagen.flac.FLAC(sys.argv[1])
	open('/home/barosl/test.jpg', 'wb').write(flac.pictures[0].data)
