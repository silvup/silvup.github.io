from getDragonNumbers import *
from getPentakillInfo import *

mapping_table = str.maketrans({'{': '','}': '','\'': ''})

with open("index.html","w") as f:
	f.writelines(["<!DOCTYPE html>\n",
		"<html>\n",
		"<head>\n",
		"<link rel=\"stylesheet\" href=\"styles.css\">\n",
		"<title>Pickem Stats</title>\n",
		"</head>\n",
		"<body>\n",
		"<h1>PICKEM STATS</h1>\n\n",
		"<h2 class=lightgreen>Longest game: ", longest_gametime, " ", longest_game,   "</h2>\n", "\n<h2 class=lightgreen>Dragon Count</h2>", "</h2>\n"])	
	f.write("<p class=lightgreen>Cloud: " + str(cloud) +"</p>\n")
	f.write("<p class=lightgreen>Infernal: " + str(infernal) + "</p>\n")
	f.write("<p class=lightgreen>Ocean: " + str(ocean) + "</p>\n")
	f.write("<p class=lightgreen>Chemtech: " + str(chemtech) + "</p>\n")
	f.write("<p class=lightgreen>Mountain: " + str(mountain) + "</p>\n")
	f.write("<p class=lightgreen>Hextech: " + str(hextech) + "</p>\n")
	f.write("<h2 class=lightgreen>Reverse sweeps: 0</h2>\n")
	f.write("<h2 class=lightgreen>Baron steals: 0</h2>\n")
	f.write("<h2 class=lightgreen>Pentakills: " + str(pentakillNumber) + " " + pentakillNames + "</h2>\n")
	f.write("<h2 class=lightsalmon>Most firstbloods: </h2>\n")
	f.write("<p class=lightsalmon>" + str(count_firstbloods).translate(mapping_table) + "</p>\n")
	f.write("<h2 class=lightsalmon>Most baron steals: ?</h2>\n")
	f.write("<h2 class=lightblue>Best 2 seeds region: ?</h2>\n")
	f.write("<h2 class=lightblue>Worlds winners: ?</h2>\n")
	f.writelines(["</body>\n","</html>"])