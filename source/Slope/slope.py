import pandas as pd
import matplotlib.pyplot as plt


# Fuente de datos
df = pd.read_csv('UNdata.csv')

# Listado de países
countries = ['Argentina', 'Brazil', 'Chile', 'Ecuador', 'Mexico', 'Peru', 'Uruguay']

# Visualización
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
plt.ylabel('USD')
# titulo
plt.title('PIB per capita Latinoamerica', loc='left', fontsize=20)
plt.show()
# Fuente
# https://towardsdatascience.com/slope-charts-with-pythons-matplotlib-2c3456c137b8
