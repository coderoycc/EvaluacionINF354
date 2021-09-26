import pandas as pd

df = pd.read_csv("D:/Tareas/INF354/Datasets/OlimpiadasGenero.csv")


#Graficamos la desviacion Standar -- DESCOMENTAR
#df.std(numeric_only=True).plot(kind='bar')

#Graficamos Participacion por género
import matplotlib.pyplot as plt
plt.pie([df['Male'].sum(), df['Female'].sum()], labels=['Varones', 'Mujeres'], colors=['cyan', 'orange'], explode=[0.1,0.1], shadow=True, autopct='%.2f%%')
plt.show()