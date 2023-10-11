import urllib.request
from bs4 import BeautifulSoup
import io

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

players = ["noplayer"]
kills = [0]
deaths = [0]
assists = [0]
playerKDA = dict()
playerKills = dict()
playerDeaths = dict()
playerAssists = dict()
playerHighestKill = dict()

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
highestKills = dict()
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
		playernum = 0
		killsnum = 0
		deathsnum = 0
		assistsnum = 0
		playerLineCount = 0
		pentakill_spot = False
		player_spot = False
		kills_spot = False
		deaths_spot = False
		assists_spot = False
		kda_spot = False
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
			if kills_spot and deaths_spot == False:
				killsnum += 1
				pos = int(killsnum/3)
				if line.strip().isnumeric():
					if players[pos] in playerKills:
						playerKills[players[pos]] += int(line)
					else:
						playerKills[players[pos]] = int(line)
					if players[pos] in playerHighestKill:
						if int(line) > playerHighestKill[players[pos]]:
							playerHighestKill[players[pos]] = int(line)
					else:
						playerHighestKill[players[pos]] = int(line)
			if "Kills" == line.strip():
				kills_spot = True
			if deaths_spot and assists_spot == False:
				deathsnum += 1
				pos = int(deathsnum/3)
				if line.strip().isnumeric():
					print(line + " deaths" + players[pos])
			if "Deaths" == line.strip():
				deaths_spot = True
			if assists_spot and kda_spot == False:
				assistsnum += 1
				pos = int(assistsnum/3)
				if line.strip().isnumeric():
					print(line + " assists" + players[pos])
			if "Assists" == line.strip():
				assists_spot = True
			if "KDA" == line.strip():
				kda_spot = True
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
	# print(sorted(playerHighestKill.items(), key=lambda x:x[1], reverse = True))
	highestKills = sorted(playerHighestKill.items(), key=lambda x:x[1], reverse = True)[:3]

					
