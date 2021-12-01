import csv #importo archivo csv

def f_baja(): #creamos la funcion de baja
    
    #Abro el archivo en modo lectura a agenda cada registro y lo 
    #guardo en un alias, en este caso fila
    #termina la línea que tienes y mueve el cursor a la otra línea.
    with open("agenda.csv","r", newline="\n") as fila: 
        reader = csv.DictReader(fila) #guardamos en la variable reader el flujo de datos iterando con formato de diccionario
        apell = input ("Por Favor, Ingrese Apellido del Registro a Eliminar: ").upper() #pido a quien quiero borrar y lo guardo en una variable,y lo convierto en mayuscula
        agenda_lista = [] #creamo una lista

        for agenda_dic in reader: #recoremos el archivo reguistro por regristro que esta en formato de diccionario
            if apell == agenda_dic["apellido"]: #comparo el apellido ingresado con cada apellido del diccionario
                print("apellido y nombre: ", agenda_dic["apellido"], agenda_dic["nombre"]) #muetra a cada uno con ese apellido

    fila.close()   #cierro el archivo 
   
    #Abro el archivo en modo lectura a agenda cada registro y lo 
    #guardo en un alias, en este caso fila
    #termina la línea que tienes y mueve el cursor a la otra línea.
    with open("agenda.csv","r", newline="\n") as fila: 
   
        reader = csv.DictReader(fila) #guardamos en la variable reader el flujo de datos iterando con formato de diccionario pero en este caso leyendo
        apellido = apell #guardo en una variable el apellido a borrar
        nom = input ("Por Favor Ingrese Nombre del Registro a Eliminar: ").upper() #pido nombre de ese apellido a borrar
        nombres = nom   #lo guardamos en otra variable
        agenda_lista = [] #creo la lista

        for agenda_dic in reader:  #recoremos el archivo reguistro por regristro que esta en formato de diccionario
            #la condicion compara el apellido, nombre diferente a lo que hemos agregado para borrar
            if  apellido != agenda_dic["apellido"] or nombres != agenda_dic["nombre"]: 
                agenda_lista.append(agenda_dic) #agrega todo los diferentes en una lista
                
    fila.close() #cierro el arrchivo
    #Abro el archivo en modo escritura a agenda cada registro y lo 
    #guardo en un alias, en este caso fila
    #termina la línea que tienes y mueve el cursor a la otra línea.
    with open("agenda.csv", "w", newline="\n") as fila:#guardamos en la variable reader el flujo de datos 
        #iterando con formato de diccionario indicandole la llave porque ahora es en forma escritura
        write = csv.DictWriter(fila, agenda_lista[0].keys())
        write.writeheader() # escribo el encabezado
        for agenda_dic in agenda_lista: #recorro la lista
            write.writerow(agenda_dic) #gravo registro por regristro de lo que esta gusrdado en la lista
    fila.close() #cierro el arrchivo