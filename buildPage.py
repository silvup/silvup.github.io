from getDragonNumbers import *

with open("index.html","w") as f:
	f.writelines(["<!DOCTYPE html>\n",
		"<html>\n",
		"<head>\n",
		"<link rel=\"stylesheet\" href=\"styles.css\">\n",
		"<title>Pickem Stats</title>\n",
		"</head>\n",
		"<body>\n",
		"<h1>PICKEM STATS</h1>\n\n",
		"<h2>Dragon Count</h2>\n"])	
	f.write("<p>Cloud: " + str(cloud) +"</p>\n")
	f.write("<p>Infernal: " + str(infernal) + "</p>\n")
	f.write("<p>Ocean: " + str(ocean) + "</p>\n")
	f.write("<p>Chemtech: " + str(chemtech) + "</p>\n")
	f.write("<p>Mountain: " + str(mountain) + "</p>\n")
	f.write("<p>Hextech: " + str(hextech) + "</p>\n")
	f.writelines(["</body>\n","</html>"])