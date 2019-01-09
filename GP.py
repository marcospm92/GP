#!/usr/bin/env python
# coding: utf-8

# In[41]:


# GP del centro
# v1.1
# 08/01/2019


# In[42]:


# para obtener fecha
import time

# si config = 1, modo consola
config = 1

# si modo_diccionarios = 1, diccionarios .dat reales
# si modo_diccionarios = 0, diccionarios ficticios hardcoded
modo_diccionarios = 0


if modo_diccionarios == 1:
    print("Modo diccionarios .dat reales")
    
elif modo_diccionarios == 0:
    print("Modo diccionarios ficticios")
    # Para poder trabajar con Jupyter creo que tengo que "emular" los diccionarios así, pero
    # HAY QUE IMPLEMENTAR LA PARTE DE LOS .dat
    # diccionario de pacientes y tarifas.
    diccionario_tarifas = {"Nombre1": 90, "Nombre2": 50, "Nombre3": 90, "Nombre4": 50, "Nombre5": 90, "Nombre6": 50}

    # diccionario con diccionarios dentro para los pagos de cada mes. NESTED DICTIONARY
    diccionario_pagos = {"201901": {"Nombre2": [44, "Otro", "01/01/2019"]}}


# In[43]:


#while 1: DESCOMENTAR e INDENTAR
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


# In[44]:


