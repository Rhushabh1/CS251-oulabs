import sys
import re


path = sys.argv[1]
cont = sys.argv[2]
cont = int(cont)
dic_email = {}


diary = open(path , 'r')
buffer = diary.read()
diary.close()

regex_email = '[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]+'
regex_contact = '[0-9]+'

for i in buffer.split() :
	lst = re.findall(regex_email,i)
	if lst != []:
		if lst[0] in dic_email:
			dic_email[lst[0]] += 1
		else :
			dic_email[lst[0]] = 1

	num_lst = re.findall(regex_contact,i)

	if (num_lst != []):
		val = int(num_lst[0])
		check = (len(num_lst[0]) == 10) and (num_lst[0][0] != '0')
		if check == True:
			if val in dic_email:
				dic_email[val] += 1
			else :
				dic_email[val] = 1


print(dic_email)
print("my frequency: ", dic_email[cont])

count = dic_email[cont]

no_print = 0
for i in dic_email:
	value = dic_email[i]
	if (i != cont) and (value > count) :
		print("Cheater alert! ",i," ",value)
		no_print += 1

if no_print == 0:
	print("It's all good yo!")