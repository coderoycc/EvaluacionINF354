#importamos Librearias
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

#Leemos y preprocesamos los datos
df = pd.read_csv("D:/Tareas/INF354/Datasets/StudentsPerformance.csv")
df = pd.DataFrame(df, columns=['gender', 'lunch', 'test preparation course', 'math score', 'reading score'])
df['lunch'].replace(('standard', 'free/reduced'), (1, 0), inplace=True)
df['test preparation course'].replace(('completed', 'none'), (1, 0), inplace=True)

#Creamos vector de variable independientes
x = df[['lunch', 'test preparation course', 'math score', 'reading score']].values
print(x[0:5])
#creamos nuestro vector de etiquetas Genero
y = df['gender']
print(y[0:5])

#entrenamiento
from sklearn.model_selection import train_test_split
#ENTRENAMIENTO 70% ENTRENAMIENTO 30%
#Con 10 SPLITS
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

print("Set de entrenamiento ", x_train.shape, y_train.shape)
print("Set de testeo ", x_test.shape, y_test.shape)

#Modelado del ARBOL DE DECISIONES
arbol = DecisionTreeClassifier(criterion="entropy", max_depth=4)
arbol.fit(x_train, y_train)

arbolPre = arbol.predict(x_test)

#Mostramos resultados de la prediccion
print("Prediccion: ",arbolPre[0:5])
print("Valores Reales: ", y_test[0:5])



