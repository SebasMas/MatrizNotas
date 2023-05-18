import numpy as np
import pandas as pd
import random

#Creamos dos variables para las dimensiones X y Y.  n = notas, a = alumnos.
n = 4
a = 5


#Creamos la matriz vacía que tomará las dimensiones a,n. A su vez, establecemos que la matriz almacenará datos tipo float.
plantilla = np.empty((a,n), dtype=float)

#Creamos un ciclo para llenar cada índice y subíndice con valores random entren 0 y 5.
for i in range(a):
    for j in range(n):
        plantilla[i][j] = float(random.randint(0,5))
            
#Creamos un dataframe con la librería pandas que nos permitirá crear una tabla visualmente decente.
df = pd.DataFrame(plantilla, columns=["Nota " + str(i) for i in range(n)],  index=["Alumno " + str(i) for i in range(a)])
print(df)

#Creamos un ciclo que permita al usuario elegir entre varias opciones indefinidamente

while True:
    print(" ")
    print("---- OPCIONES ----")
    print("1 - Máximos, mínimos y promedios")
    print("2 - Modificar notas")
    print("3 - Eliminar")
    print("-------------------------------")
    
    option = int(input("Ingrese una opción: "))
    
    
    if option == 1:
               
        for i in range(len(plantilla)):
            #Iniciamos las variables max, min y promedio para una correcta comparación
            max = 0
            min = 5
            promedio = 0
            for j in range(len(plantilla[0])):
                if plantilla[i][j] > max:
                    max = plantilla[i][j]
                if plantilla[i][j] < min:
                    min = plantilla[i][j]
                promedio +=  plantilla[i][j] #Tras ubicarse en i, se sumará a "promedio" cada valor en j (nota), es decir, los valores dentro del índice i (Alumno)
            promedio = promedio / n
            
            #Imprimimos en pantalla el máximo, mínimo y promedio de cada alumno
            print(f"---- ALUMNO {i+1} ----")
            print("Mínimo: ",min)
            print("Máximo: ",max)
            print("Promedio: ", promedio)
            print("-----------------------")
            
    elif option == 2:
        #Imprimimos la planntilla de estudiantes para mejor experiencia de usuario
        print(df)
        
        #Preguntamos por el índice del estudiante (código), el subíndice de la nota (posicNota) y la nueva nota a asignar (nuevaNota)
        codigo = int(input("Escriba el número del alumno: "))
        posicNota = int(input("¿Cuál nota desea cambiar?: "))
        nuevaNota = float(input("Ingrese una nueva nota: "))
        
        #Creamos un ciclo para encontrar el índice del estudiante en cuestión
        for i in range(len(plantilla)):
            if i == codigo:
                #Creamos otro ciclo adentro para hallar el subíndice de la nota (posicNota)
                for j in range(len(plantilla)):
                    if j == posicNota:
                        plantilla[i][j] = nuevaNota #La nota (j) del alumno (i) dentro de la matriz (plantilla) será igual a la nueva Nota escrita anteriormente             
        print(df)
        
    elif option == 3:
        exit()