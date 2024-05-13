# Ejercicio 1: operaciones aritméticas
print("Ejercicio 1: operaciones aritméticas")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division_real = num1 / num2
division_entera = num1 // num2
division_modular = num1 % num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División real: {division_real}")
print(f"División entera: {division_entera}")
print(f"División modular: {division_modular}")

# Ejercicio 2: operaciones booleanas
print("\nEjercicio 2: operaciones booleanas")

mayor_que = num1 > num2
menor_que = num1 < num2
igualdad = num1 == num2
diferencia = num1 != num2

print(f"{num1} > {num2}: {mayor_que}")
print(f"{num1} < {num2}: {menor_que}")
print(f"{num1} == {num2}: {igualdad}")
print(f"{num1} != {num2}: {diferencia}") 

# Ejercicio 3: jerarquía de operadores
print("\nEjercicio 3: jerarquía de operadores")

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

expresion1 = a * b + c
expresion2 = a * (b + c)
expresion3 = a * b + c
expresion4 = 3 * a + 2 * b / c

print(f"a * b + c = {expresion1}")
print(f"a(b + c) = {expresion2}")
print(f"a * b + c = {expresion3}")
print(f"3a + 2b / c = {expresion4}")

