from math import *

class Dimension:
	def __init__(self,s):
		buff = [x for x in s.split() if x!='-']
		coordinates = [int(x) for x in buff[0].split(',')]
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.z = coordinates[2]
		date = [int(x) for x in buff[1].split('/')]
		self.dd = date[0]
		self.mm = date[1]
		self.yy = date[2]

	def __sub__(self, other):
		distance = sqrt( ((self.x-other.x)**2) + ((self.y-other.y)**2) + ((self.y-other.y)**2) )
		if self.yy > other.yy:
			return -1
		elif self.yy < other.yy:
			return distance
		else:
			if self.mm < other.mm:
				return distance
			elif self.mm > other.mm:
				return -1
			else:
				if self.dd < other.dd:
					return distance
				else :
					return -1

	def __str__(self):
		# print("({}, {}, {}) Time: ({}, {}, {})".format(self.x,self.y,self.z,self.yy,self.mm, self.dd))
		return "Coordinates: ({}, {}, {}) Time: ({}, {}, {})".format(self.x,self.y,self.z,self.yy,self.mm, self.dd)

s = input()
current_point = Dimension(s)
n = int(input())
closest_point = []
least_distance = 100000000000

for x in range(n):
	temp = input()
	obj = Dimension(temp)
	diff = current_point - obj
	if diff!=-1 and diff<least_distance:
		closest_point.append(obj)
		least_distance = diff

if len(closest_point)==0:
	print("Can't move to any point")
else:
	print("Closest point is:")
	print(closest_point[-1])
