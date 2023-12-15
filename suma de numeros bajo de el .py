while(True):
    num = int(input("ingrese un número para sumar todos sus números debajo de el: "))
    ASX=[]
    for i in range(0, num+1):
        ASX.append(i)
    print("la lista de valores a sumar son: "+str(ASX))
    sum = 0
    for n in ASX:
        sum += n
    print ("la sumatoria final es: "+str(sum))