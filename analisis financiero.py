##############################
########  programa 8  ########
##############################



import psycopg2
from tabulate import tabulate

def findc():
            try:
                conexion = psycopg2.connect(     
                    dbname = "empresas"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from claro; ")
                print (tabulate(cursor, headers= ["plan vendido", "Precio del plan en Q"], tablefmt="psql", numalign = "center"))
            except:
                print("Error en la conexion \n")

def findt():
            try:
                conexion = psycopg2.connect(     
                    dbname = "empresas"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from tigo; ")
                print (tabulate(cursor, headers= ["plan vendido", "Precio del plan en Q"], tablefmt="psql", numalign = "center"))
            except:
                print("Error en la conexion \n")

def findm():
            try:
                conexion = psycopg2.connect(     
                    dbname = "empresas"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from movistar; ")
                print (tabulate(cursor, headers= ["plan vendido", "Precio del plan en Q"], tablefmt="psql", numalign = "center"))
            except:
                print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú pera ver la informacion de esa empresa: \n'C' CLARO \n'T' TIGO \n'M' Movistar\n")
    opcion = input("Ingrese únicamente la letra inicial: ").upper ()
    if opcion == 'C':
        findc()
    elif opcion=='T':
        findt()
    elif opcion=='M':
        findm()
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")