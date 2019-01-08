# GP
A tool to control payments of clients, generate lists, reports, ...

Changelog:

v1.0 - 08/01/2019 A very simple first version working with dictionaries and console.









Notas: 
Si no quieres usar bases de datos (sqlite viene incluida en la biblioteca estándar y es muy sencillo usarla) puedes usar pickle o cpickle para serializar objetos Python.

De esta forma guardas el diccionario en un archivo y al iniciar tu programa lo cargas. Así te evitas leer y parsear manualmente un txt o csv para construir tu diccionario.

Me he tomado la libertad de modificar algunas cosas más en tu código pero la idea del uso de pickle está en dos funciones:

cargar_datos(): intenta abrir el archivo de datos (traducciones.dat). Si existe lo carga y retorna el diccionario de la sesión anterior. Si no existe retorna un diccionario vacío.

guardar_datos(): usa pickle.dump() para guardar el diccionario actual para que esté disponible en futuras sesiones.

El código quedaría:

#!/bin/python3
# -*- coding: utf-8 -*-

import pickle


def repasar(dic):
    for es, ing in dic.items():
        resp = input('Escribe en ingles "{}": '.format(es))
        if resp == ing:
            print ("Correcto.")
        else:
            print ('Incorrecto, es "{}".'.format(ing))

def agregar(dic):
    x = input("Palabra en español: ")
    y = input("Palabra en ingles: ")
    dic[x] = y

def cargar_datos():
    try:
        with open("traducciones.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        return dict()

def guardar_datos(dic):
    with open("traducciones.dat", "wb") as f:
        pickle.dump(dic, f)


def main():
    dic = cargar_datos()
    menu ='''
    1. Repasar.
    2. Añadir palabra.
    3. Guardar y salir.
    '''

    while True:
        print(menu)
        decision = input("¿Que quieres hacer?: ")
        if decision == "1":
            repasar(dic)
        elif decision == "2":
            agregar(dic)
        elif decision == "3":
            guardar_datos(dic)
            break
        else:
            print('Opción inválida, intentelo de nuevo.')

if __name__ == '__main__':
    main()
La opción de sqlite3 es mucho más eficiente si vas a terminar con diccionarios muy grandes. La opción más 'básica' es usar un txt o un csv y construir con el diccionario. Te podrías ayudar del módulo csv para ello, pero eso lo dejo a tu elección.

--------------------------------------------------------------------------------------------------------------------

Diccionarios
febrero 3, 2018 by Recursos Python  2 comentarios


Un diccionario es una colección no ordenada de objetos. Es por eso que para identificar un valor cualquiera dentro de él, especificamos una clave (a diferencia de las listas y tuplas, cuyos elementos se identifican por su posición). Las claves suelen ser números enteros o cadenas, aunque cualquier otro objeto inmutable puede actuar como una clave. Los valores, por el contrario, pueden ser de cualquier tipo, incluso otros diccionarios.

Para crear un diccionario se emplean llaves ({}), y sus pares clave-valor se separan por comas. A su vez, intercalamos la clave del valor con dos puntos (:). Por ejemplo, el siguiente código genera un diccionario cuyas claves son nombres de lenguajes de programación y sus valores, los años en los que fueron creados.

>>> d = {"Python": 1991, "C": 1972, "Java": 1996}
Los diccionarios se crean como instancias de la clase primitiva dict.

>>> type(d)
<class 'dict'>
>>> isinstance(d, dict)
True
Operaciones principales
Para acceder a alguno de los valores se indica su clave correspondiente entre corchetes.

>>> d["Python"]
1991
Y bajo la misma sintaxis le asignamos un nuevo valor.

>>> d["Python"] = 2001
>>> d["Python"]
2001
También de esta forma podemos agregar nuevos elementos.

>>> d["C++"] = 1983
>>> d
{'C++': 1983, 'Java': 1996, 'Python': 2001, 'C': 1972}
Por cuanto las claves actúan como identificadores, no es posible que haya dos iguales (si esto fuese posible Python no sabría cuál de sus valores asociados debería retornar). No obstante, puede haber dos claves (o más) con el mismo valor.

>>> d["JavaScript"] = 1995
>>> d["PHP"] = 1995
Cuando intentamos acceder a una clave inexistente, se lanza la excepción KeyError.

>>> d["Basic"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Basic'
Una forma alternativa para obtener un valor es vía el método get(), indicándo la clave como argumento.

>>> d.get("Python")
1991
De esta forma, cuando la clave no existe el valor retornado es None.

>>> d.get("Elixir") is None
True
O bien cualquier otro objeto que se pase como segundo argumento.

>>> d.get("Elixir", "No existe")
'No existe'
(Véase también Diccionaros con valores por defecto).

La palabra reservada del permite remover un valor.

>>> del d["Python"]
Al iterar un diccionario, éste retorna sus claves.

>>> for key in d:
...     print(key)
...
JavaScript
C++
C
PHP
Java
Para recorrer sus valores, se emplea el método dict.values().

>>> for value in d.values():
...     print(value)
...
1995
1983
1972
1995
1996
Y para recorrer tanto claves como valores simultáneamente:

>>> for key, value in d.items():
...     print(key, value)
...
JavaScript 1995
C++ 1983
C 1972
PHP 1995
Java 1996
Al tratarse de una colección, len() devuelve la cantidad de pares clave-valor que conforman el diccionario.

>>> len(d)
5
Otras operaciones
Para determinar si una clave pertenece a un diccionario, se emplea la palabra reservada in.

>>> "Python" in d
True
El método clear() elimina todas las claves y valores.

>>> d.clear()
>>> d
{}
(Aunque por lo general simplemente se crea un nuevo diccionario vía d = {}).

Podemos actualizar un diccionario ─o bien unir dos de ellos─ vía update().

>>> d = {"Python": 1991, "C": 1972, "Java": 1996}
>>> d2 = {"Elixir": 2011, "Ruby": 1995}
>>> d.update(d2)
>>> d
{'Python': 1991, 'Ruby': 1995, 'C': 1972, 'Java': 1996, 'Elixir': 2011}
La función pop() es similar a get(), pero elimina el elemento una vez retornado.

>>> d = {"Python": 1991, "C": 1972, "Java": 1996}
>>> d.pop("Python")
1991
>>> d
{'C': 1972, 'Java': 1996}
Incluso también soporta devolver un valor por defecto en caso que la clave no exista.

>>> d.pop("Erlang", "No existe")
'No existe'
Por otro lado, popitem() retorna un par clave-valor de forma aleatoria (no podría ser de otra forma pues es una colección no ordenada), y luego lo remueve. Invocar este método en un diccionario vacío lanza KeyError.

>>> d = {"Python": 1991, "C": 1972, "Java": 1996}
>>> d.popitem()
('Python', 1991)
>>> d.popitem()
('C', 1972)
>>> d.popitem()
('Java', 1996)
>>> d.popitem()
Traceback (most recent call last):
   ...
KeyError: 'popitem(): dictionary is empty'
Otras formas de crear diccionarios
Haciendo uso directo de la clase dict Python ofrece algunos métodos para crear diccionarios de formas alternativas (cuyo uso, por cierto, es poco usual).

Si se pasan argumentos por nombre a dict(), constituirán las claves del nuevo diccionario como cadenas.

>>> d = dict(Python=1991, C=1972, Java=1996)
>>> d
{'Python': 1991, 'C': 1972, 'Java': 1996}
(Las razones para emplear este método en oposición al tradicional son, por lo general, puramente estilísticas. Por ejemplo, en el framework de desarrollo web web2py se estila crear diccionarios de esta forma).

Una forma alternativa de representar pares clave-valor es incluyendo tuplas de dos ítems dentro de una lista.

>>> keys_and_values = [
...     ("Python", 1991),
...     ("C", 1972),
...     ("Java", 1996)
... ]
Una lista (o cualquier otro objeto iterable) estructurada de esta manera puede ser pasada directamente como argumento a dict() y devolverá sin reproches el diccionario correspondiente.

>>> d = dict(keys_and_values)
>>> d
{'Python': 1991, 'C': 1972, 'Java': 1996}
El método estático fromkeys() genera un diccionario a partir de un conjunto de claves y les asigna a todas ellas el mismo valor (None por defecto).

>>> dict.fromkeys(["Python", "C", "Java"], 0)
{'Python': 0, 'C': 0, 'Java': 0}
El primer argumento puede ser, de hecho, cualquier objeto iterable.

Métodos obsoletos de Python 2.x
Durante el desarrollo de la versión 3 de Python se pergeñaron algunas modificaciones a los diccionarios que rompen la compatibilidad con versiones anteriores, a saber:

a) El método has_key() que indica si una clave pertenece al diccionario (reemplazado por el operador in).

# ¡¡¡Obsoleto!!!
>>> d.has_key("Python")
True
b) Los métodos keys(), values() e items() solían retornar listas, de modo que recorrer un diccionario muy grande requeriría almacenar primero todas sus claves o valores en la memoria. Para solventar esto, la versión 2.2 introdujo sus equivalentes iterkeys(), itervalues() e iteritems(), que retornan iteradores en su lugar.

