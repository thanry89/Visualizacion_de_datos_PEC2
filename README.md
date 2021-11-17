# Estudio de Técnicas de Visualizacion de Datos (PEC2)

#### Autor:  Jonathan Zambrano
#### Máster Universitario en Ciencia de Datos
#### Universidad Oberta de Catalunya

En el presente proyecto se presentan tres pequeñas muestras de técnicas de visualización de datos correspondiente a los siguientes tipos:
 - Pyramid Chart
 - Slope Chart
 - OHLC (open-high-low-close) Chart

### Pyramid Chart

Esta visualización ha sido generada en la web gratuita INFOGRAM, en donde se presentan dos tipos de Pyramid Chart, por un lado se presenta una piramide con información cuanlitativa y por el otro una visualización cuantitativo correspondiente a un Population Pyramid (comparativo de Población y Sexo entre China y Estados Unidos).

Fuente de Datos: Repositorio Kaggle. Population Pyramid 2019 - Population pyramid (by age group and gender) for some countries - Divyanshu Sharma.
URL: https://www.kaggle.com/hotessy/population-pyramid-2019

La visualización de los Pyramid Charts se encuentran disponibles en el siguiente link: [Infogram Pyramid Charts](https://infogram.com/pyramid-charts-1hxr4zx9dzl8o6y?live)

![Infogram - Population Pyramid Chart](image/Population_Pyramid_Chart.png)


### Slope Chart

``` Python
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
```
