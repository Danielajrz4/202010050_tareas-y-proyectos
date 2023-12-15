while(True):
    inic = int(input("ingrese el número de inicio para hacer el conteo: "))
    fin = int(input("ingrese el número final en el que acabará el conteo: "))
    for i in range(inic,fin+1,2):
        print(i)
