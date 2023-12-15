import psycopg2
from tabulate import tabulate

def Ingreso(): 
        try:
            año= int(input("ingrese el año del vehiculo a registrar: "))
            kmt=int(input("ingrese el kilometraje de vehículo: "))
            if(año<=2007 and kmt>=20000):
                print("renovar\n")
                try:
                    conexion = psycopg2.connect(     
                        dbname = "reg_taxis"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into reg_taxis(modelo,kilometraje,estado) values("+str(año)+","+str(kmt)+",'Renovar');")
                    conexion.commit()
                except:
                    print("Error en la conexion \n")
            elif(2007<año<2013 and kmt>=20000):
                print("mantenimiento\n")
                try:
                    conexion = psycopg2.connect(     
                        dbname = "reg_taxis"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into reg_taxis(modelo,kilometraje,estado) values("+str(año)+","+str(kmt)+",'Mantenimiento');")
                    conexion.commit()
                except:
                    print("Error en la conexion \n")
            elif(año>=2013 and kmt<10000):
                print("Optimas condiciones\n")
                try:
                    conexion = psycopg2.connect(     
                        dbname = "reg_taxis"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into reg_taxis(modelo,kilometraje,estado) values("+str(año)+","+str(kmt)+",'Optimas condiciones');")
                    conexion.commit()
                except:
                    print("Error en la conexion \n")
            else:
                print("Mecánico\n")
                try:
                    conexion = psycopg2.connect(     
                        dbname = "reg_taxis"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into reg_taxis(modelo,kilometraje,estado) values("+str(año)+","+str(kmt)+",'Mecánico');")
                    conexion.commit()
                except:
                    print("Error en la conexion \n")
        except:
            print("Por favor ingrese únicamente números\n")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "reg_taxis"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from reg_taxis; ")
            print (tabulate(cursor, headers= ["Modelo", "kilometraje","estado"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

def borrar():
    try:
        conexion = psycopg2.connect(     
            dbname = "reg_taxis"
            )
        cursor = conexion.cursor()
        cursor.execute("delete from reg_taxis; ")
        conexion.commit()
        print ("Historial borrado exitosamente.\n")
    except:
        print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar datos de vehiculo \n'B' Ver historial \n'C' Borrar historial\n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        Ingreso()
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break 
    elif opcion=='C':
        borrar()
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")