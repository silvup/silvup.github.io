import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

cloud = 0
infernal = 0
ocean = 0
chemtech = 0
mountain = 0
hextech = 0

file = ""

with open("games_timelines.txt") as file:
	for item in file:
		resp = opener.open(item)
		urlB = resp.read()
		urlD = urlB.decode("utf8")
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