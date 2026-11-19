from menus.utils import URL_SERVER, pedir_opcion, pedir_id

import requests

def mostrar_autor():
    id = pedir_id(" \n Ingresa el ID del autor del que quieres obtner información: \n")

    respuesta = requests.get(f"{URL_SERVER}/autor/{id}")

    if respuesta.status_code == 200:
        print("\n Información del autor: \n", respuesta.json())
    else:
        print(f"\n Error al obtener información: {respuesta.status_code}: ", respuesta.text)

def mostrar_autores():
    respuesta = requests.get(f"{URL_SERVER}/autores")

    if respuesta.status_code == 200:
        print("\n Listado de autores: \n", respuesta.json())
    else:
        print(f"\n Error al obtener información: {respuesta.status_code}: ", respuesta.text)

def crear_autor():
    nombre = input("\n Ingresa el nombre del nuevo autor: \n").strip()
    respuesta = requests.post(f"{URL_SERVER}/autor", json={"nombre": nombre})
    if respuesta.status_code == 200:
        print("\n Autor Creado con éxito \n", respuesta.json())
    else:
        print(f"\n Error al crear {respuesta.status_code}: ", respuesta.text)

def modificar_autor():
    id = pedir_id(" \n Ingresa el ID del autor que quieres modificar: \n")
    nuevo_nombre = input("\n Ingresa el nuevo nombre: \n").strip()

    respuesta = requests.put(f"{URL_SERVER}/autor/{id}", json={"nombre": nuevo_nombre})

    if respuesta.status_code == 200:
        print("\n Autor actualizado con éxito", respuesta.json())
    else:
        print(f"\n Error al modificar autor: {id}, {respuesta.status_code}", respuesta.text)

def eliminar_autor():
    id = pedir_id(" \n Ingresa el ID del autor que quieres eliminar: \n")

    respuesta = requests.delete(f"{URL_SERVER}/autor/{id}")

    if respuesta.status_code == 200:
        print("\n Autor eliminado con éxito", respuesta.json())
    else:
        print(f"\n Error al eliminar autor: {id}, {respuesta.status_code}", respuesta.text)


def mostrar_menu_autor():
    opcion = 0
    while opcion != 6:
        print("\n --- Menú Autor --- \n")
        print(" 1 - Mostrar Autor por ID \n 2 - Mostrar Todos los autores \n 3 - Crear Autor \n 4 - Editar Autor \n 5 - Eliminar Autor \n 6 - Volver al menú principal \n")
        opcion = pedir_opcion()

        if opcion == 1:
            mostrar_autor()
        elif opcion == 2:
            mostrar_autores()
        elif opcion == 3:
            crear_autor()
        elif opcion == 4:
            modificar_autor()
        elif opcion == 5:
            eliminar_autor()