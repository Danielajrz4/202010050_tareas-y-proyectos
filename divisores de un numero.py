num = int(input("ingrese un numero para conseguirle sus divisores exactos: "))
div=[i for i in range(1, num+1) if num % i !=0]
print(div)