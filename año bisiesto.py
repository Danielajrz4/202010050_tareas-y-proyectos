import psycopg2
from tabulate import tabulate
def ingreso():
    año = int(input("Introduce un año: "))
    if (año % 4) == 0:
        if (año % 100) == 0:
            if (año % 400) == 0:
                print("El año es bisiesto")
                try:
                    conexion = psycopg2.connect(     
                        dbname = "bisono"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into bisono(anio,bisiesto) values("+str(año)+",'si');")
                    conexion.commit()
                except:
                    print("Error en la conexion \n")
            else:
                print("El año no es bisiesto")
                try:
                    conexion = psycopg2.connect(     
                        dbname = "bisono"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into bisono(anio,bisiesto) values("+str(año)+",'no');")
                    conexion.commit()
                except:
                    print("Error en la conexion \n")
        else:
            print("El año es bisiesto.")
            try:
                    conexion = psycopg2.connect(     
                        dbname = "bisono"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into bisono(anio,bisiesto) values("+str(año)+",'si');")
                    conexion.commit()
            except:
                    print("Error en la conexion \n")
    else:
        print("El año no es bisiesto.")
        try:
                    conexion = psycopg2.connect(     
                        dbname = "bisono"
                        )
                    cursor = conexion.cursor()
                    cursor.execute("insert into bisono(anio,bisiesto) values("+str(año)+",'no');")
                    conexion.commit()
        except:
                    print("Error en la conexion \n")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "bisono"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from bisono; ")
            print (tabulate(cursor, headers= ["año", "bisiesto"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar año \n'B' Ver historial \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")