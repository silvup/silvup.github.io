import urllib.request
from bs4 import BeautifulSoup
import io

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

players = ["noplayer"]

pentakill = "Penta kills"
playerWord = "Player"
playerLineCount = 0
one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
pentakillNames = ""
pentakillNumber = 0
playernum = 0
pentakill_spot = False
player_spot = False
# top jgl mid adc supp

with open("games_stats.txt") as file:
	for item in file:
		resp = opener.open(item)
		urlB = resp.read()
		urlD = BeautifulSoup(urlB).prettify()
		urlLines = io.StringIO(urlD)
		pentakill_spot = False
		playernum = 0
		playerLineCount = 0
		player_spot = False
		players = ["noplayer"]
		for line in urlLines:
			if player_spot:
				playerLineCount += 1
				if playerLineCount < 50 and playerLineCount % 5 == 4:
					players.append(line.strip())
			if playerWord == line.strip():
				player_spot = True
			if playernum > 30:
				break
			if pentakill_spot:
				playernum += 1
				pos = int(playernum/3)
				if one in line:
					pentakillNumber += 1
					pentakillNames += players[pos]
					pentakillNames += " "
				if two in line:
					pentakillNumber += 2
					pentakillNames += players[pos]
					pentakillNames += " "
				if three in line:
					pentakillNumber += 3
					pentakillNames += players[pos]
					pentakillNames += " "
				if four in line:
					pentakillNumber += 4
					pentakillNames += players[pos]
					pentakillNames += " "
				if five in line:
					pentakillNumber += 5
					pentakillNames += players[pos]
					pentakillNames += " "
			if pentakill in line:
				pentakill_spot = True
				

					
