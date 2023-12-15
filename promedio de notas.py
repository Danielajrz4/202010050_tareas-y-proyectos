import psycopg2
from tabulate import tabulate
notas=[]
nota=0
i=0
def ingreso():
        try:
            for i in range(0,3):
                nota=int(input("por favor ingrese una nota: "))
                notas.append(nota)
                if i==2:

                    print("Notas ingresadas: "+str(notas))
                    prom= sum(notas)/len(notas)
                    print("El promedio de las notas es: "+str(prom))
                    if (prom>=60):
                        print("Usted está APROBADO")
                        try:
                            conexion = psycopg2.connect(     
                                dbname = "promedios"
                                )
                            cursor = conexion.cursor()
                            cursor.execute("insert into promedios(nota1,nota2,nota3,promedio,resultado) values("+str(notas[0])+","+str(notas[1])+","+str(notas[2])+","+str(prom)+",'APROBADO');")
                            conexion.commit()     
                            
                        except:
                            print("Error en la conexion \n")
                            
                    elif(prom<60):
                        print("Usted está REPROBADO")
                        try:
                            conexion = psycopg2.connect(     
                                dbname = "promedios"
                                )
                            cursor = conexion.cursor()
                            cursor.execute("insert into promedios(nota1,nota2,nota3,promedio,resultado) values("+str(notas[0])+","+str(notas[1])+","+str(notas[2])+","+str(prom)+",'REPROBADO');")
                            conexion.commit()         

                        except:
                            print("Error en la conexion \n")
        except ValueError:
            print("por favor ingrese un número")

def Historial():
        try:
            conexion = psycopg2.connect(     
                dbname = "promedios"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from promedios; ")
            print (tabulate(cursor, headers= ["nota 1", "nota 2", "nota 3", "promedio", "resultado"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

opcion = " "
while opcion != 'Z':
                                    
    print("Seleccione una opción del siguiente menú: \n'A' Ingresar notas \n'B' Ver historial \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        ingreso()
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")
    