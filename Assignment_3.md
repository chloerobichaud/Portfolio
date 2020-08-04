
subjects = ['spid10_2014_06_17_17_44', 'spid12_2014_06_20_15_11']

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

in_file = subjects[0]+'/'+subjects[0]+'_data.txt'

df=pd.read_csv(in_file, sep='\t')

df.isnull().sum()

df = df.dropna()

df = df.iloc[::3,:]

df.head()


pd.unique(df['block'])

df = df[df['block'] != 'practice']


df['rt'] = df['rt']/1000

plt.hist(df['rt'])

plt.axvline(df['rt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--') 

plt.axvline(df['rt'].median(), 0, 1, color='cyan', linestyle='-')

plt.axvline(df['rt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

plt.show()




