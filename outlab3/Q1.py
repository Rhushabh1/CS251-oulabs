import tarfile
import os
from sys import *


def create_name(nam):
	y=[x for x in nam.split('/')]
	res=''
	for i in y:
		res=res+'-'+i
	res = res[1:]
	return res
n=0


path_list = argv[2:]
abs_lst = []

if len(argv[1:])<2:
	print("not enough arguements")
	exit()


for x in path_list:
	abs_lst.append(os.path.abspath(x))


tar = tarfile.open(argv[1], "w:gz" )

added_files = []

n = 0

missing_file = []


def compress(given_path):
	global n
	if os.path.isfile(given_path):
		nam=create_name(given_path)
		if nam in added_files:
			None
		else :
			added_files.append(nam)
			tar.add(given_path,arcname = nam)
	elif os.path.isdir(given_path):
		in_lst = os.listdir(given_path)
		for a in in_lst:
			new_path = given_path + "/" + a
			compress(new_path)
	else:
		n=n+1
		missing_file.append(given_path)




for x in abs_lst:
	compress(x)


if n == len(path_list) :
	print("All files are missing")
else :
	print("Successfully Compressed")
	for x in missing_file:
		print(x)


