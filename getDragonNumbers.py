import urllib.request
import io

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

longest_gametime = "00:00"
keyWord = "Game Time"
cloud = 0
infernal = 0
ocean = 0
chemtech = 0
mountain = 0
hextech = 0

file = ""

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
	

with open("games_timelines.txt") as file:
	for item in file:
		resp = opener.open(item)
		urlB = resp.read()
		urlD = urlB.decode("utf8")
		current_gametime = get_gametime(urlD)
		print(current_gametime)
		if int(longest_gametime.replace(':', '')) < int(current_gametime.replace(':','')):
			longest_gametime = current_gametime 	
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