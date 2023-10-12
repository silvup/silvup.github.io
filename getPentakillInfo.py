import urllib.request
from bs4 import BeautifulSoup
import io
from collections import Counter
from getDragonNumbers import *


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

players = ["noplayer"]
champs = ["nochamps"]
playerKDA = dict()
playerKills = dict()
playerDeaths = dict()
playerAssists = dict()
playerHighestKill = dict()
champsDeaths = dict()
rolesplayed = dict()
playersChampions = dict()
teamChampions = dict()

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
i = 0

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
		champions_spot = False
		kda_spot = False
		players = ["noplayer"]
		teams = ["noteam"]
		champs = ["nochamps"]
		current_champ = ""
		blue_team = ""
		red_team = ""
		vs_found = False
		for line in urlLines:
			if vs_found == False:
				vs_found = True
				teams = games[i].strip().split("vs")
				blue_team = teams[0].strip()
				red_team = teams[1].strip()
				print(blue_team + red_team)
			if "champions" in line:
				# print(line.strip().split("\"")[1])
				current_champ = line.strip().split("\"")[1]
				champs.append(current_champ)
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
					# print(players[pos])
					if players[pos] in playerDeaths:
						playerDeaths[players[pos]] += int(line)
					else:
						playerDeaths[players[pos]] = int(line)
					if champs[pos] in champsDeaths:
						champsDeaths[champs[pos]] += int(line)
					else:
						champsDeaths[champs[pos]] = int(line)
					if champs[pos] in rolesplayed:
						rolesplayed[champs[pos]].append(pos%5)
					else:
						rolesplayed[champs[pos]] = [pos%5]
					if players[pos] in playersChampions:
						playersChampions[players[pos]].append(champs[pos])
					else:
						playersChampions[players[pos]] = [champs[pos]]
					if pos > 5:
						if red_team in teamChampions:
							teamChampions[red_team].append(champs[pos])
						else:
							teamChampions[red_team] = [champs[pos]]
					else:
						if blue_team in teamChampions:
							teamChampions[blue_team].append(champs[pos])
						else:
							teamChampions[blue_team] = [champs[pos]]
			if "Deaths" == line.strip():
				deaths_spot = True
			if assists_spot and kda_spot == False:
				assistsnum += 1
				pos = int(assistsnum/3)
				if line.strip().isnumeric():
					if players[pos] in playerAssists:
						playerAssists[players[pos]] += int(line)
					else:
						playerAssists[players[pos]] = int(line)
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
		i += 1
	# print(sorted(playerHighestKill.items(), key=lambda x:x[1], reverse = True))
	highestKills = sorted(playerHighestKill.items(), key=lambda x:x[1], reverse = True)[:5]
	for player in playerKills.keys():
		if player != "noplayer":
			playerKDA[player] = round((playerKills[player] + playerAssists[player]) / max(1,playerDeaths[player]),2)
	bestKDAs = sorted(playerKDA.items(), key=lambda x:x[1], reverse = True)[:5]
	mostDeaths = sorted(champsDeaths.items(), key=lambda x:x[1], reverse = True)[:5]
	most_roles_played = dict()
	for champ in rolesplayed.keys():
		if champ != "nochamps":
			most_roles_played[champ] = len(Counter(rolesplayed[champ]))
	champs_with_most_roles = sorted(most_roles_played.items(), key=lambda x:x[1], reverse = True)[:5]
	champs_played = dict()
	for player in playersChampions.keys():
		if player != "noplayer":
			champs_played[player] = len(Counter(playersChampions[player]))
	most_champs_played = sorted(champs_played.items(), key=lambda x:x[1], reverse = True)[:5]
	champs_played_by_team = dict()
	for team in teamChampions.keys():
		if team != "noteam":
			champs_played_by_team[team] = len(Counter(teamChampions[team]))
	most_champs_played_by_team = sorted(champs_played_by_team.items(), key=lambda x:x[1], reverse = True)[:5]
			
		

					
