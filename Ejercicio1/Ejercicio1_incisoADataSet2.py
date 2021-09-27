a = open("D:/Tareas/INF354/Datasets/car.csv", 'r', encoding='utf8')
a.readline()

suma = [0, 0]
#Vector para sacar la moda
moda=[{'0':0},{'0':0},{'0':0}]
columnas=[[],[],[]]
for linea in a:
	e=linea.split(",")
	#Media
	suma[0]=int(e[2]) + suma[0]
	suma[1]=int(e[3]) + suma[1]
	columnas[0].append(e[2])
	columnas[1].append(e[3])
	moda[0][e[4]] = moda[0].get(e[4], 0)+1
	moda[1][e[5]] = moda[1].get(e[5], 0)+1
	moda[2][e[6]] = moda[2].get(e[6], 0)+1
print("MEDIA".center(20, '°'))
print(f'Puertas: {round(suma[0]/len(columnas[0]), 2)}\nPersonas: {round(suma[1]/len(columnas[0]), 2)}')
print("MODA".center(20, '°'))
columna=1
for m in moda:
	print(f'Columna: {columna}')
	for key, value in m.items():
		if value == max(m.values()):
			print(key)
			#break
	columna+=1
#Cálculo de la desviacion Estandar
desv=0
for el in columnas[0]:
	desv= desv + ((int(el)-suma[0]/len(columnas[0]))**2)
print(f'Desviacion Estándar #Puertas: {round((desv/len(columnas[0]))**(1/2) ,2)}')
desv=0
for el in columnas[1]:
	desv= desv + ((int(el)-suma[1]/len(columnas[1]))**2)
print(f'Desviacion Estándar #Personas: {round((desv/len(columnas[1]))**(1/2) ,2)}')
