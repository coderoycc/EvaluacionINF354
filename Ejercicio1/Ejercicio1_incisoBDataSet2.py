import pandas as pd

df = pd.read_csv("D:/Tareas/INF354/Datasets/car.csv")
print("Media".center(20,'*'))
media = df["puertas"].mean()
print("Puertas: ", media)
media = df["capacidad"].mean()
print("#personas Capacidad: ", media)

print("Moda".center(20, '*'))
moda = df["tamano"].mode()
print("Tamaño: ", moda)
moda = df["seguro"].mode()
print("Es Seguro: ", moda)
moda = df["calificacion"].mode()
print("Calificación: ", moda)

print("Desviacion estándar".center(20, '*'))
df = pd.DataFrame(df)
print(df.std(numeric_only=True))
