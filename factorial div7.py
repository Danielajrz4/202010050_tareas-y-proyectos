import psycopg2
from tabulate import tabulate
from math import factorial
def ingreso():
    try:
        num=int(input("Ingrese el númeroa dividir y sacar factorial: "))
        if num%7 == 0:
            fact= factorial(num)
            print("El factorial es: "+str(fact))
            try:
                    conexion = psycopg2.connect(     
                        dbname = "fact"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into fact(divisible,factorial) values('si',"+str(fact)+");")
                    conexion.commit()
            except:
                    print("Error en la conexion \n")
        else:
            print("El número ingresado no es divisible dentro de 7")
            try:
                    conexion = psycopg2.connect(     
                        dbname = "fact"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into fact(divisible,factorial) values('no','no cuenta');")
                    conexion.commit()
            except:
                    print("Error en la conexion \n")
    except:
        print("Ingrese un número")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "fact"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from fact; ")
            print (tabulate(cursor, headers= ["divisible", "Factorial"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar número \n'B' Ver historial \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")