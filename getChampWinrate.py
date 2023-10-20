import urllib.request
from bs4 import BeautifulSoup
import io
from collections import Counter

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

championStats = dict()

with open("champion_stats.txt") as file:
	for item in file:
		resp = opener.open(item)
		urlB = resp.read()
		urlD = BeautifulSoup(urlB).prettify()
		urlLines = io.StringIO(urlD)
		endTable = "XPD@15"
		endTableFound = False
		imgFound = False
		classCount = 0
		classCountChanged = False
		currentChampion = "noChamp"
		for line in urlLines:
			if endTable in line:
				endTableFound = True
			if endTableFound:
				if imgFound:	
					if not championFound:
						championStats[line.strip()] = []
						championFound = True
						currentChampion = line.strip()
				if "img" in line:	
					imgFound = True
					championFound = False
					classCount = 0
				if classCount > 0 and classCountChanged:
					classCountChanged = False
					championStats[currentChampion].append(line.strip())
				if "class" in line:
					classCount += 1
					classCountChanged = True
	print(championStats)