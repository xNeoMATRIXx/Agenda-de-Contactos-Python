import csv #Importo archivo csv

def f_alta():
    with open("agenda.csv","a", newline="\n") as fila: #Crea un archivo, en modo Escritura, llamado agenda.csv
    
        agenda_lista = [] #se crea una variable vacia, para almacenar informacion
        agenda_dic = {} #se crea un diccionario, para que el usuario ingrese informacion

        agenda_dic["apellido"] = input("ingrese apellido: ").upper() #En cada ingreso, convertimos a mayusculas
        apell = agenda_dic["apellido"]                               #Los Nombres, Apellido, y Direccion
        agenda_dic["nombre"] = input("ingrese nombre: ").upper()
        nom = agenda_dic["nombre"] 
        agenda_dic["tel"] = input("ingrese tel: ")          #ingresamos en cada uno, los datos a requerir por el programa, y lo guardamos
        tele = agenda_dic["tel"]                            #en una variable
        agenda_dic["email"] = input("ingrese email: ")
        correo = agenda_dic["email"] 
        agenda_dic["direccion"] = input("ingrese direccion: ").upper()
        dire = agenda_dic["direccion"]
    
    fila.close() #Cerramos el archivo con los datos almacenados

    with open("agenda.csv","r", newline="\n") as fila: #Abrimos nuevamente, en modo lectura
    
        agenda_lista = [] #Una vez abierto, recibe la informacion anterior previamente ingresada
        reader = csv.DictReader(fila) #Creo un objeto que mapea la información en cada fila,donde lee a traves de cada fila, del diccionario creado
        agenda_lista.append(agenda_dic) #Permite agregar nuevos elementos a la lista en la agenda.
        for agenda_dic in reader: #Recorro cada fila
            
            #Verifico, si los datos ingresados, se encuentran o no en la Agenda
            if apell != agenda_dic["apellido"] or nom != agenda_dic["nombre"] or tele != agenda_dic["tel"] or correo != agenda_dic["email"] or dire != agenda_dic["direccion"]:
                exito = "si"    
            else:
                if apell == agenda_dic["apellido"] and nom == agenda_dic["nombre"] and tele == agenda_dic["tel"] and correo == agenda_dic["email"] and dire == agenda_dic["direccion"]:
                    print("Contacto Existente, Saliendo del Programa")      #Caso contrario, no agrega, y obliga automaticamente al programa regresar al Menu Principal
                    print("Gracias por usar nuestra Agenda")
                    exit()
        if exito == "si":              
            print("Contacto Agreado Exitosamente!")                     #Si, No Existe, lo agrega a la agenda, avisando al usuario con un mensaje   
            print('')        
    fila.close() #Cerramos el archivo con los datos, nuevos, verificados y actualizados

    with open("agenda.csv", "a", newline="\n") as fila: #Abrimos nuevamente, en modo Escritura
        write = csv.DictWriter(fila, agenda_lista[0].keys()) #Crea un objeto que mapea la información donde escribe en cada fila para la devolucion de la informacion
        for agenda_dic in agenda_lista: #Recorro cada elemento, previamente ingresado en la agenda
            write.writerow(agenda_dic) #Escribo la informacion, valida y unica, luego de ser verificado.
    fila.close()