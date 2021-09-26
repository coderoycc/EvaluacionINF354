import pandas as pd

df = pd.read_csv("D:/Tareas/INF354/Datasets/OlimpiadasGenero.csv")
print("Media".center(20,'*'))
media = df["Female"].mean()
print("Mujeres: ", media)
media = df["Male"].mean()
print("Varones: ", media)
media = df["Total"].mean()
print("Participación: ", media)

print("Moda".center(20, '*'))
moda = df["Female"].mode()
print("Mujeres: ", moda)
moda = df["Male"].mode()
print("Varones: ", moda)
moda = df["Total"].mode()
print("Participación: ", moda)

print("Desviacion estándar".center(20, '*'))
df = pd.DataFrame(df)
print(df.std(numeric_only=True))

