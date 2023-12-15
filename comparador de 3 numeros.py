Num1 = int(input("ingrese el primer número: "))
Num2 = int(input("ingrese el segundo número: "))
Num3 = int(input("ingrese el tercer número: "))
conc = Num1,Num2,Num3
sum= Num1+Num2+Num3
if (Num1==Num2==Num3):
    print("los tres números son iguales")
elif(Num2==Num1):
    print("El número diferente es: "+str(Num3))
elif(Num2==Num3):
    print("El número diferente es: "+str(Num1))
elif(Num3==Num1):
    print("El número diferente es: "+str(Num2))
elif(Num1>Num2 and Num1>Num3):
    print("La suma de los 3 números es: ",sum)
elif(Num2>Num1 and Num2>Num3):
    print("La multiplicacion de los 3 números es: "+str(Num1* Num2* Num3))
elif(Num3>Num1 and Num3>Num2):
    print("La concatenación de los 3 números es: ", conc)