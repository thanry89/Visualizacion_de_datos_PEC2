import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_sp = pd.read_csv('NFLX-D.csv')
#df_sp = pd.read_csv('AMZN-D.csv')

df_sp['timestamp'] = pd.to_datetime(df_sp['timestamp']) 

df = df_sp.sample(n=20, random_state=1).sort_index()
df.reset_index(inplace=True)

x = np.arange(0,len(df))
fig, ax = plt.subplots(1, figsize=(12,6))
for idx, val in df.iterrows():
    # high/low lines
    plt.plot([x[idx], x[idx]], [val['low'], val['high']])
    plt.plot([x[idx], x[idx]-0.1], 
             [val['open'], val['open']])
    # close marker
    plt.plot([x[idx], x[idx]+0.1], 
             [val['close'], val['close']])

# ticks
plt.xticks(x, df.timestamp.dt.date, rotation='vertical')
ax.set_xticks(x, minor=True)
# labels
plt.ylabel('USD')
# grid
ax.xaxis.grid(color='black', linestyle='dashed', which='both', alpha=0.1)
# title
plt.title('Netflix Stock Price', loc='left', fontsize=20)
plt.show()
# Fuente
# https://towardsdatascience.com/basics-of-ohlc-charts-with-pythons-matplotlib-56d0e745a5be
