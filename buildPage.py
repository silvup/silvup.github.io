import time
from getDragonNumbers import *
time.sleep(5)
from getPentakillInfo import *
time.sleep(5)
from getGeneralData import *
time.sleep(5)
from getChampWinrate import *


mapping_table = str.maketrans({'{': '','}': '','\'': '','[': '','(': '',')': '',']': ''})

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
	f.write("<h2 class=lightgreen>Reverse sweeps: 1</h2>\n")
	f.write("<h2 class=lightgreen>Baron steals: 1</h2>\n")
	f.write("<h2 class=lightgreen>Pentakills: " + str(pentakillNumber) + "</h2>\n")
	f.write("<h2 class=goldenrod>Most picked champions: </h2>\n")
	f.write("<p class=goldenrod>" + str(most_picked).translate(mapping_table) + "</p>\n")
	f.write("<h2 class=goldenrod>Most banned champions: </h2>\n")
	f.write("<p class=goldenrod>" + str(most_banned).translate(mapping_table) + "</p>\n")
	f.write("<h2 class=goldenrod>Most deaths on champion: </h2>\n")
	f.write("<p class=goldenrod>" + str(mostDeaths).translate(mapping_table) + "</p>\n")	
	f.write("<h2 class=goldenrod>Champions with most roles: </h2>\n")
	f.write("<p class=goldenrod>" + str(champs_with_most_roles).translate(mapping_table) + "</p>\n")	
	f.write("<h2 class =lightsalmon>Players with a pentakill: " + pentakillNames + "</h2>\n")
	f.write("<h2 class=lightsalmon>Most firstbloods: </h2>\n")
	f.write("<p class=lightsalmon>" + str(highest_firstbloods).translate(mapping_table) + "</p>\n")
	f.write("<h2 class=lightsalmon>Most kills in a single game: </h2>\n")
	f.write("<p class=lightsalmon>" + str(highestKills).translate(mapping_table) + "</p>\n")
	f.write("<h2 class=lightsalmon>Best KDA's: </h2>\n")
	f.write("<p class=lightsalmon>" + str(bestKDAs).translate(mapping_table) + "</p>\n")
	f.write("<h2 class=lightsalmon>Most champions played: </h2>\n")
	f.write("<p class=lightsalmon>" + str(most_champs_played).translate(mapping_table) + "</p>\n")
	f.write("<h2 class=lightblue>Best 2 seeds region: GAM Esports</h2>\n")
	f.writelines(["<h2 class=lightblue>Shortest game: ", shortest_gametime, " ", shortest_winner,   "</h2>\n"])
	f.write("<h2 class=lightblue>Most baron steals (team): DK (1)</h2>\n")
	f.write("<h2 class=lightblue>Worlds winners: ?</h2>\n")
	f.write("<h2 class=lightblue>Most champions played by team: </h2>\n")
	f.write("<p class=lightblue>" + str(most_champs_played_by_team).translate(mapping_table) + "</p>\n")
	f.writelines(["</body>\n","</html>"])