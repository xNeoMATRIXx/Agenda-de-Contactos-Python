# importa cada funcion de los modulos que usaremos
from baja import f_baja
from menuprincipal import fmenuprincipal
from listado import f_listado
from alta import f_alta
from modificacion import f_modificacion

def fopciones():  # creamos la funcion de opciones
    
    while True: #vuelve a mostrar el menu para pedir una opcion hasta q 
                #el usuario desee salir
        
        #guardo en una variable lo q me retorna la funcion asi la uso
        #en los condicionales IF
        OPC = fmenuprincipal()

        #dependiendo que sea OPC sera en que IF ingrese y que hara
        if OPC == "1":
            print()
            print ("AGREGAR UN CONTACTO")
            f_alta()
            print()
        elif OPC == "2":
            print()
            print ("MODIFICAR UN CONTACTO")
            f_modificacion()
            print()
        elif OPC == "3":
            print()
            print ("BORRAR UN CONTACTO")
            f_baja()
            print()
        elif OPC == "4":
            print()
            print ("LISTADO DE LOS CONTACTOS")
            f_listado()
            print()
        elif OPC == "5":
            print ("MUCHAS GRACIAS POR USAR NUESTRA AGENDA, ESPERAMOS NUEVAMENTE SU REGRESO!!")
            exit()
        else:
            print("OPCION INCORRECTA")

 