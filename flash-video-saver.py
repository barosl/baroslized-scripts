#!/usr/bin/env python

import os
import shutil

out_fpath_fmt = 'out-%d.bin'

vid_id = 1
pids = [int(x) for x in os.popen('ps -eo pid,args | grep libflashplayer.so | grep -v grep | awk \'{print $1}\'').read().split()]
dpath = '/proc/%d/fd' % pids[0]
for fname in os.listdir(dpath):
	fpath = dpath+'/'+fname
	link_fpath = os.readlink(fpath)
	if '/tmp/Flash' in link_fpath:
		while True:
			out_fpath = out_fpath_fmt % vid_id
			if not os.path.exists(out_fpath): break
			vid_id += 1

		print '* Saving %s to %s' % (os.path.basename(link_fpath), out_fpath)
		shutil.copy2(fpath, out_fpath)
