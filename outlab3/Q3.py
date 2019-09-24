from math import *

class Dimension:
	
	def __init__ (self,string):
		xyz, date = string.split('-')
		self.x self.y ,self.z = xyz.split(',')

		j,m,y = date.split('/')
		self.d = (y,m,j)

	def __sub__(self,other):
		if other.d > self.d :
			x_1 = self.x - other.x
			y_1 = self.y - other.y
			z_1 = self.z - other.z
			distance = sqrt(x_1*x_1 + y_1*y_1 + z_1*z_1)
			return distance
		else:
			return -1

	def __str__(self):
		str1 = "Coordinates: "
		str2 = "Time: "
		coor = (self.x,self.y,self.z)
		return str1 + str(coor) + str2 + str(self.d)

	


