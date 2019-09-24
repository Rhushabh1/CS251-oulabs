
n = int(input())
dic = {}
run_dic = {}

for i in range(n):
	match, score = input().split(':')
	score_list = score.split(',')
	
	player_score_dic = {}
	for i in score_list:
		name , run = i.split('-')
		player_score_dic[name] = int(run)
		if name in run_dic:
			run_dic[name] += int(run)
		else:
			run_dic[name] = int(run)


	dic[match] = player_score_dic

print(dic)
#print(run_dic)

new = sorted(run_dic.items(), key = lambda x : (x[1],x[0]) , reverse = True)

print(new)

 