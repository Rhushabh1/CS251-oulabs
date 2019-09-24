import argparse 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('ggplot')


def mean_line_crude(df):
	xs = np.unique(df['horizon'])
	print(xs)
	for x in xs:
		ys = df[df['horizon'] == x]
		mean = ys['REG'].mean()
		print(mean)
	return 


def mean_line(df):
	xs = np.unique(df['horizon'])
	ys = df.groupby('horizon').mean()['REG']
	return xs, ys



parser = argparse.ArgumentParser()
parser.add_argument("--data", metavar="--data", nargs = '+',help = "the path of data file")
args = parser.parse_args()

filename = args.data[0]
df = pd.read_csv(filename)



instances = np.unique(df['instance'])
plot_no = 1
colors = 10*['b','g','r','c','m','chocolate','purple']

for instance in instances:
	df_by_instance = df[df['instance'] == instance]
	algos = np.unique(df_by_instance['algorithm'])

	line_no = 0
	plt.figure(plot_no)

	for algo in algos:
		df_by_algo = df_by_instance[df_by_instance['algorithm'] == algo]

		if algo == 'epsilon-greedy':
			eps = np.unique(df_by_algo['epsilon'])

			for ep in eps:
				df_by_ep = df_by_algo[df_by_algo['epsilon'] == ep]

				xs, ys = mean_line(df_by_ep)
				# plt.loglog(xs,ys)
				plt.loglog(xs, ys, label = algo+' with epsilon='+str(ep), color = colors[line_no])
				line_no+=1


		else:
			xs, ys = mean_line(df_by_algo)
			# plt.loglog(xs,ys)
			plt.loglog(xs,ys, label = algo, color = colors[line_no])
			
			line_no+=1

	plt.xlabel('Horizon')
	plt.ylabel('Regret')
	plt.title(instance)
	plt.legend(loc = 'upper left')
	
	plt.savefig('instance'+str(plot_no)+'.png')
	plt.show()

	plot_no+=1

