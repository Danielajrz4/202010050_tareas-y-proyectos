Palabra = input("Ingresar una palabra en mínuscula: ")  #se asigna a una variable la palabra a contar
a="a" # se le asigna a una variable lo que queremos que cuente
e="e"
i="i"
o="o"
u="u"
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
count_a = Palabra.count(a)  #se cuenta la cantidad de variables que hay dentro de la palabra
count_e = Palabra.count(e)
count_i = Palabra.count(i)
count_o = Palabra.count(o)
count_u = Palabra.count(u)
Suma_vocal = count_a+count_e+count_i+count_o+count_u
print("La palabra "+str(Palabra)+" tiene "+str(Suma_vocal)+" vocales.") #se imprimen la cantidad de veces que se repite cada vocal
