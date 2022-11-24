ruta_base = 'C:/Users/Tarde/Desktop/Lista de Tareas/'
archivo = ruta_base + 'trabajo.txt'
d = {}
with open(archivo, "r") as f:
    for line in f:
        line=line.replace("\n","")
        print(line)
        (key, val) = line.split(" : ")
        d[key] = val
        
print (d[4])