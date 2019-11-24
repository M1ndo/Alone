#!/usr/bin/env python3
# Created By ybenel 
##########################################
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
yellow="\033[1;36m"
Red="\033[1;31m"
purple="\033[35m"
Light="\033[95m"
cyan="\033[96m"
stong="\033[39m"
unknown="\033[38;5;82m"
unknown2="\033[38;5;198m"
unknown3="\033[38;5;208m"
unknown4="\033[38;5;167m"
###########################################
from time import sleep

import re
import sys
import requests
import urllib.request
import random
import argparse

good = "\033[92m✔\033[0m"

# This magic spell lets me erase the current line.
# I can use this to show for example "Downloading..."
# and then "Downloaded" on the line where
# "Downloading..." was.
ERASE_LINE = '\x1b[2K'

# This extracts the video url
def extract_url(html, quality):

	if quality == "sd":
		# Standard Definition video
		url = re.search('sd_src:"(.+?)"', html)[0]
	else:
		# High Definition video
		url = re.search('hd_src:"(.+?)"', html)[0]

	# cleaning the url
	url = url.replace('hd_src:"', '')
	url = url.replace('sd_src:"', '')
	url = url.replace('"', "")

	return url

print("        "+unknown4+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown4+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown4+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Blue+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
print("        "+Blue+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
print("        "+Blue+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
print("        "+Blue+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
print("        "+Blue+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
print("        "+Blue+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
print("        "+Blue+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
print("        "+Blue+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
print("        "+Blue+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
print("        "+Blue+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
print("        "+Blue+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
print("        "+Blue+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
print("        "+Blue+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
print("        "+Blue+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
print("        "+Blue+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
print("        "+Blue+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
print("        "+Blue+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
print("        "+Green+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Green+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Green+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Green+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Green+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Blue+"                   "+unknown+"["+unknown3+"Alone"+unknown+"]"+unknown+"         ")
print("     "+purple+"             "+unknown+"["+unknown2+"  Created By ybenel"+unknown+"]"+unknown+"    "+Reset+"\n")
def main():
	parser = argparse.ArgumentParser(description = "Download videos from facebook In High quality Or In Low")

	parser.add_argument('url', action="store")
	parser.add_argument('resolution', action="store", nargs="?")

	args = parser.parse_args()

	print("Fetching source code...", end="\r", flush=True)
	r = requests.get(args.url)
	sys.stdout.write(ERASE_LINE)
	print(good, "Fetched source code")

	file_url = extract_url(r.text, args.resolution)

	# Generates a random number with will be the file name
	path = str(random.random())[3:12] + ".mp4"

	print("Downloading video...",  end="\r", flush=True)
	# Downloads the video
	urllib.request.urlretrieve(file_url, path)
	sys.stdout.write(ERASE_LINE)
	print(good, "Video downloaded:", path)

if __name__=="__main__":
	main()
