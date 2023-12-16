##############################
########  programa 9  ########
##############################


import psycopg2
from tabulate import tabulate

def ingreso():
    try:
        porducto = input("ingrese el nombre del producto: ")
        cant = int(input("ingrese la cantidad de productos existentes: "))
        precio = int(input("Ingrese el precio del producto: "))
        try:
            conexion = psycopg2.connect(     
                dbname = "inventario2"                            
               )
            cursor = conexion.cursor()
            cursor.execute("insert into inventario(producto,existencias,precio) values('"+porducto+"',"+str(cant)+","+str(precio)+");")
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
                dbname = "inventario2"
                )
            cursor = conexion.cursor()
            cursor.execute("update inventario set existencias='"+str(nwcant)+"' where producto= '"+prod+"'; ")
            conexion.commit()
            print ("cantidad del producto actualizada correctamente.\n")
        except:
            print("Error en la conexion \n")
    except:
        print("Error, ingrese valores válidos")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "inventario2"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from inventario; ")
            print (tabulate(cursor, headers= ["producto", "existencias","precio"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

def find():
        try:
            coddd=input("Ingrese el nombre del producto a consultar: ")
            try:
                conexion = psycopg2.connect(     
                    dbname = "inventario2"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from inventario where producto ='"+str(coddd)+"'; ")
                print (tabulate(cursor, headers= ["producto", "existencias","precio"], tablefmt="psql", numalign = "center"))
            except:
                print("Error en la conexion \n")
        except:
            print("Codigo no existente")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar producto \n'F' Consultar producto \n'B' Ver historial \n'U' Actualizar cantidad de un producto \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion =='F':
        find()
    elif opcion=='B':
        Historial()
    elif opcion=='U':
        Update()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")