import csv
equipos=[]
def validar_puntos(puntos):
    return 0 <= puntos <= 150
def determinar_categoria(puntos):
    if puntos <= 40:
        return "amateur"
    elif puntos <= 80:
        return "intermedio"
    elif puntos <= 120:
        return "avanzado"
    else:
        return "profesional"
def agregar_equipo():
    id_equipo=int(input("Ingrese ID del equipo: "))
    nombre=input("Ingrese el nombre del equipo: ")
    puntos=int(input("Ingrese puntos del equipo: "))
    if validar_puntos(puntos):
        categoria=determinar_categoria(puntos)
        equipos.append({"ID": id_equipo, "Nombre": nombre, "Puntos": puntos, "Categoria": categoria})
        print("Equipo agregado correctamente")
def listar_equipos():
    for equipo in equipos:
        print(f"ID: {equipo['ID']}, Nombre: {equipo['Nombre']}, Puntos: {equipo['Puntos']}, Categoria: {equipo['Categoria']}")
def actualizar_nombre_equipo():
    id_equipo=int(input("Ingrese el ID del equipo que desea actualizar"))
    for equipo in equipos:
        if equipo ["ID"]==id_equipo:
            nuevo_nombre=input("Ingrese el nuevo nombre del equipo: ")
            equipo["Nombre"]=nuevo_nombre
            print("Nombre actualizado correctamente.")
            return
        print("Equipo no encontrado.")
def generar_bbdd():
    with open ('equipo.cvs', mode='w', newline='') as file:
        writer= cvs.DictWriter(file, fieldnames=["ID", "Nombre", "Puntos", "Categoria"])
        writer.writerheader()
        for equipo in equipos:
            writer.writerow(equipo)
            print("BBDD generada correctamente")
def cargar_bbdd():
    global equipos
    equipos=[]
    try:
        with open ('equipos.csv', mode='r' is file):
                   reader= csv.DictReader(file)
                   for row in reader:
                   row["ID"]=int(row["ID"])
                   row["Puntos"]=int(row["Puntos"])
                   equipos.append(row)
                   print("BBDD cargada correctamente.")
                   except FileNotFoundError:
                       print("Archivo no encontrado.")
def puntaje_promedio():
    if equipos:
        total_puntos=su(equipo["Puntos"] for equipo in equipos)
        return total_puntos/len(equipos)
    return 0
def puntaje_mas_alto():
    if equipos:
        equipo_mas_alto=equipo[0]
        for equipo in equipos:
            if equipo["Puntos"]>equipo_mas_alto["Puntos"]:
                equipo_mas_alto=equipo
                return
            equipo_mas_alto["Puntos"], equipo_mas_alto["Nombre"]
            return 0, None
def mostrar_estadisticas():
    promedio=puntaje_promedio()
    maximo=puntaje_mas_alto()
    print(f"Puntaje promedio mas alto: {maximo}")
def menu():
    while True:
        print("1.- Agregar equipo")
        print("2.- Listar equipo")
        print("3.- Actualizar nombre de equipo por id")
        print("4.- Generar BBDD")
        print("5.- Cargar BBDD")
        print("6.- Estadísticas")
        print("0.- Salir")
        op=input("Seleccione una opcion: ")
        if op=="1":
            agregar_equipo()
        elif op=="2":
            listar_equipo()
        elif op=="3":
            actualizar_nombre_equipo()
        elif op=="4":
            generar_bbdd()
        elif op=="5":
            cargar_bbdd()
        elif op=="6":
            mostrar_estdisticas()
        elif op=="0":
            break
        else:
            print("Opcion invalida. Intente nuevamente")
