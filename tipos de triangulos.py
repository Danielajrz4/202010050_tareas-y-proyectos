import psycopg2
from tabulate import tabulate

def ingreso():
    try:
        l1 = int(input("Ingrese el primer lado del triángulo: "))
        l2 = int(input("Ingrese el segundo lado del triángulo: "))
        l3 = int(input("Ingrese el tercer lado del triángulo: "))
        if (l1==l2 and l2==l3):
            print("Su triángulo es equilátero")
            try:
                conexion = psycopg2.connect(     
                    dbname = "triangulos"
                    )
                cursor = conexion.cursor()
                cursor.execute("insert into triangulos(lado1,lado2,lado3,triangulo) values("+str(l1)+","+str(l2)+","+str(l3)+",'equilatero');")
                conexion.commit()         
            except:
                        print("Error en la conexion \n")
        elif (l1==l2):
            print("Su triángulo es isósceles")
            try:
                        conexion = psycopg2.connect(     
                            dbname = "triangulos"
                            )
                        cursor = conexion.cursor()
                        cursor.execute("insert into triangulos(lado1,lado2,lado3,triangulo) values("+str(l1)+","+str(l2)+","+str(l3)+",'isosceles');")
                        conexion.commit()
            except:
                        print("Error en la conexion \n")
        elif (l1==l3):
            print("Su triángulo es isósceles")
            try:
                        conexion = psycopg2.connect(     
                            dbname = "triangulos"
                            )
                        cursor = conexion.cursor()
                        cursor.execute("insert into triangulos(lado1,lado2,lado3,triangulo) values("+str(l1)+","+str(l2)+","+str(l3)+",'isosceles');")
                        conexion.commit()
            except:
                        print("Error en la conexion \n")
        elif (l2==l3):
            print("Su triángulo es isósceles")
            try:
                        conexion = psycopg2.connect(     
                            dbname = "triangulos"
                            )
                        cursor = conexion.cursor()
                        cursor.execute("insert into triangulos(lado1,lado2,lado3,triangulo) values("+str(l1)+","+str(l2)+","+str(l3)+",'isosceles');")
                        conexion.commit()
            except:
                        print("Error en la conexion \n")
        else:
            print("Su triángulo es escaleno")
            try:
                        conexion = psycopg2.connect(     
                            dbname = "triangulos"
                            )
                        cursor = conexion.cursor()
                        cursor.execute("insert into triangulos(lado1,lado2,lado3,triangulo) values("+str(l1)+","+str(l2)+","+str(l3)+",'escaleno');")
                        conexion.commit()
            except:
                        print("Error en la conexion \n")
    except:
        print("Por favor ingrese solamente numeros.")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "triangulos"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from triangulos; ")
            print (tabulate(cursor, headers= ["lado 1", "lado 2","lado 3","triangulo"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar lados \n'B' Ver historial \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")