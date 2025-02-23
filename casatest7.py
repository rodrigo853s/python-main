def convertirMayusculas(texto):
    return texto.upper()

def convertirMinusculas(texto):
    return texto.lower()

def concatenar(texto1, texto2):
    resultado = texto1 + texto2
    return resultado

def mostrarMenu():
    print("Seleccione una opción:")
    print("1 - Convertir MAYÚSCULAS")
    print("2 - Convertir minúsculas")
    print("3 - Concatenar textos")


# PROGRAMA PRINCIPAL

print("Introduzca un texto")
valor = input()

mostrarMenu()

print("Seleccione una opción: ")
opcion = int(input())
#resultado = ""


if (opcion == 1):
    resultado = convertirMayusculas(valor)
    print(resultado)
elif (opcion == 2):
    resultado = convertirMinusculas(valor)
    print(resultado)
else:
    print ("Dame otro texto")
    aux2 = input()
    resultado = concatenar(valor, aux2)
    print(resultado)