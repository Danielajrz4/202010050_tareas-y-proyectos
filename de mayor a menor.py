while(True):
    Num1 = int(input("ingrese primer número: "))
    Num2 = int(input("ingrese el segundo número: "))
    if(Num1>Num2):
        for i in range(Num1, Num2-1,-1):
            print(i)
    if(Num2>Num1):
        for i in range(Num2, Num1-1,-1):
            print(i)