>>> d.keys()
['Python', 'C', 'Java']
>>> d.values()
[1991, 1972, 1996]
>>> d.items()
[('Python', 1991), ('C', 1972), ('Java', 1996)]
>>> d.iterkeys()
<dictionary-keyiterator object at 0x01F225A0>
>>> d.itervalues()
<dictionary-valueiterator object at 0x01EDFB40>
>>> d.iteritems()
<dictionary-itemiterator object at 0x01EA25A0>
En Python 3.x los primeros tres métodos retornan iteradores (de hecho se trata de un tipo de objetos particulares llamados View objects), por lo que iterkeys(), itervalues() e iteritems() fueron removidos.

Sobre la implementación
El código que regula la actividad de los diccionarios, como el de cualquier tipo de datos nativo de Python, está escrito en C (al menos en CPython, la implementación oficial del lenguaje). De hecho puedes verlo en el archivo dictobject.c del código de fuente. Esto, sumado a que internamente funcionan como una tabla hash, implica que son altamente eficientes al momento de almacenar y acceder a grandes cantidades de pares clave-valor, por cuanto el tiempo que le toma acceder a una clave se mantiene constante independientemente del número de ellas que contenga.

A partir de Python 3.6 los diccionarios operan internamente como una colección ordenada.

Python >= 3.6Python < 3.6
# Ordenado a partir de Python 3.6.
>>> d = {"Python": 1991, "C": 1972, "Java": 1996}
>>> d
{'Python': 1991, 'C': 1972, 'Java': 1996}

Esta nueva implementación optimiza el rendimiento proveyendo diccionarios hasta dos veces más rápidos. La idea surge en el núcleo de desarrolladores de PyPy y es luego adoptada por CPython. Un artículo del blog oficial de PyPy explica los detalles en este enlace.

No obstante, la clase collections.OrderedDict sigue siendo la opción preferida para garantizar el orden de los elementos de un diccionario, especialmente a través de las distintas versiones de Python. Aún más, el natural orden de las claves a partir de la versión 3.6 debe ser considerado únicamente como una característica de la implementación ─que podría aun cambiar en el futuro─ y no de los diccionarios en sí mismos.


-----------------------------------------------------------------------------------------------------

dict_1 = {}
name = input("What is your name")
dict_1[name] = ["blah", "blah"]
