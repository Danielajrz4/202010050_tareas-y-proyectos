##############################
########  programa 5  ########
##############################




import psycopg2
from tabulate import tabulate

def ingreso():
    try:
        codigo = int(input("ingrese el codigo de la venta: "))
        venta = int(input("ingrese la cantidad de la venta en Q: "))
        desc = input("Ingrese artículo vendido: ")
        try:
            conexion = psycopg2.connect(     
                dbname = "monitoreo_ventas"                            
               )
            cursor = conexion.cursor()
            cursor.execute("insert into ventas(codgio,venta,descripcion) values("+str(codigo)+","+str(venta)+",'"+desc+"');")
            conexion.commit()       
            print("La venta fue registrada exitosamente")                     
        except:
            print("Error en la conexion \n")
    except: 
        print("ERROR, Ingrese valores válidos")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "monitoreo_ventas"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from ventas; ")
            print (tabulate(cursor, headers= ["codigo", "venta","descripcion"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

def find():
        try:
            coddd=int(input("Ingrese el codigo de la venta para observar su información su orden: "))
            try:
                conexion = psycopg2.connect(     
                    dbname = "monitoreo_ventas"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from ventas where codgio ="+str(coddd)+"; ")
                print (tabulate(cursor, headers= ["codigo", "venta","descripcion"], tablefmt="psql", numalign = "center"))
            except:
                print("Error en la conexion \n")
        except:
            print("Codigo no existente")

def clear():
    try:
        conexion = psycopg2.connect(     
            dbname = "monitoreo_ventas"
            )
        cursor = conexion.cursor()
        cursor.execute("delete from ventas; ")
        conexion.commit()
        print ("Historial borrado exitosamente.\n")
    except:
        print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Registrar venta \n'F' Buscar venta \n'H' Ver historial \n'C' Borrar historial \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion=='F':
        find()
    elif opcion=='H':
        Historial()
    elif opcion=='C':
        clear()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")