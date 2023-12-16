##############################
########  programa 1  ########
##############################


import psycopg2
from tabulate import tabulate


def ingreso():
    try:   
        nombre=input("Ingrese su nombre: ")
        edad = int(input("ingrese su edad: "))
        genero= input("ingrese su genero: ")
        direccion= input("ingrese su direccion: ")
        try:
            conexion = psycopg2.connect(     
                dbname = "reg_estud"
                )
            cursor = conexion.cursor()
            cursor.execute("insert into reg_estud(nombre,edad,genero,direccion) values('"+nombre+"',"+str(edad)+",'"+genero+"','"+direccion+"');")
            conexion.commit()
        except:
            print("Error en la conexion \n")
    except:
        print("Ingrese valores válidos")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "reg_estud"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from reg_estud; ")
            print (tabulate(cursor, headers= ["nombre", "edad","genero","direccion"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

def clear():
    try:
        conexion = psycopg2.connect(     
            dbname = "reg_estud"
            )
        cursor = conexion.cursor()
        cursor.execute("delete from reg_estud; ")
        conexion.commit()
        print ("Historial borrado exitosamente.\n")
    except:
        print("Error en la conexion \n")

def Update():
    try:
        nnombre= input("Ingrese su nombre para editar la edad: ")
        nwedad= int(input("Ingrese su nueva edad: "))

        try:
            conexion = psycopg2.connect(     
                dbname = "reg_estud"
                )
            cursor = conexion.cursor()
            cursor.execute("update reg_estud set edad='"+str(nwedad)+"' where nombre= '"+nnombre+"'; ")
            conexion.commit()
            print ("Edad actualizada correctamente.\n")
        except:
            print("Error en la conexion \n")
    except:
        print("Error, ingrese valores válidos")

def borrardato():
    try:
        nnnombre= input("Ingrese su nombre para borrar sus datos: ")
        try:
            conexion = psycopg2.connect(     
                dbname = "reg_estud"
                )
            cursor = conexion.cursor()
            cursor.execute("delete from reg_estud where nombre= '"+nnnombre+"'; ")
            conexion.commit()
            print ("Sus datos se borraron correctamente.\n")
        except:
            print("Error en la conexion \n")
    except:
        print("Error, ingrese valores válidos")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar datos \n'B' Ver historial \n'U' Actualizar edad \n'G' Borrar datos de estudiante \n'F' Borrar historial \n'Z' salir\n")
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