# Entramos al modo NUEVO PAGO
if modo_principal == 1:
    print("Modo seleccionado: Nuevo pago")
    
    # Pido nombre del paciente y compruebo si existe en el diccionario de tarifas
    print("Introduce el nombre del paciente")
    while 1:
        nuevo_pago_nombre = input("Nombre: ")

        if nuevo_pago_nombre in diccionario_tarifas:
            print("Paciente encontrado")
            nuevo_pago_tarifa = diccionario_tarifas.get(nuevo_pago_nombre)
            break
        else:
            print("Paciente no encontrado")
        
    # Confirmo la cantidad pagada del diccionario de tarifas
    print("El paciente tiene asignada una tarifa de", nuevo_pago_tarifa, "€.")
    print("¿Se corresponde esta cifra con el pago?")
    print("1: Sí, el paciente paga", nuevo_pago_tarifa, "€")
    print("2: No, el paciente paga otra cantidad")
    while 1:
        try:
            modo_nuevo_pago_tarifa = int(input())
        except ValueError:
            print ("Debes escribir un número")
        else:
            break    
            
    # La tarifa se corresponde con la del diccionario        
    if modo_nuevo_pago_tarifa == 1:
        print("Cantidad pagada:", nuevo_pago_tarifa, "€")
    
    # La tarifa no se corresponde con la del diccionario
    elif modo_nuevo_pago_tarifa == 2:
        print("Introduce la cantidad pagada")
        while 1:
            try:
                nuevo_pago_tarifa = int(input())
            except ValueError:
                print ("Debes escribir un número")
            else:
                break
        print("Cantidad pagada:", nuevo_pago_tarifa, "€") 
    
    # Error al seleccionar tarifa
    else:
        print("Error al seleccionar la tarifa")        


    # Pregunto método de pago
    print("Introduce la forma de pago")
    print("1: Efectivo")
    print("2: Tarjeta")
    print("3: Otro")
    
    while 1:
        try:
            modo_nuevo_pago_metodo = int(input())
        except ValueError:
            print ("Debes escribir un número")
        else:
            break     
    
    # Pago en efectivo
    if modo_nuevo_pago_metodo == 1:
        print("Pago en efectivo")
        nuevo_pago_metodo = "Efectivo"
        
    # Pago con tarjeta       
    elif modo_nuevo_pago_metodo == 2:
        print("Pago con tarjeta")
        nuevo_pago_metodo = "Tarjeta"
    
    # Otro método de pago
    elif modo_nuevo_pago_metodo == 3:
        print("Pago con otra forma de pago")
        nuevo_pago_metodo = "Otro"
        
    # Error al seleccionar forma de pago
    else:
        print("Error al seleccionar la forma de pago")    
    
    
    # Pregunto si se ha realizado el pago hoy y si no pido fecha
    print("¿Usar la fecha de hoy para el pago?")
    print("1: Sí, usar", time.strftime("%d/%m/%Y"))
    print("2: No, elegir otra fecha")    
    
    while 1:
        try:
            modo_nuevo_pago_fecha = int(input())
        except ValueError:
            print ("Debes escribir un número")
        else:
            break 
    
    # Fecha de hoy 
    if modo_nuevo_pago_fecha == 1:
        print("Fecha escogida:", time.strftime("%d/%m/%Y"))
        nuevo_pago_fecha = time.strftime("%d/%m/%Y")
        nuevo_pago_fecha_anio = time.strftime("%Y")
        nuevo_pago_fecha_mes = time.strftime("%m")
        
    # Otra fecha       
    elif modo_nuevo_pago_fecha == 2:
        print("Introduce la fecha del pago")        
        print("Introduce el día del pago (2 cifras)")
        while 1:
            try:
                nuevo_pago_fecha_dia_tmp = input("Día: ").zfill(2)
                if nuevo_pago_fecha_dia_tmp.isdigit() and int(nuevo_pago_fecha_dia_tmp) > 0 and int(nuevo_pago_fecha_dia_tmp) <=31:
                    nuevo_pago_fecha_dia = nuevo_pago_fecha_dia_tmp
                else:
                    raise ValueError
            except ValueError:
                print ("Debes escribir un número entre 1 y 31")
            else:
                break
                
        print("Introduce el mes del pago (2 cifras)")
        while 1:
            try:
                nuevo_pago_fecha_mes_tmp = input("Mes: ").zfill(2)
                if nuevo_pago_fecha_mes_tmp.isdigit() and int(nuevo_pago_fecha_mes_tmp) > 0 and int(nuevo_pago_fecha_mes_tmp) <=12:
                    nuevo_pago_fecha_mes = nuevo_pago_fecha_mes_tmp
                else:
                    raise ValueError
            except ValueError:
                print ("Debes escribir un número entre 1 y 12")
            else:
                break

        print("Introduce el año del pago (4 cifras)")
        while 1:
            try:
                nuevo_pago_fecha_anio_tmp = input("Año: ").zfill(4)
                if nuevo_pago_fecha_anio_tmp.isdigit() and int(nuevo_pago_fecha_anio_tmp) > 0 and int(nuevo_pago_fecha_anio_tmp) <=9999:
                    nuevo_pago_fecha_anio = nuevo_pago_fecha_anio_tmp
                else:
                    raise ValueError
            except ValueError:
                print ("Debes escribir un número de cuatro cifras")
            else:
                break
        nuevo_pago_fecha = nuevo_pago_fecha_dia + "/" + nuevo_pago_fecha_mes + "/" + nuevo_pago_fecha_anio      
        print("Fecha escogida:", nuevo_pago_fecha)
        
    # Error al seleccionar fecha
    else:
        print("Error al seleccionar la fecha")    
    
    print("Se va a introducir un nuevo pago con los siguientes datos: ")
    print("Nombre: ", nuevo_pago_nombre)
    print("Cantidad: ", nuevo_pago_tarifa)
    print("Forma de pago: ", nuevo_pago_metodo)
    print("Fecha: ", nuevo_pago_fecha)
    print("¿Confirmar?")
    print("1: Sí")
    print("2: No")
    
    while 1:
        try:
            modo_nuevo_pago_confirmar = int(input())
        except ValueError:
            print ("Debes escribir un número")
        else:
            break 
        
    # Confirmar introduccion pago
    if modo_nuevo_pago_confirmar == 1:
        # AQUI HAY QUE CONFIRMAR QUE EL ARCHIVO DEL MES EXISTE
        diccionario_pagos[nuevo_pago_fecha_anio+nuevo_pago_fecha_mes][nuevo_pago_nombre] = [nuevo_pago_tarifa, nuevo_pago_metodo, nuevo_pago_fecha]
        print("Nuevo pago introducido")
        print(diccionario_pagos)
        
    # Cancelar introduccion pago       
    elif modo_nuevo_pago_confirmar == 2:
        print("Nuevo pago cancelado")
        
    # Error al seleccionar confirmacion
    else:
        print("Error al seleccionar confirmación")   
    


        
        
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

        # Menú para preguntar si se quiere ver el diccionario completa de nombres y tarifas o filtrar
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
            for key, value in diccionario_tarifas.items():
                print(key, "\t", value)

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

                if busq in diccionario_tarifas:
                    print("NOMBRE", "\t\t", "TARIFA")
                    print(busq, "\t", diccionario_tarifas.get(busq))
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
                        
                if busq in diccionario_tarifas.values():
                    print("NOMBRE", "\t\t", "TARIFA")
                    for key, value in diccionario_tarifas.items():
                        if value == busq:
                            print(key, "\t", value)
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
    
    while 1:
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
        if modo_nuevo_mes == 1:
            # AQUI DEBEMOS COMPROBAR QUE NO EXISTA EL ARCHIVO DEL MES YA EN EL DICCIONARIO DE PAGOS
            diccionario_pagos[anio+mes] = {}
            print(diccionario_pagos)
            print("Lista del mes", mes, "del año", anio, "creada satisfactoriamente")
            break
            
        elif modo_nuevo_mes == 2:
            print("Escribe el número del mes del que deseas crear la lista (2 cifras)")
            while 1:
                try:
                    mes_tmp = input("Mes: ").zfill(2)
                    if mes_tmp.isdigit() and int(mes_tmp) > 0 and int(mes_tmp) <=12:
                        mes = mes_tmp
                    else:
                        raise ValueError
                except ValueError:
                    print ("Debes escribir un número entre 1 y 12")
                else:
                    break

            print("Escribe el número del año del que deseas crear la lista (4 cifras)")
            while 1:
                try:
                    anio_tmp = input("Año: ").zfill(4)
                    if anio_tmp.isdigit() and int(anio_tmp) > 0 and int(anio_tmp) <=9999:
                        anio = anio_tmp
                    else:
                        raise ValueError
                except ValueError:
                    print ("Debes escribir un número de cuatro cifras")
                else:
                    break
        
# Error al entrar al modo
else:
    print("Error al seleccionar el modo")

print("______________________")


# In[ ]:





# In[ ]:




