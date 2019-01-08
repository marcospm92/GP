#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# GP del centro
# v1.0
# 08/01/2019


# In[ ]:


# para obtener fecha
import time

# si config = 1, modo consola
config = 1

# lista de persona y tarifa. Indices impares personas y el siguiente tarifa asignada. A CAMBIAR POR DICCIONARIO
lista_tarifas = ["Nombre1", 90, "Nombre2", 50]


# In[ ]:


while 1:
    # Pedimos el modo en el que vamos a entrar
    # Primero mostramos un menú con las opciones disponibles
    print("Selección de modo")
    print("Introduce el modo (1-5) en el que quieres entrar y presiona Enter:")
    print("1: Nuevo pago")
    print("2: Consultar datos")
    print("3: Modificar datos")
    print("4: Generar informe")
    print("5: Generar nuevo mes")

    # Recogemos la entrada del usuario
    # Si da error al castear a int es que el dato introducido no es un número, así que lo pedimos de nuevo hasta que sea correcto
    while 1:
        try:
            modo_principal = int(input("Modo: "))
        except ValueError:
            print ("Debes escribir un número")
        else:
            break
    
    
    # Entramos al modo NUEVO PAGO
    if modo_principal == 1:
        print("Modo seleccionado: Nuevo pago")

    # Entramos al modo CONSULTAR DATOS

    elif modo_principal == 2:    
        print("Modo seleccionado: Consultar datos")

        # Menú para preguntar si se quieren consultar tarifas o pagos
        print("Introduce el modo (1-2) en el que quieres entrar y presiona Enter:")
        print("1: Consultar lista de tarifas")
        print("2: Consultar lista de pagos")

        while 1:
            try:
                modo_consultar_datos = int(input("Modo: "))
            except ValueError:
                print ("Debes escribir un número")
            else:
                break

        # Modo LISTA DE TARIFAS
        if modo_consultar_datos == 1:
            print("Modo seleccionado: Lista de tarifas")

            # Menú para preguntar si se quiere ver la lista completa de nombres y tarifas o filtrar
            print("Introduce el modo (1-2) en el que quieres entrar y presiona Enter:")
            print("1: Lista completa de tarifas")
            print("2: Buscar en la lista de tarifas")
            while 1:
                try:
                    modo_lista_tarifas = int(input("Modo: "))
                except ValueError:
                    print ("Debes escribir un número")
                else:
                    break

            # Modo LISTA COMPLETA DE TARIFAS
            if modo_lista_tarifas == 1:
                print("Modo seleccionado: Lista completa de tarifas")
                print("NOMBRE", "\t\t", "TARIFA")
                for i in range(0,len(lista_tarifas)):
                    if i % 2 == 0:
                        print(lista_tarifas[i], "\t", lista_tarifas[i+1])

            # Modo BUSCAR EN LISTA DE TARIFAS
            elif modo_lista_tarifas == 2:    
                print("Modo seleccionado: Buscar en la lista de tarifas")

                print("Introduce el modo (1-2) de búsqueda y presiona Enter:")
                print("1: Nombre")
                print("2: Tarifa")
                while 1:
                    try:
                        modo_lista_tarifas_buscar = int(input("Modo: "))
                    except ValueError:
                        print ("Debes escribir un número")
                    else:
                        break

                # Modo BUSCAR EN LISTA DE TARIFAS POR NOMBRE
                if modo_lista_tarifas_buscar == 1:
                    print("Introduce el nombre exacto a buscar")
                    busq = input("Nombre: ")
                    if busq in lista_tarifas:
                        print("NOMBRE", "\t\t", "TARIFA")
                        print(lista_tarifas[lista_tarifas.index(busq)], "\t", lista_tarifas[lista_tarifas.index(busq)+1])
                    else:
                        print("No hay coincidencias")

                # Modo BUSCAR EN LISTA DE TARIFAS POR TARIFA
                elif modo_lista_tarifas_buscar == 2:
                    print("Introduce la tarifa a buscar en €/mes. Ej: 90")

                    while 1:
                        try:
                            busq = int(input("Tarifa: "))
                        except ValueError:
                            print ("Debes escribir un número")
                        else:
                            break

                    if busq in lista_tarifas:
                        print("NOMBRE", "\t\t", "TARIFA")
                        print(lista_tarifas[lista_tarifas.index(busq)-1], "\t", lista_tarifas[lista_tarifas.index(busq)])
                    else:
                        print("No hay coincidencias")

                # Error al seleccionar modo
                else:
                    print("Error al seleccionar el modo")

            # Error al seleccionar modo
            else:
                print("Error al seleccionar el modo")

        # Modo LISTA DE PAGOS
        elif modo_consultar_datos == 2:
            print("Modo seleccionado: Lista de pagos")

        # Error al seleccionar modo
        else:
            print("Error al seleccionar el modo")

    # Entramos al modo MODIFICAR DATOS

    elif modo_principal == 3:
        print("Modo seleccionado: Modificar datos")

    # Entramos al modo GENERAR INFORME

    elif modo_principal == 4:
        print("Modo seleccionado: Generar informe")

    # Entramos al modo NUEVO MES

    elif modo_principal == 5:
        print("Modo seleccionado: Nuevo mes")
        
        mes = time.strftime("%m")
        anio = time.strftime("%Y")
        
        print("Mes: ", mes)
        print("Año: ", anio)
        print("¿Quieres crear la lista con los datos anteriores?")
        print("1: Sí, crear la lista")
        print("2: No, modificar datos")
        
        while 1:
            try:
                modo_nuevo_mes = int(input("Opción: "))
            except ValueError:
                print ("Debes escribir un número")
            else:
                break        
        
        # Modo GENERAR LISTA NUEVO MES
        #if modo_nuevo_mes == 1:
            # AQUI DEBEMOS COMPROBAR QUE NO EXISTA EL ARCHIVO DEL MES YA
            
        
        
    # Error al entrar al modo

    else:
        print("Error al seleccionar el modo")
    
    print("______________________")


# In[ ]:




