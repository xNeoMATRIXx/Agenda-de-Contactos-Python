import csv #importo archivo csv

def f_listado(): #creamos la funcion de lista
    #Abro el archivo en modo lectura a agenda cada registro y lo 
    #guardo en un alias, en este caso fila
    #termina la línea que tienes y mueve el cursor a la otra línea.
    with open("agenda.csv", 'r', newline="\n") as fila:
        reader = csv.DictReader(fila)#guardamos en la variable reader el flujo de datos iterando con formato de diccionario
        for agenda_dic in reader: #con un ciclo for recorremos el archivo, registro por registro
            #muetro cada registro del archivo
            print(agenda_dic["apellido"], 
            agenda_dic["nombre"], 
            agenda_dic["tel"], 
            agenda_dic["email"],
            agenda_dic["direccion"])