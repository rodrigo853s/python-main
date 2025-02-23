print("Dame un numero con 4 caracteres")
numero = str(input())
longitud = len(numero)
suma = 0
for i in range(longitud):
    letra = int(numero[i])
    suma = suma + letra
print ("La suma de todos los números es " + str(suma))