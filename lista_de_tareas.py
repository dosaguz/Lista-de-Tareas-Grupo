ruta_base = 'C:/Users/Tarde/Desktop/Lista de Tareas/'
archivo = ruta_base + 'trabajo.txt'
def crear_archivo(ruta_archivo):
    with open(ruta_archivo, "w+") as f:
        f.write("""Lista de tareas
        """)

def menu(ruta_archivo):
    
    print("""Lista de tareas
    1.-Añade una nueva tarea
    2.-Mostrar lista de tareas
    3.-Modificar lista de tareas
    4.- Crear nueva lista de tareas (Ejecutar primero en caso de que sea la primera vez que se ejecuta)""")

    opc1=input("Escriba con un numero lo que quiera realizar: ")
    if opc1=="1":
        insertar_tareas(ruta_archivo)
    elif opc1=="2":
        mostrar_tareas(ruta_archivo)
    elif opc1=="3":
        modificar_tareas(ruta_archivo)
    elif opc1=="4":
        opc2=input("Estas seguro perderas lo que haya escrito en él (S/N)")
        if opc2.lower()=="s":
            crear_archivo(ruta_archivo)
        elif opc2.lower()=="n":
            menu(ruta_archivo)
        else:
            print("Error")
            crear_archivo(ruta_archivo)
    else:
        print("Error, vuelva a elegir una opcion")
        print("")
        menu()


def insertar_tareas(ruta_archivo):

    dic = {}

    while True:
        entrada = input("Por favor, introduzca la tarea (Para dejar de introducir tareas, presione la tecla 'intro'): ")
        if entrada == '':
            break
        else:
            entrada = {entrada : "Pendiente"}
            dic.update(entrada)

    with open(ruta_archivo,"a+") as f:
        for tarea in dic:
            cadena = f"{tarea} : {dic[tarea]}\n"
            f.write(cadena)

def mostrar_tareas(ruta_archivo):
    print("Mostrar tareas aquii esta")

def modificar_tareas(ruta_archivo):
    print("Modificar tareas aquii esta")
    
menu(archivo)