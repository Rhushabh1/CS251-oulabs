import argparse 
from scipy.cluster.vq import kmeans2
from scipy import misc
import numpy as np 
import pickle
 
parser = argparse.ArgumentParser()
parser.add_argument("--input", metavar="INPUT", nargs = 1 ,help = "the path of input image")
parser.add_argument("--k", metavar="K", nargs = 1 ,type = int, help = "as in kmeans++")
parser.add_argument("--output", metavar="OUTPUT", nargs = 1 ,help = "the path of output image")
args = parser.parse_args()

input_file = args.input[0]
k = args.k[0]
output_file = args.output[0]

img = misc.imread(input_file)
img = np.array(img, dtype= float)
r,c,h = img.shape
img = img.reshape(r*c, h)

centroids, label = kmeans2(img, k, minit='++')

########################## save data in a pickle
with open('kmeans.pickle','wb') as fin:
	pickle.dump(centroids, fin)
	pickle.dump(label, fin)

########################## load saved pickle
# pickle_in = open("kmeans.pickle",'rb')
# centroids = pickle.load(pickle_in)
# label = pickle.load(pickle_in)
# pickle_in.close()

for i in range(len(label)):
	img[i] = centroids[label[i]]

img = img.reshape(r,c,h)

misc.imsave(output_file,img)




