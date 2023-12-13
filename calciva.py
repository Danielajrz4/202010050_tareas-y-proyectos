import psycopg2
from tabulate import tabulate 

def Historial():
    try:
        conexion = psycopg2.connect(     
            dbname = "tabla_precios"
            )
        cursor = conexion.cursor()
        cursor.execute("SELECT * from tabla_precios; ")
        # for row in cursor:
        #print (row)
        print (tabulate(cursor, headers= ["No. Producto", "Precio"], tablefmt="psql", numalign = "center"))
    except:
        print("Error en la conexion1 \n")


def Post(Numero):
    try:
        conexion = psycopg2.connect(      
            dbname = "tabla_precios"
            )
        cursor = conexion.cursor()
        cursor.execute("insert into tabla_precios(precios) values('"+str(Numero)+"'); ")
        conexion.commit()
        print("número agregado exitosamente \n")
    except:
        print("Error en la conexion2 \n")


def Jugar():
    validez = True
    while validez:
        print ("Ingrese el precio del producto")
        Entrada = input ("Q")
        try:
            Numero = int (Entrada)
            Precio_total=Numero
            IVA=Numero*0.12
            Precio_sin_IVA = Precio_total-IVA
            print("El precio del producto sin iva es de: Q", str (Precio_sin_IVA)," por lo que su IVA es de: Q", str (IVA))
            print("El precio a agregar a la DB es: "+ str(Numero))
            validez=False
            break
        except:
            print ("Ingrese un numero válido. \n")

    return Numero
opcion = " "
print("Bienvenidos al programa 'Calculadora de IVA'")
while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Jugar \n'B' Ver historial \n'Z' salir")
    opcion = input("Su elección: ").upper ()
    if opcion == 'A':
        Numero = Jugar()
        Post(Numero)
    elif opcion=='B':
        Historial ()
    elif opcion=='Z':
        break 
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")