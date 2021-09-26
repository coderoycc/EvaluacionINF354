a = open("D:/Tareas/INF354/Datasets/OlimpiadasGenero.csv", 'r', encoding='utf8')
print(a.readline())
#Leeremos participantes por genero 2, 3, 4 
suma = [0, 0, 0]
#moda={'0':0}
moda=[{'0':0},{'0':0},{'0':0}]
columnas=[[],[],[]]
for linea in a:
	e=linea.split(",")
	#Media
	suma[0]=int(e[1]) + suma[0]
	suma[1]=int(e[2]) + suma[1]
	suma[2]=int(e[3]) + suma[2]
	columnas[0].append(int(e[1]))
	columnas[1].append(int(e[2]))
	columnas[2].append(int(e[3]))
	moda[0][e[1]] = moda[0].get(e[1], 0)+1
	moda[1][e[2]] = moda[1].get(e[2], 0)+1
	moda[2][e[3]] = moda[2].get(e[3], 0)+1
print("MEDIA".center(20, '°'))
print(f'Mujeres: {round(suma[0]/len(columnas[0]), 2)}\nVarones: {round(suma[1]/len(columnas[0]), 2)}\nParticipacion: {round(suma[2]/len(columnas[0]), 2)}')
print("MODA".center(20, '°'))
columna=1
for m in moda:
	print(f'Columna: {columna}')
	for key, value in m.items():
		if value == max(m.values()):
			print(key)
			break
	columna+=1
desv=0
for el in columnas[0]:
	desv= desv + ((el-suma[0]/len(columnas[0]))**2)
print(f'Desviacion Estándar Mujeres: {round((desv/len(columnas[0]))**(1/2) ,2)}')
desv=0
for el in columnas[1]:
	desv= desv + ((el-suma[1]/len(columnas[1]))**2)
print(f'Desviacion Estándar Varones: {round((desv/len(columnas[1]))**(1/2) ,2)}')
desv=0 
for el in columnas[2]:
	desv= desv + ((el-suma[2]/len(columnas[2]))**2)
print(f'Desviacion Estándar Participación: {round((desv/len(columnas[2]))**(1/2) ,2)}')
