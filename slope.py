import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('UNdata.csv')

countries = ['Argentina', 'Brazil', 'Chile', 'Ecuador', 'Mexico', 'Peru', 'Uruguay']
fig, ax = plt.subplots(1, figsize=(10,10))
for i in countries:
    # get a single country from the list
    temp = df[df['Country or Area'] == i]
    # plot the lines
    plt.plot(temp.Year, temp.Value, marker='o', markersize=5)
    # end label
    plt.text(temp.Year.values[0]+0.02, temp.Value.values[0], i)
    # start label
    plt.text(temp.Year.values[1]-0.02, temp.Value.values[1], i, ha='right')
    
# x limits, x ticks, and y label 
plt.xlim(2017.5,2019.5)
plt.xticks([2018, 2019])
# get y ticks, replace 1,000 with k, and draw the ticks
yticks = plt.yticks()[0]
plt.yticks(yticks, ['{}k'.format(i/1000) for i in yticks])
plt.show()
