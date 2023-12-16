##############################
########  programa 3  ########
##############################


import psycopg2
from tabulate import tabulate

def ingreso():
    try:
        porducto = input("ingrese el nombre del producto: ")
        cantidad = int(input("ingrese la cantidad de productos existentes: "))
        try:
            conexion = psycopg2.connect(     
                dbname = "inventario"                            
               )
            cursor = conexion.cursor()
            cursor.execute("insert into inventario(producto,cantidad) values('"+porducto+"',"+str(cantidad)+");")
            conexion.commit()       
            print("El producto fue agregado exitosamente")                     
        except:
            print("Error en la conexion \n")
    except: 
        print("ERROR, Ingrese valores válidos")

def Update():
    try:
        prod = input("Ingrese su nombre para editar la cantidad: ")
        nwcant= int(input("Ingrese la cantidad: "))

        try:
            conexion = psycopg2.connect(     
                dbname = "inventario"
                )
            cursor = conexion.cursor()
            cursor.execute("update inventario set cantidad='"+str(nwcant)+"' where producto= '"+prod+"'; ")
            conexion.commit()
            print ("cantidad del producto actualizada correctamente.\n")
        except:
            print("Error en la conexion \n")
    except:
        print("Error, ingrese valores válidos")

def borrardato():
    try:
        nnnombre= input("Ingrese el nombre del producto que quiere eliminar: ")
        try:
            conexion = psycopg2.connect(     
                dbname = "inventario"
                )
            cursor = conexion.cursor()
            cursor.execute("delete from inventario where producto= '"+nnnombre+"'; ")
            conexion.commit()
            print ("El producto fue eliminado correctamente.\n")
        except:
            print("Error en la conexion \n")
    except:
        print("Error, ingrese valores válidos")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "inventario"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from inventario; ")
            print (tabulate(cursor, headers= ["producto", "cantidad"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

def clear():
    try:
        conexion = psycopg2.connect(     
            dbname = "inventario"
            )
        cursor = conexion.cursor()
        cursor.execute("delete from inventario; ")
        conexion.commit()
        print ("Historial borrado exitosamente.\n")
    except:
        print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar producto \n'B' Ver historial \n'U' Actualizar cantidad de un producto \n'G' Borrar un producto \n'F' Borrar historial \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion=='B':
        Historial()
    elif opcion=='U':
        Update()
    elif opcion=='G':
        borrardato()
    elif opcion=='F':
        clear()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")