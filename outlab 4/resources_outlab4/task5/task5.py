import argparse 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('ggplot')


parser = argparse.ArgumentParser()
parser.add_argument("--data", metavar="--data", nargs = '+',help = "the path of data file")
args = parser.parse_args()

filename = args.data[0]
df = pd.read_csv(filename)

df_ep = df[df['algorithm'] == 'epsilon-greedy']
df_no_ep = df[df['algorithm'] != 'epsilon-greedy']

df_by_instance = list(df_ep.groupby(['instance','epsilon','horizon'], sort=False))
print(len(df_by_instance))

# l = df_ep.groupby(['horizon', 'REG'])
# print(l.first())


