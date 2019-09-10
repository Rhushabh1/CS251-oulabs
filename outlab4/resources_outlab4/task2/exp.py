import numpy as np 
# a = np.random.normal(5,5)
# b = np.random.normal(2,2)
a = np.arange(25).reshape(5,5)
b = np.arange(4).reshape(2,2)
print(a)

def add_patch(big, small, x,y):
	br, bc = big.shape
	sr,sc = small.shape
	big[x:x+sr, y:y+sc] += small
	print(big)
	# return big


# print(b)

# x,y = 2,2
# x1=np.repeat(np.array([2,3]),2,axis=0).reshape(2,2)
# y1=np.repeat(np.array([2,3]),2,axis=0).reshape(2,2).transpose()
# print(x1)
# print(y1)
# a[x1,y1]+=b
# print(a)

# c = np.arange(25).reshape(5,5)
# add_patch(c,b,2,2)
# # c[2:4,2:4] += b
# # print(c)

b = a.copy()
# b[a>=15] =0
# print(b)
m = np.zeros(a.shape)
x= all([(b<=15), (b>=5)])
m[x] = a[x]/b[x]
print(m)