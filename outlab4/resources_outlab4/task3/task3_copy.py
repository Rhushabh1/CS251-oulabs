import argparse 
from scipy.cluster.vq import kmeans2,vq
import numpy as np 
import cv2
import pickle
import matplotlib.pyplot as plt
 
parser = argparse.ArgumentParser()
parser.add_argument("--input", metavar="INPUT", nargs = '+',help = "the path of input image")
parser.add_argument("--k", metavar="K", nargs = '+',type = int, help = "as in kmeans++")
parser.add_argument("--output", metavar="OUTPUT", nargs = '+',help = "the path of output image")
args = parser.parse_args()

input_file = args.input[0]
k = int(args.k[0])
output_file = args.output[0]

img = cv2.imread(input_file,1)
img = np.array(img, dtype= float)
r,c,h = img.shape
img = img.reshape(r*c, 3)

for x in range(1,k+1):
	print(x)
	centroids, label = kmeans2(img, x, minit='++')

########################## save data in a pickle
	with open('kmeans'+str(x)+'.pickle','wb') as fin:
		pickle.dump(centroids, fin)
		pickle.dump(label, fin)

########################## load saved pickle
# pickle_in = open("kmeans.pickle",'rb')
# centroids = pickle.load(pickle_in)
# label = pickle.load(pickle_in)
# pickle_in.close()

	for i in range(len(label)):
		img[i] = centroids[label[i]]

	img = img.astype(int)
	img = img.reshape(r,c,3)

	cv2.imwrite(output_file+str(x)+'.png' ,img)




