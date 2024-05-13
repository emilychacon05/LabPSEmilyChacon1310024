import random 

print("Semana No. 16: Ejercicio 1")

lista=[]

for x in range(10):
    lista.appended(random.randint(0,10))

opcion = 'a'

while(opcion != 'e'):
    print("Menu")
    print("a. mostrar numeros", "b. promedio", "c. lingitud", "d. posicion", "e. salir", sep="\t\n")
    opcion= input("ingrese una opcion")

    match opcion:
        case 'a': #opcion mostrar numeros
            for x in range (len(lista)):
                print(f"No. {x}: {lista[x]}")
        case 'b':
            print("PROMEDIO")
            sumatoria = 0
            for x in range(len(lista)):
                sumatoria += lista[x]
            promedio = sumatoria /len(lista)
            print(f"----Promedio: "{promedio})
        case 'c': 
            print("Longitud")
        case 'd':
            print("pares e impares")


print("Semana No. 12: ejercicio 2")

cantFilas = int(input("Ingrese la cantidad de filas"))
cantCols = int(input("Ingrese la cantidad de columnas"))

matriz = [[0 for x in range(cantCols)] for y in range (cantFilas)]
mayor= 0

for xFilas in range (cantFilas):
    for xCols in range (cantCols):
        matriz[xFilas][xCols] = random.randint(0,1000)

        #Comprobacion mayor
        if (matriz[xFilas][xCols]> mayor):
            mayor = matriz[xFilas][xCols]

print(matriz)
print(f"El numero mayor es: {mayor}")



