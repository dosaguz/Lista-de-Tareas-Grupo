RUTA_BASE = "/home/pablo/Proyectos/Programación/Tema 2. Funciones/Archivos/"
archivo = RUTA_BASE + "tareas.txt"

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




