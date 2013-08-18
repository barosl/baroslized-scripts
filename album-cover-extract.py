#!/usr/bin/env python

import sys

import mutagen.id3
import mutagen.flac

id3 = mutagen.id3.ID3(sys.argv[1])
open('/home/barosl/test.jpg', 'wb').write(id3.getall('APIC')[0].data)
sys.exit()

flac = mutagen.flac.FLAC(sys.argv[1])
for pic in flac.pictures:
	print pic
	open('/home/barosl/test.jpg', 'wb').write(pic.data)
