print("Dime un número")
num1 = int(input())
print("Dime otro número")
num2 = int(input())
if ( num1 > num2 ):
    print("El número " + str(num1) + " es mayor que " + str(num2))
elif ( num2 > num1 ):
    print("El número " + str(num2) + " es mayor que " + str(num1))
else:
    print("El número " + str(num2) + " es igual a " + str(num1))