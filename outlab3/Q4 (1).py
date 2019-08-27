n = int(input())

total = {}
Dict = {}
for x in range(n):
	match = [x for x in input().split(':')]
	stats = [x for x in match[1].split(',')]
	player_stat = {}
	for player in stats:
		temp = player.split('-')
		player_stat[temp[0]] = int(temp[1])
		total[temp[0]] = total.setdefault(temp[0],0) + int(temp[1])

	Dict[match[0]] = player_stat

print(Dict)
scoreboard = []
for play in total:
	scoreboard.append((play,total[play]))

print(scoreboard)

