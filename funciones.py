def ObtenerAreaTriangulo(base, altura):
 area = (base * altura) / 2
 return area
def ObtenerAreaCuadrado(lado):
 area = lado * lado
 return area
def ObtenerAreaRectangulo(base, altura):
 area = base * altura
 return area
def ObtenerAreaCirculo(radio):
 area = 3.14159 * radio * radio
 return area
print("Semana No. 12: Ejercicio 1")
# Menú de opciones para calcular áreas
while True:
 print("\nMenú de opciones:")
 print("a. Área de triángulo")
 print("b. Área de cuadrado")
 print("c. Área de rectángulo")
 print("d. Área de círculo")
 print("e. Salir")
 opcion = input("Ingrese la opción que desea: ")
 if opcion == "a":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    areaTriangulo = ObtenerAreaTriangulo(base, altura)
print("El área del triángulo es:", areaTriangulo)
        elif opcion == "b":
        lado = float(input("Ingrese el lado del cuadrado: "))
 areaCuadrado = ObtenerAreaCuadrado(lado)
 print("El área del cuadrado es:", areaCuadrado)
        elif opcion == "c":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        areaRectangulo = ObtenerAreaRectangulo(base, altura)
                print("El área del rectángulo es:", areaRectangul 
                      elif opcion == "d":
 radio = float(input("Ingrese el radio del círculo: "))
 areaCirculo = ObtenerAreaCirculo(radio)
 print("El área del círculo es:", areaCirculo)
 elif opcion == "e":
 break
 else:
 print("Opción no válida. Intente nuevamente.")