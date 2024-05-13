print("Semana No. 10: Ejercicio 1")

mesEntrada = int(input("Ingrese un número del 1-12: "))
mesSalida = ""

match mesEntrada:
    case 1:
        mesSalida = "Enero "
    case 2:
        mesSalida = "Febrero"
    case 3:
        mesSalida = "Marzo"
    case 4:
        mesSalida = "Abril"
    case 5:
        mesSalida = "Mayo"
    case 6:
        mesSalida = "Junio"
    case 7:
        mesSalida = "Julio"
    case 8:
        mesSalida = "Agosto"
    case 9:
        mesSalida = "Septiembre"
    case 10:
        mesSalida = "Octubre"
    case 11:
        mesSalida = "Noviembre"
    case 12:
        mesSalida = "Diciembre"
    
    case _:
        print("Error: El nuemero a ingresar debe estra contenido entre 1 y 12")

print(f"MES: {mesSalida}")


#Ejercicio2
def obtener_signo_zodiacal(dia, mes):
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    else:
        return "Capricornio"


dia = int(input("Ingrese el día de su fecha de nacimiento: "))
mes = int(input("Ingrese el mes de su fecha de nacimiento (en número): "))


signo = obtener_signo_zodiacal(dia, mes)


print("Su signo zodiacal es:", signo)
