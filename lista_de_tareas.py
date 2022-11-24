import os
ruta_base = 'C:/Users/Tarde/Desktop/Lista de Tareas/'
archivo = ruta_base + 'trabajo.txt'

def crear_archivo(ruta_archivo):
    open(ruta_archivo, "w+")

def menu(ruta_archivo):
    os.system("cls")
    
    print("""-----------Lista de tareas-----------
    1.-Añade una nueva tarea
    2.-Mostrar lista de tareas
    3.-Modificar lista de tareas
    4.- Eliminar la tarea que quieras
    5.- Crear una nueva lista de tareas (Elimina la actual)
    6.-SUS
    """)
    
    opc1=input("Escriba con un numero lo que quiera realizar: ")
    if opc1=="1":
        insertar_tareas(ruta_archivo)
    elif opc1=="2":
        mostrar_tareas(ruta_archivo)
    elif opc1=="3":
        modificar_tareas(ruta_archivo)
    
    elif opc1=="4":
        borrar_tareas(ruta_archivo)
    elif opc1=="5":
        opc2=input("Estas seguro perderas lo que haya escrito en él (S/N)")
        if opc2.lower()=="s":
            crear_archivo(ruta_archivo)
        elif opc2.lower()=="n":
            menu(ruta_archivo)
    
        else:
            print("Error")
            crear_archivo(ruta_archivo)
    elif opc1=="6":
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀
⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀
⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁""")
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
    menu(ruta_archivo)

def mostrar_tareas(ruta_archivo):
    os.system("cls")
    with open(ruta_archivo, 'r') as fichero:
        print("LISTA DE TAREAS")
        contador=1
        for linea in fichero.readlines():
            print("")
            print(f"{contador}.-{linea}",end='')
            contador+=1

def modificar_tareas(ruta_archivo):
    mostrar_tareas(ruta_archivo)
    pregunta = input("¿Desea modificar el estado de alguna tarea?(S/N)")

    if pregunta.lower() == "s":
        pregunta_2 = int(input("Por favor, especifique el número de la tarea que desee modificar: "))

    d = {}
    with open(archivo, "r") as f:
        for line in f:
            line=line.replace("\n","")
            (key, val) = line.split(" : ")
            d[key] = val
        pregunta_3 = input("Por favor, especifique el estado de la tarea: ")
        list_dict = list(d)
        pregunta_2=pregunta_2-1
        cambio= list_dict[pregunta_2]
        d.update({cambio:pregunta_3})

    with open(ruta_archivo,"w") as f:
        for tarea in d:
            cadena = f"{tarea} : {d[tarea]}\n"
            f.write(cadena)
    menu(ruta_archivo)

def borrar_tareas(ruta_archivo):
    mostrar_tareas(ruta_archivo)
    print("")
    quitar= int(input("Dime una linea que quieras borrar: "))

    with open(ruta_archivo, 'r') as fichero:
            lineas = fichero.readlines()
            
            contador = 1
     

    with open(ruta_archivo, 'w') as fw:
                for linea in lineas:
                    if contador != quitar:
                        fw.write(linea)                    
                    contador += 1
    print("Borrado")
    menu(ruta_archivo)
        
menu(archivo)