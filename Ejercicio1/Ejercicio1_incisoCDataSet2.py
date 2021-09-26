import pandas as pd

df = pd.read_csv("D:/Tareas/INF354/Datasets/StudentsPerformance.csv")

#graficamos la cantidad de estudiantes que se preparanron antes del examen
graf = df['test preparation course'].value_counts()
graf.plot(kind='bar')

#Graficamos la media de las notas 
"""import matplotlib.pyplot as plt
materias = ['Matemáticas', 'Literatura', 'Escritura']
medias = [df["math score"].mean(), df["reading score"].mean(), df["writing score"].mean()]
plt.bar(materias, medias)
plt.show()

"""

