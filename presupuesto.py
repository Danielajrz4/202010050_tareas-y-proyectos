##############################
########  programa 2  ########
##############################


import psycopg2
from tabulate import tabulate

def ingreso():
    try:
        gasto = input("ingrese en que se gastó: ")
        cantidad = int(input("ingrese la cantidad gastada en Q: "))
        try:
            conexion = psycopg2.connect(     
                dbname = "presupuesto"                            
               )
            cursor = conexion.cursor()
            cursor.execute("insert into presupuesto2(gasto,cantidad) values('"+gasto+"',"+str(cantidad)+");")
            conexion.commit()                            
        except:
            print("Error en la conexion \n")
    except: 
        print("ERROR, Ingrese valores válidos")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "presupuesto"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from presupuesto2; ")
            print (tabulate(cursor, headers= ["Gasto", "Cantidad en Q"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

def clear():
    try:
        conexion = psycopg2.connect(     
            dbname = "presupuesto"
            )
        cursor = conexion.cursor()
        cursor.execute("delete from presupuesto2; ")
        conexion.commit()
        print ("Historial borrado exitosamente.\n")
    except:
        print("Error en la conexion \n")

def acumulado():
    try:
        conexion = psycopg2.connect(     
            dbname = "presupuesto"
            )
        cursor = conexion.cursor()
        cursor.execute("select SUM(cantidad) from presupuesto2; ")
        conexion.commit()
    except:
        print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar gastos \n'V' Ver gastos acumulados \n'B' Ver historial \n'F' Borrar historial \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion=='V':
        acumulado()
    elif opcion=='B':
        Historial()
    elif opcion=='F':
        clear()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")