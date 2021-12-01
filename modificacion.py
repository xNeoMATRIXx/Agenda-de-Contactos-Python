import csv #Importo archivo csv
from listado import f_listado #Importo la Funcion Listado

def f_modificacion(): #Creamos la funcion de modificacion

    #Abro el archivo en modo lectura a agenda cada registro y lo 
    #guardo en un alias, en este caso fila
    #termina la línea que tienes y mueve el cursor a la otra línea.
    with open("agenda.csv", 'r', newline="\n") as fila:
    
        agenda_lista = [] #creo una lista
        #guardamos en la variable reader el flujo de datos iterando con formato de diccionario pero en este caso leyendo
        reader = csv.DictReader(fila)
        f_listado() #Llamo a la funcion listado, para que me muestre la lista de contactos.
        print('') #Realizo un espacio en blanco para que quede prolijo
        #pedimos el apellido y nombre y lo pasamos a mayuscula  
        apell = input ("Ingrese Apellido para Modificacion: ").upper()
        nom = input("Ingrese Nombre para Modificacion: ").upper()
        print('') #Realizo un espacio en blanco para que quede prolijo
        #recoremos el archivo reguistro por regristro que esta en formato de diccionario
        for agenda_dic in reader:
            #si el apellido y nombre ingresado son iguales a del archivo entonces sus datos
            if apell == agenda_dic["apellido"] and nom == agenda_dic["nombre"]:
                print(agenda_dic["apellido"], 
                agenda_dic["nombre"], 
                agenda_dic["tel"], 
                agenda_dic["email"],
                agenda_dic["direccion"])
                #y lo agrego en la lista
                agenda_lista.append(agenda_dic)
            
    fila.close() #cierro el archivo

    with open("agenda.csv", 'r', newline="\n") as fila: #abro en el archivo en forma lectura
    
        agenda_lista = [] #En este caso, crea la lista pero recibe los datos previamente guardados anteriormente
        reader = csv.DictReader(fila) #guardamos en la variable reader el flujo de datos iterando con formato de diccionario pero en este caso leyendo
        #guardo mi ingreso de appellido y nombre en variables
        apellido = apell
        nombres = nom
        #Creo un Menu, donde el usuario, ingresara la opcion a modificar
        print('----------------------------------')
        print('|     Menú de Modificación       |')
        print('|                                |')
        print('|        1 - Nombre              |')
        print('|        2 - Telefono            |')
        print('|        3 - Email               |')
        print('|        4 - Dirección           |')
        print('----------------------------------')
        #Obligo al usuario a elegir una opcion para modificar en la agenda, el registro que ingrese
        menuopcio = input("       Ingrese una Opcion: ")
         #recorremos el archivo registro por registro que esta en formato de diccionario
        for agenda_dic in reader:
            #lo voy guardando en la lista
            agenda_lista.append(agenda_dic)
 
    fila.close() #cierro el archivo

    with open("agenda.csv", 'r', newline="\n") as fila: #habro en forma lectura al archivo
    
        agenda_lista = [] #nuevamente crea la lista pero recibe los datos previamente guardados anteriormente
        #guardamos en la variable reader el flujo de datos iterando con formato de diccionario pero en este caso leyendo
        reader = csv.DictReader(fila)
        #dependiendo que elijo en el menu ira comparando cada if y hara lo que este alli en el if
        #en cada if pedira lo respectivo a modificar hara un ciclo para leer todos los registros
        #y lo guardara en la lista, comprobara q lo agregado sea igual y lo cambiara por lo nuevo
        if menuopcio == "1":
            nomb1 = input ("Ingrese Nombre a Modificar: ").upper() 
            nombres1 = nomb1
            for agenda_dic in reader:
                agenda_lista.append(agenda_dic)
                if  apellido == agenda_dic["apellido"] and nombres == agenda_dic["nombre"]: 
                    agenda_dic["nombre"] = nombres1
        elif menuopcio == "2":
            tele = input ("Ingrese Telefono a Modificar: ") 
            telefonos = tele
            for agenda_dic in reader:
                agenda_lista.append(agenda_dic)
                if  apellido == agenda_dic["apellido"] and nombres == agenda_dic["nombre"]: 
                    agenda_dic["tel"] = telefonos
        elif menuopcio == "3":
            correo = input ("Ingrese Email a Modificar: ") 
            correos = correo
            for agenda_dic in reader:
                agenda_lista.append(agenda_dic)
                if  apellido == agenda_dic["apellido"] and nombres == agenda_dic["nombre"]: 
                    agenda_dic["email"] = correos
        elif menuopcio == "4":
            dire = input ("Ingrese Direccion a Modificar: ").upper() 
            direcciones = dire
            for agenda_dic in reader:
                agenda_lista.append(agenda_dic)
                if  apellido == agenda_dic["apellido"] and nombres == agenda_dic["nombre"]: 
                    agenda_dic["direccion"] = direcciones
        else:
            for agenda_dic in reader:
                print("Opcion Incorrecta, Por Favor Ingrese Nuevamente")
                print('')
                exit()
                
    fila.close() #Cerramos el Archivo, ya con el registro actualizado por el usuario
        
    with open("agenda.csv", "w", newline="\n") as fila: #Abrimos nuevamente, en modo Escritura
        write = csv.DictWriter(fila, agenda_lista[0].keys())  #Crea un objeto que mapea la información donde escribe en cada fila para la devolucion de la informacion
        write.writeheader()
        for agenda_dic in agenda_lista: #Recorro cada elemento, previamente ingresado en la agenda
            write.writerow(agenda_dic) #Escribo la informacion, verificado y comparado previamente, luego de su modificacion
    fila.close() #Cerramos el Archivo completamente