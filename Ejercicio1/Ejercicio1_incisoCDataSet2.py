import pandas as pd

df = pd.read_csv("D:/Tareas/INF354/Datasets/car.csv")

#graficamos la preferencia en la calificación
graf = df['calificacion'].value_counts()
#graf.plot(kind='bar')
#Graficamos el tamaño de los autos en forma de torta
import matplotlib.pyplot as plt
pp = df['tamano'].value_counts()

plt.pie([pp['small'], pp['med'], pp['big']], labels=['Pequeño', 'Mediano', 'Grande'], colors=['orange', 'red', 'cyan'], explode=[0.1, 0.1, 0.1], shadow=True, autopct='%.2f%%')
plt.show()

