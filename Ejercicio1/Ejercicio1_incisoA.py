a = open("D:/Tareas/INF354/Datasets/StudentsPerformance.csv", 'r', encoding='utf8')
a.readline()
#Leeremos 50 registros Analizando notas de estudiantes columnas 6, 7 y 8 
suma = [0, 0, 0]
#moda={'0':0}
moda=[{'0':0},{'0':0},{'0':0}]
notas=[[],[],[]]
for i in range(50):
	e=a.readline().split(",")
	#Media
	suma[0]=int(e[5]) + suma[0]
	suma[1]=int(e[6]) + suma[1]
	suma[2]=int(e[7]) + suma[2]
	notas[0].append(int(e[5]))
	notas[1].append(int(e[6]))
	notas[2].append(int(e[7]))
	moda[0][e[5]] = moda[0].get(e[5], 0)+1
	moda[1][e[6]] = moda[1].get(e[6], 0)+1
	moda[2][e[7]] = moda[2].get(e[7], 0)+1
print("MEDIA".center(20, '°'))
print(f'Matemáticas: {round(suma[0]/50, 2)}\nLiteratura: {round(suma[1]/50, 2)}\nEscritura: {round(suma[2]/50, 2)}')
print("MODA".center(20, '°'))
columna=1
for m in moda:
	moda1 = [key for key, value in m.items()
                      if value == max(m.values())]
	print(f'Columna {columna}: ')
	for e in moda1:
		print(str(e), end="  ")
	print("")                      
	columna+=1
desv=0
for el in notas[0]:
	desv= desv + (el-suma[0]/50)**2
print(f'Desviacion Estándar Matemáticas: {round((desv/50)**(1/2) ,2)}')
desv=0
for el in notas[1]:
	desv= desv + (el-suma[1]/50)**2
print(f'Desviacion Estándar Literatura: {round((desv/50)**(1/2) ,2)}')
desv=0
for el in notas[2]:
	desv= desv + (el-suma[2]/50)**2
print(f'Desviacion Estándar Escritura: {round((desv/50)**(1/2) ,2)}')

