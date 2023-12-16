##############################
########  programa 4  ########
##############################



import psycopg2
from tabulate import tabulate

def ingreso():
    try:
        codigo = int(input("ingrese el codigo del pedido: "))
        pedido = input("ingrese el pedido: ")
        try:
            conexion = psycopg2.connect(     
                dbname = "pedidos"                            
               )
            cursor = conexion.cursor()
            cursor.execute("insert into pedidos(codigo,pedido) values("+str(codigo)+",'"+pedido+"');")
            conexion.commit()       
            print("El pedido fue agregado exitosamente")                     
        except:
            print("Error en la conexion \n")
    except: 
        print("ERROR, Ingrese valores válidos")

def Update():
    try:
        cod = int(input("Ingrese el codigo del pedido para actualizarlo: "))
        nwped= input("Ingrese el nuevo pedido: ")

        try:
            conexion = psycopg2.connect(     
                dbname = "pedidos"
                )
            cursor = conexion.cursor()
            cursor.execute("update pedidos set pedido='"+nwped+"' where codigo= "+str(cod)+"; ")
            conexion.commit()
            print ("pedido actualizado correctamente.\n")
        except:
            print("Error en la conexion \n")
    except:
        print("Error, ingrese valores válidos")

def borrardato():
    try:
        codd= int(input("Ingrese el codigo del pedido a eliminar: "))
        try:
            conexion = psycopg2.connect(     
                dbname = "pedidos"
                )
            cursor = conexion.cursor()
            cursor.execute("delete from pedidos where codigo= "+str(codd)+"; ")
            conexion.commit()
            print ("El pedido fue eliminado correctamente.\n")
        except:
            print("Error en la conexion \n")
    except:
        print("Error, ingrese valores válidos")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "pedidos"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from pedidos; ")
            print (tabulate(cursor, headers= ["codigo", "pedido"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

def find():
        try:
            coddd=int(input("Ingrese el codigo del pedido para revisar su orden: "))
            try:
                conexion = psycopg2.connect(     
                    dbname = "pedidos"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from pedidos where codigo ="+str(coddd)+"; ")
                print (tabulate(cursor, headers= ["codigo", "pedido"], tablefmt="psql", numalign = "center"))
            except:
                print("Error en la conexion \n")
        except:
            print("Codigo no existente")

def clear():
    try:
        conexion = psycopg2.connect(     
            dbname = "pedidos"
            )
        cursor = conexion.cursor()
        cursor.execute("delete from pedidos; ")
        conexion.commit()
        print ("Historial borrado exitosamente.\n")
    except:
        print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar pedido \n'F' buscar pedido \n'H' Ver historial \n'U' Actualizar un pedido existente \n'G' Borrar un producto \n'C' Borrar historial \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion=='F':
        find()
    elif opcion=='H':
        Historial()
    elif opcion=='U':
        Update()
    elif opcion=='G':
        borrardato()
    elif opcion=='C':
        clear()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")