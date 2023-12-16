##############################
########  programa 12  #######
##############################

import psycopg2
from tabulate import tabulate

def jugar():
    v=3
    for i in range(1,6):
        if (i==1):
            try:
                print("Vidas disponibles:"+str(v))
                conexion = psycopg2.connect(     
                    dbname = "preguntados"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from preguntados where numero =1; ")
                
                print (tabulate(cursor, headers= ["pregunta","No."], numalign = "center"))
                resp1=int(input("ingrese su respuesta: "))
                if (resp1== 60):
                    print("correcto.")
                    v+=1

                else:
                    print("Erroneo.")
                    v-=1

            except:
                print("Error en la conexion \n")
        elif (i==2):
            try:
                conexion = psycopg2.connect(     
                    dbname = "preguntados"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from preguntados where numero =2; ")
                print("Vidas disponibles:"+str(v))
                print (tabulate(cursor, headers= ["pregunta","No."], numalign = "center"))
                resp2=int(input("ingrese su respuesta: "))
                if (resp2== 8):
                    print("correcto.")
                    v+=1
                else:
                    print("Erroneo.")
                    v-=1
            except:
                print("Error en la conexion \n")
        elif (i==3):
            try:
                conexion = psycopg2.connect(     
                    dbname = "preguntados"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from preguntados where numero =3; ")
                print("Vidas disponibles:"+str(v))
                print (tabulate(cursor, headers= ["pregunta","No."], numalign = "center"))
                resp3=int(input("ingrese su respuesta: "))
                if (resp3== 4):
                    print("correcto.")
                    v+=1
                else:
                    print("Erroneo.")
                    v-=1
                    if(v==0):
                        break
            except:
                print("Error en la conexion \n")
        elif (i==4):
            try:
                conexion = psycopg2.connect(     
                    dbname = "preguntados"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from preguntados where numero =4; ")
                print("Vidas disponibles:"+str(v))
                print (tabulate(cursor, headers= ["pregunta","No."], numalign = "center"))
                resp4=int(input("ingrese su respuesta: "))
                if (resp4== 100):
                    print("correcto.")
                    v+=1
                else:
                    print("Erroneo.")
                    v-=1
                    if(v==0):
                        break
            except:
                print("Error en la conexion \n")
        elif (i==5):
            try:
                conexion = psycopg2.connect(     
                    dbname = "preguntados"
                    )
                cursor = conexion.cursor()
                cursor.execute("SELECT * from preguntados where numero =5; ")
                print("Vidas disponibles:"+str(v))
                print (tabulate(cursor, headers= ["pregunta","No."], numalign = "center"))
                resp5=int(input("ingrese su respuesta: "))
                if (resp5== 31):
                    print("correcto.")
                    v+=1
                else:
                    print("Erroneo.")
                    v-=1
                    if(v==0):
                        break
            except:
                print("Error en la conexion \n")
    print("\nUsted finalizó el juego con: "+str(v)+ " vidas\n")

def instrucciones():
    print("\nINSTRUCCIONES:\nAl empezar el juego se le mostrará la cantidad de vidas con las que ud cuenta y con ello viene la primer pregunta a responder,\nsi ud le acierta a la respuesta correcta se le sumará una vida, si ud le falla a la respuesta se le quitará una vida.\nSe le presentarán 5 preguntas en donde puede ganar o perder puntos.\n")

def preguntas():
        try:
            conexion = psycopg2.connect(     
                dbname = "preguntados"
                )
            cursor = conexion.cursor()
            cursor.execute("SELECT * from preguntados; ")
            print (tabulate(cursor, headers= ["pregunta"], tablefmt="psql", numalign = "center"))
        except:
            print("Error en la conexion \n")

opcion = " "
print("Bienvenid@ al juego concurso.")
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'J' Jugar \n'I' Instrucciones \n'P' Ver preguntas \n'Z' salir\n")
    opcion = input("Su elección: ").upper ()
    if opcion == 'J':
        jugar()
    elif opcion =='I':
        instrucciones()
    elif opcion =='P':
        preguntas()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")