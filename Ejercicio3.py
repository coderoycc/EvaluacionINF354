import pandas as pd
df = pd.read_csv("D:/Tareas/INF354/Datasets/StudentsPerformance.csv")

#Tomamos los datos que nos interesan
df = pd.DataFrame(df, columns=['gender', 'lunch', 'test preparation course', 'math score', 'reading score'])


#****Primer algortimo rellenar notas vacias con la media
from pandas.api.types import is_numeric_dtype
df = df.apply(lambda x: x.fillna(x.mean()) if is_numeric_dtype(x) else x)
print(df.head())



#******Segundo algoritmo de preprocesamiento TRANSFORMATION --> NORMALIZACION VALORES 0, 1
df['lunch'].replace(('standard', 'free/reduced'), (1, 0), inplace=True)
df['test preparation course'].replace(('completed', 'none'), (1, 0), inplace=True)
print(df.sample(10))



#*****Tercer algortimo algoritmo de preprocesamiento eliminar elementos DUPLICADOS
df.drop_duplicates()
print(df.sample(10)) 
