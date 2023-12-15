from math import pi
import psycopg2
from tabulate import tabulate
def ingreso():
    op = " "
    print("Bienvenido a la caluladora de áreas de figuras")
    while op != 'SALIR':
        print("por favor ingrese unicamente el nombre de la figura (sin tildes) a calcular \n1. Círculo \n2. Triángulo \n3. Cuadrado \n4. Rectángulo \n5. Salir")
        op = input("Opcion: ").upper ()
        if op == 'CIRCULO':
            radio=int(input("ingrese el valor del radio del cirulo: "))
            areacirc= pi*(radio**2)
            print("El área del circulo es: "+ str(areacirc))
            try:
                                conexion = psycopg2.connect(     
                                    dbname = "figuras"
                                    )
                                cursor = conexion.cursor()
                                cursor.execute("insert into circulo(radio, area) values("+str(radio)+","+str(areacirc)+");")
                                conexion.commit()     
                                
            except:
                                print("Error en la conexion \n")
        elif op=='TRIANGULO':
            base=int(input("ingrese el valor de la base del triangulo: "))
            altura=int(input("ingrese el valor de la alura del triangulo: "))
            areatrian= (base*altura)/2
            print("El área del triangulo es: "+ str(areatrian))
            try:
                                conexion = psycopg2.connect(     
                                    dbname = "figuras"
                                    )
                                cursor = conexion.cursor()
                                cursor.execute("insert into triangulo(base,altura,area) values("+str(base)+","+str(altura)+","+str(areatrian)+");")
                                conexion.commit()     
                                
            except:
                                print("Error en la conexion \n")
        elif op=='CUADRADO':
            lado=int(input("ingrese el valor de un lado del cuadrado: "))
            areacuad= (lado**2)
            print("El área del cuadrado es: "+ str(areacuad))
            try:
                                conexion = psycopg2.connect(     
                                    dbname = "figuras"
                                    )
                                cursor = conexion.cursor()
                                cursor.execute("insert into cuadrado(lado,area) values("+str(lado)+","+str(areacuad)+");")
                                conexion.commit()     
                                
            except:
                                print("Error en la conexion \n")
        elif op=='RECTANGULO':
            lado1=int(input("ingrese el valor de un lado del rectangulo: "))
            lado2=int(input("ingrese el valor de lado diferene al ya ingresado: "))
            arearect= (lado1*lado2)
            print("El área del rectangulo es: "+ str(arearect))
            try:
                                conexion = psycopg2.connect(     
                                    dbname = "figuras"
                                    )
                                cursor = conexion.cursor()
                                cursor.execute("insert into rectangulo(lado1,lado2,area) values("+str(lado1)+","+str(lado2)+","+str(arearect)+");")
                                conexion.commit()     
                                
            except:
                                print("Error en la conexion \n")
        elif op=='SALIR':
            break 
        else:
            print("Opcion no válida, ingrese unicamente el nombre de la figura mostradas en el menú")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "figuras"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from circulo; ")
            print (tabulate(cursor, headers= ["radio", "area"], tablefmt="psql", numalign = "center"))
            cursor = conexion.cursor()
            cursor.execute("SELECT * from triangulo; ")
            print (tabulate(cursor, headers= ["base", "altura","area"], tablefmt="psql", numalign = "center"))
            cursor = conexion.cursor()
            cursor.execute("SELECT * from cuadrado; ")
            print (tabulate(cursor, headers= ["lado", "area"], tablefmt="psql", numalign = "center"))
            cursor = conexion.cursor()
            cursor.execute("SELECT * from rectangulo; ")
            print (tabulate(cursor, headers= ["lado 1", "lado 2", "area"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

def clear():
    try:
        conexion = psycopg2.connect(     
            dbname = "figuras"
            )
        cursor = conexion.cursor()
        cursor.execute("delete from circulo; ")
        conexion.commit()
        cursor = conexion.cursor()
        cursor.execute("delete from cuadrado; ")
        conexion.commit()
        cursor = conexion.cursor()
        cursor.execute("delete from triangulo; ")
        conexion.commit()
        cursor = conexion.cursor()
        cursor.execute("delete from rectangulo; ")
        conexion.commit()
        print ("Historial borrado exitosamente.\n")
    except:
        print("Error en la conexion \n")


opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar número \n'B' Ver historial \n'F' Borrar historial \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion=='B':
        Historial()
    elif opcion=='F':
        clear()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")