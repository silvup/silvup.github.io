import urllib.request
import io
from bs4 import BeautifulSoup
from collections import Counter
import time


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()


picks = []
bans = []
most_banned = dict()
most_picked = dict()

def get_picks(urlD):
	global picks
	global bans
	buf = io.StringIO(urlD)
	item = ""
	bans_found = False
	picks_found = False
	bans_count = 0
	picks_count = 0
	while item.strip() != "</html>":
		item = buf.readline()
		if picks_found and "img alt" in item.strip():
			picks.append(item.strip().split("\"")[1])
			picks_count += 1;
			if picks_count == 5 or picks_count == 10:
				picks_found = False
			# print(item.strip().split("\"")[1])
		if bans_found and "img alt" in item.strip():
			bans.append(item.strip().split("\"")[1])
			bans_count += 1;
			if bans_count == 5 or bans_count == 10:
				bans_found = False
			# print(item.strip().split("\"")[1])
		if "Bans" == item.strip():
			bans_found = True
		if "Picks" == item.strip():
			picks_found = True
		if bans_count == 10 and picks_count == 10:
			break
	

with open("games_general.txt") as file:
	for item in file:
		resp = opener.open(item)
		# time.sleep(5)
		urlB = resp.read()
		# time.sleep(5)
		urlD = urlB.decode("utf8")
		urlPretty = BeautifulSoup(urlB).prettify()
		get_picks(urlPretty)
		file = urlD
	most_banned = dict(Counter(bans).most_common(5))
	most_picked = dict(Counter(picks).most_common(5))
