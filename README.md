# Estudio de Técnicas de Visualizacion de Datos (PEC2)

#### Autor:  Jonathan Zambrano
#### Máster Universitario en Ciencia de Datos
#### Universidad Oberta de Catalunya

En el presente proyecto se presentan tres pequeñas muestras de técnicas de visualización de datos correspondiente a los siguientes tipos:
 - Pyramid Chart
 - Slope Chart
 - OHLC (open-high-low-close) Chart

### Pyramid Chart

Esta visualización ha sido generada en la web gratuita INFOGRAM, en donde se presentan dos tipos de Pyramid Chart, por un lado una piramide con información relativa a las causas de fallecimientos en la ciudad de Nueva York entre 2007 a 2014; y de otro lado, una visualización cuantitativa correspondiente a un Population Pyramid (comparativo de Población y Sexo entre China y Estados Unidos) respecto del año 2019.

Fuente de Datos: Repositorio Kaggle. NY New York City Leading Causes of Death - City of New York.

URL: [Kaggle - NYC Cause of Death 2007 - 2014](https://www.kaggle.com/new-york-city/ny-new-york-city-leading-causes-of-death)

![NYC Death Causes Pyramid Chart](image/NYC_Pyramid_Chart.png)

En esta visualización se han presentado las cuatro principales causas de fallecimiento, en donde, se observa que un tercio de ellas corresponden a enfermedades del corazón, igualando al resto de causas con excepción del cáncer, influenza y diabetes. Igualmente, en el gráfico interactivo se ha añadido el porcentaje de cada causa según la raza. Como información extra gráfico se puede indicar que aproximadamente el 34% de las personas fallecidas corresponden a la raza blanca no hispana. 

Fuente de Datos: Repositorio Kaggle. Population Pyramid 2019 - Population pyramid (by age group and gender) for some countries - Divyanshu Sharma.

URL: [Kaggle - Population Pyramid 2019](https://www.kaggle.com/hotessy/population-pyramid-2019)

![Population Pyramid Chart](image/Population_Pyramid_Chart.png)

La visualización corresponde a una comparativa entre la distribución de población, edad y sexo entre los habitantes de China y Estados Unidos. En donde, la primera conclusión que se puede observar a primera vista es que la población de China por edad supera aproximadamente en 4 veces la población de Estados Unidos. Adicionalmente, se puede observar que la distribución de población entre los habitantes de Estados Unidos sigue una tendencia normal, con disminución a medida que aumenta la edad; sin embargo, la población de China presenta una disminución de población entre 0 y 39 años con excepción del rango de 25 a 29 años.

La visualización de los Pyramid Charts indicados previamente se encuentran disponibles en el siguiente link: [Infogram Pyramid Charts](https://infogram.com/pyramid-charts-1hxr4zx9dzl8o6y?live)

### Slope Chart

Para el caso de la visualización de lineas, se ha realizado la programación en lenguaje Python tomando en cuenta la información del PIB del repositorio de datos de las Naciones Unidas, en donde, se han seleccionado algunos países de Sudamérica y México para obtener una comparación de la evolución del PIB entre los años 2018 y 2019.

Fuente de Datos: Repositorio UNData. Per capita GDP at current prices - US dollars. United Nations

URL: [UN - PIB por País](http://data.un.org/Data.aspx?q=GDP&d=SNAAMA&f=grID%3A101%3BcurrID%3AUSD%3BpcFlag%3A1)

![PIB Países Latinoamericanos 2018-2019](image/Slope_Chart_PIB.png)

En el gráfico presentado se pueden obtener rapidamente algunas conclusiones como, que Uruguay y Chile presenta el PIB mas alto de la región, mientras que Ecuador y Perú el mas bajo, aunque Perú presenta un ligero aumento; y, Ecuador, Uruguay y Chile presentan una baja de su valor de PIB, correspondiente a una tendencia dentro de la región. Así mismo, es destacable la gran disminución que han tenido Uruguay, Chile y Argentina; en donde, Uruguay y Argentina coinciden en el año de elecciones para Senado y Presidencia respectivamente.

El código fuente de la representación es la siguiente:

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
# Fuente
# https://towardsdatascience.com/slope-charts-with-pythons-matplotlib-2c3456c137b8
```

### OHLC Chart

La visualización correspondiente a OHLC está orientada principalmente al análisis de tendencias y variación de precios, por lo que, en este punto se ha evaluado la evolución del precio de las acciones de las empresas Netflix y Amazon entre 2019 y 2020. Así mismo, se ha utilizado el lenguaje Python para la generación del OHLC Chart.

Fuente de Datos: Repositorio Kaggle. OHLC Financial Data. Denis.

URL: [Kaggle - OHLC Financial Data](https://www.kaggle.com/dozmaden/ohlc-financial-data)

#### Precio de las acciones de Netflix (2019-2020)

![OHLC Stock Price Netflix](image/OHLC_Netflix.png)


#### Precio de las acciones de Amazon (2019-2020)

![OHLC Stock Price Amazon](image/OHLC_Amazon.png)


Para poder visualizar de mejor manera los valores de las acciones, se ha tomado valores aleatorios en el periodo de 2019 y 2020, en donde, se puede obserbar que en el mes de Septiembre de 2019 ambas empresas presentan una baja en el precio de sus acciones, el cual, se recupera progresivamente hasta septiembre 2020, donde se tiene el valor máximo en ambos. Finalmente, vale acotar que el precio de la acción de Amazon supera en aproximadamente 5 veces el precio de la acción de Netflix.

El código fuente de la representación es la siguiente:

```
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
```
