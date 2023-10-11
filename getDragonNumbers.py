import urllib.request
import io
from bs4 import BeautifulSoup
from collections import Counter

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

longest_gametime = "00:00"
shortest_gametime = "99:99"
longest_game = ""
keyWord = "Game Time"
vs = "vs"

cloud = 0
infernal = 0
ocean = 0
chemtech = 0
mountain = 0
hextech = 0

file = ""

firstblood_kill = []
count_firstbloods = dict()

def get_firstblood(urlD):
	buf = io.StringIO(urlD)
	item = ""
	events_found = False
	inside_tab = False
	td_count = 0
	td_found = False
	current_player_name = "Noone"
	while item.strip() != "</html>":
		item = buf.readline()
		if inside_tab and "</td>" in item.strip():
			td_found = False
			td_count = td_count % 7	
		if td_found:
			if td_count == 3:
				current_player_name = item.strip()
			if td_count == 5 and "kill-icon" in item.strip():
				return current_player_name
		if "Events" in item.strip():
			events_found = True
		if events_found and "Action" in item.strip():
			inside_tab = True
		if inside_tab and "<td" in item.strip():
			td_found = True
			td_count += 1

def get_gametime(urlD):
	gametime_found = False
	buf = io.StringIO(urlD)
	while True:
		item = buf.readline()
		if gametime_found:
			return item.strip()[4:-5]
			break
		if keyWord in item:
			gametime_found = True
	return "00:00"

def get_gamename(urlD):
	buf = io.StringIO(urlD)
	item = ""
	gamename = ""
	while item.strip() != "</html>":
		item = buf.readline()
		if vs in item.strip():
			return item.strip()[41:-72]

with open("games_timelines.txt") as file:
	for item in file:
		resp = opener.open(item)
		urlB = resp.read()
		urlD = urlB.decode("utf8")
		urlPretty = BeautifulSoup(urlB).prettify()
		gamename = get_gamename(urlD)
		current_gametime = get_gametime(urlD)
		firstblood_kill.append(get_firstblood(urlPretty))
		count_firstbloods = dict(Counter(firstblood_kill))
		if int(longest_gametime.replace(':', '')) < int(current_gametime.replace(':','')):
			longest_gametime = current_gametime
			longest_game = gamename
		if int(shortest_gametime.replace(':', '')) > int(current_gametime.replace(':','')):
			shortest_gametime = current_gametime	
		cloud += urlD.count("cloud-dragon")
		infernal += urlD.count("fire-dragon")
		ocean += urlD.count("ocean-dragon")
		chemtech += urlD.count("chemtech-dragon")
		mountain += urlD.count("mountain-dragon")
		hextech += urlD.count("hextech-dragon")
		file = urlD
cloud = int(cloud/2)
infernal = int(infernal/2)
ocean = int(ocean/2)
chemtech = int(chemtech/2)
mountain = int(mountain/2)
hextech = int(hextech/2)