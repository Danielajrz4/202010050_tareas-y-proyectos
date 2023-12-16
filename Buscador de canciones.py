##############################
########  programa 11  #######
##############################

import psycopg2
from tabulate import tabulate

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "espoti"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from pl; ")
            print (tabulate(cursor, headers= ["Cancion", "Artista","Letra"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

def finda():
        try:
            coddd=input("Ingrese el nombre del artista a escuchar: ")
            try:
                conexion = psycopg2.connect(     
                    dbname = "espoti"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from pl where artista ='"+str(coddd)+"'; ")
                print (tabulate(cursor, headers= ["Cancion", "Artista","Letra"], tablefmt="psql", numalign = "center"))
            except:
                print("Error en la conexion \n")
        except:
            print("Codigo no existente")
 
def findc():
        try:
            coddd=input("Ingrese el nombre de la cancion a escuchar: ")
            try:
                conexion = psycopg2.connect(     
                    dbname = "espoti"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from pl where cancion ='"+str(coddd)+"'; ")
                print (tabulate(cursor, headers= ["Cancion", "Artista","Letra"], tablefmt="psql", numalign = "center"))
            except:
                print("Error en la conexion \n")
        except:
            print("Codigo no existente")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'B' Ver las canciones existentes \n'A' Buscar por el nombre de la cancion \n'F' Buscar por el nombre del artista \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        findc()
    elif opcion =='F':
        finda()
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")