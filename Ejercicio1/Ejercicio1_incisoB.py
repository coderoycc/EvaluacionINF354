import pandas as pd
df = pd.read_csv("D:/Tareas/INF354/Datasets/StudentsPerformance.csv")
print("Media".center(20,'*'))
media = df["math score"].mean()
print("Matemáticas: ", media)
media = df["reading score"].mean()
print("Literatura: ", media)
media = df["writing score"].mean()
print("Escritura: ", media)

print("Moda".center(20, '*'))
moda = df["math score"].mode()
print("Matemáticas: ", moda)
moda = df["reading score"].mode()
print("Literatura: ", moda)
moda = df["writing score"].mode()
print("Escritura: ", moda)

print("Desviacion estándar".center(20, '*'))
df = pd.DataFrame(df)
print(df.std(numeric_only=True))
