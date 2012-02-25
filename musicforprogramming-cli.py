#!/usr/bin/python

import feedparser
import sys,os

d = feedparser.parse('http://musicforprogramming.net/rss.php')

def episodes():
	for episode in d['entries']:
		print episode['subtitle'],episode['links'][0]['href']
		print ''
	print 'Enter the episode number: (example, 1 for episode 01)'
	ep = input()
	print 'Playing ',d['entries'][ep-1]['subtitle']
	os.system("mpg123 -o alsa -q %s" % d['entries'][ep-1]['links'][0]['href'])
def play_latest():
	n = len(d['entries'])
	print 'Playing ',d['entries'][n-1]['subtitle'],'...'
	print ''
	os.system("mpg123 -o alsa -q %s" % d['entries'][n-1]['links'][0]['href'])

def download_latest():
	n = len(d['entries'])
	print 'Press enter to download the latest episode.'
	raw_input()
	os.system("wget %s" % d['entries'][n-1]['links'][0]['href'])

def select_download():
	for episode in d['entries']:
		print episode['subtitle']
		print ''
	print 'Enter the episode number: (example 1 for episode 01)'
	ep = input()
	os.system("wget %s" % d['entries'][ep-1]['links'][0]['href'])

if len(sys.argv) == 1:
	print 'Usage:\nmusicforprorgamming -h <help>\nmusicforprogramming -l <latest episode>\nmusicforprogramming -s <select episode>\nmusicforprogramming -dl <download latest episode>\nmusicforprogramming -sd <select episode to download>\n'
elif sys.argv[1] == '-h':
	print d['feed']['subtitle']
	print ''
	print d['feed']['summary']
	print ''
	print d['feed']['copyright']
	print ''
elif sys.argv[1] == '-s':
	episodes()
elif sys.argv[1] == '-l':
	play_latest()
elif sys.argv[1] == '-ld':
	download_latest()
elif sys.argv[1] == '-sd':
	select_download()
else:
	print 'Usage:\nmusicforprorgamming -h <help>\nmusicforprogramming -l <latest episode>\nmusicforprogramming -s <select episode>\nmusicforprogramming -dl <download latest episode>\nmusicforprogramming -sd <select episode to download>\n'
