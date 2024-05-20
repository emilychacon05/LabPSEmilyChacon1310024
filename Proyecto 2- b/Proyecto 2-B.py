# Función para validar una posición en el tablero de ajedrez
def validar_posicion(posicion):
    if len(posicion) != 2:
        print("La posición debe tener dos caracteres.")
        return False
    letra, numero = posicion
    if letra.lower() not in 'abcdefgh' or numero not in '12345678':
        print("Posición inválida.")
        return False
    return True

# Función para imprimir el tablero de ajedrez de manera creativa
def imprimir_tablero():
    print("  a b c d e f g h")
    print(" ┌─┬─┬─┬─┬─┬─┬─┬─┐")
    for i in range(8):
        print(f"{8 - i}|", end="")
        for j in range(8):
            if (i + j) % 2 == 0:
                print("░", end="")
            else:
                print(" ", end="")
            if tablero[i][j] == '':
                print(" |", end="")
            else:
                print(tablero[i][j][0][0], end="|")
        print(f" {8 - i}")
        if i < 7:
            print(" ├─┼─┼─┼─┼─┼─┼─┼─┤")
    print(" └─┴─┴─┴─┴─┴─┴─┴─┘")

# Define el tablero de ajedrez como una matriz de 8x8
tablero = [['' for _ in range(8)] for _ in range(8)]
piezas_agregadas = []

# Lista de tipos de piezas válidas
tipos_validos = ['alfil', 'peon', 'caballo', 'torre', 'reina', 'rey']


def ingresar_cualquier_pieza_valida(tipo_pieza, color, posicion):
    # Verificar si el tipo de pieza es válido
    if tipo_pieza.lower() not in tipos_validos:
        print("Tipo de pieza inválido.")
        return False

    # Validar la posición
    if not validar_posicion(posicion):
        print("Posición inválida.")
        return False

    letra, numero = posicion
    fila = ord(letra) - ord('a')
    columna = int(numero) - 1

    # Verificar si ya hay una pieza en la posición
    if tablero[fila][columna] != '':
        print("Ya hay una pieza en esta posición.")
        return False

    # Agregar la pieza al tablero y a la lista de piezas agregadas
    tablero[fila][columna] = (tipo_pieza, color)
    piezas_agregadas.append((tipo_pieza, color, posicion))
    return True

# Función para obtener los movimientos válidos de un caballo
def posibles_posiciones_del_caballo(color, posicion):
    letra, numero = posicion
    fila = ord(letra) - ord('a')
    columna = int(numero) - 1
    movimientos = []
    movimientos_formato = []

    # Generar los movimientos posibles del caballo
    for df, dc in [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]:
        nueva_fila = fila + df
        nueva_columna = columna + dc
        # Verificar si la nueva posición está dentro del tablero
        if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
            pieza = tablero[nueva_fila][nueva_columna]
            # Agrega la posición a la lista de movimientos válidos del caballo
            # solo si está vacía o tiene una pieza del color opuesto
            if pieza == '' or pieza[1] != color:
                movimientos.append((chr(nueva_fila + ord('a')), nueva_columna + 1))
                if pieza == '':
                    movimientos_formato.append(f"{chr(nueva_fila + ord('a'))}{nueva_columna + 1}, vacía")
                else:
                    movimientos_formato.append(f"{chr(nueva_fila + ord('a'))}{nueva_columna + 1} con {pieza[0]} {pieza[1]}")
    return movimientos, movimientos_formato


# Función para validar una entrada entera
def validar_numero_entero(valor):
    while True:
        if valor.isdigit():
            return int(valor)
        else:
            print("Por favor, ingresa un entero válido.")
            valor = input("Ingresa un entero: ")


# Función para validar una entrada de color
def color_de_pieza(color):
    while color.lower() not in ['blanco', 'negro']:
        print("Color inválido. Por favor, ingresa 'blanco' o 'negro'.")
        color = input("Ingresa el color de la pieza (blanco/negro): ")
    return color

# Solicitar al usuario el número de piezas a agregar
N = validar_numero_entero(input("Ingresa el número de piezas a agregar: "))

# Iterar N veces para agregar las piezas al tablero
for _ in range(N):
    # Solicitar al usuario el tipo de pieza
    tipo_pieza = input("Ingresa el tipo de pieza: ").lower()

    # Validar que el tipo de pieza sea válido
    while tipo_pieza not in tipos_validos:
        print("Tipo de pieza inválido.")
        tipo_pieza = input("Ingresa el tipo de pieza: ").lower()

    # Solicitar al usuario el color de la pieza
    color = color_de_pieza(input("Ingresa el color de la pieza (blanco/negro): "))

    # Solicitar al usuario la posición de la pieza
    posicion = input("Ingresa la posición de la pieza (por ejemplo, a1): ")
    if not validar_posicion(posicion):
        print("Posición inválida.")
        continue

    # Validar y agregar la pieza al tablero
    while not ingresar_cualquier_pieza_valida(tipo_pieza, color, posicion):
        print("No se pudo agregar la pieza. Por favor, intenta nuevamente.")
        tipo_pieza = input("Ingresa el tipo de pieza: ").lower()
        while tipo_pieza not in tipos_validos:
            print("Tipo de pieza inválido.")
            tipo_pieza = input("Ingresa el tipo de pieza: ").lower()
        color = color_de_pieza(input("Ingresa el color de la pieza (blanco/negro): "))
        posicion = input("Ingresa la posición de la pieza (por ejemplo, a1): ")
        if not validar_posicion(posicion):
            print("Posición inválida.")

# Imprimir el tablero de ajedrez
imprimir_tablero()

# Solicitar al usuario el color del caballo
color_caballo = color_de_pieza(input("Ingresa el color del caballo: "))

# Solicitar al usuario la posición del caballo
posicion_caballo = input("Ingresa la posición del caballo (por ejemplo, a1): ")
if not validar_posicion(posicion_caballo):
    print("Posición inválida.")
else:
    # Obtener los movimientos válidos del caballo
    posibles_posiciones_del_caballo, posibles_posiciones_del_caballo_formato = posibles_posiciones_del_caballo(color_caballo, posicion_caballo)

    # Mostrar los movimientos válidos del caballo
    print("Los movimientos válidos para el caballo son: ", posibles_posiciones_del_caballo)
    print("Los movimientos válidos para el caballo en formato 1 son: ")
    for i in range(len(posibles_posiciones_del_caballo_formato)):
        movimiento = posibles_posiciones_del_caballo_formato[i]
        print(f"{i + 1}. {movimiento}")
