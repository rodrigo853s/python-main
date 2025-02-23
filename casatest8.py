def metodoSumar(num1, num2):
    return num1 + num2

def metodoRestar(num1, num2):
    return num1 - num2

def metodoMultiplicar(num1, num2):
    return num1 * num2

def menu():
    print("Seleccione una opción: ")
    print("1 - Sumar números")
    print("2 - Restar números")
    print("3 - Multiplicar números")


# PROGRAMA PRINCIPAL

print("Dame un número")
numero1 = int(input())

print("Dame otro número")
numero2 = int(input())

menu()
opcion = int(input())

if (opcion == 1):
    res = metodoSumar(numero1, numero2)

elif (opcion == 2):
    res = metodoRestar(numero1, numero2)

else:
    res = metodoMultiplicar(numero1, numero2)

print(res)
