from menus.utils import URL_SERVER, pedir_opcion, pedir_id

import requests
import json

def mostrar_prestamo():
    id = pedir_id(" \n Ingresa el ID del prestamo del que quieres obtener información: \n")

    respuesta = requests.get(f"{URL_SERVER}/prestamo/{id}")

    if respuesta.status_code == 200:
        print("\n Información del prestamo: \n", json.dumps(respuesta.json(), indent=4))
    else:
        print(f"\n Error al obtener información: {respuesta.status_code}: ", respuesta.text)

def mostrar_prestamos():
    respuesta = requests.get(f"{URL_SERVER}/prestamos")

    if respuesta.status_code == 200:
        print("\n Listado de autores: \n", json.dumps(respuesta.json(), indent=4))
    else:
        print(f"\n Error al obtener información: {respuesta.status_code}: ", respuesta.text)

def crear_prestamo():
    usuario = pedir_id("\n Ingresa el id del usuario: \n")
    libro = pedir_id("\n Ingresa el id del libro: \n")
    respuesta = requests.post(f"{URL_SERVER}/prestamo", json={"usuario": usuario, "libro": libro})
    if respuesta.status_code == 200:
        print("\n Prestamo Creado con éxito \n", json.dumps(respuesta.json(), indent=4))
    else:
        print(f"\n Error al crear {respuesta.status_code}: ", respuesta.text)

def renovar_prestamo():
    id = pedir_id(" \n Ingresa el ID del prestamo que quieres modificar: \n")
    
    respuesta = requests.patch(f"{URL_SERVER}/prestamo/{id}/renovar")

    if respuesta.status_code == 200:
        print("\n Prestamo actualizado con éxito", json.dumps(respuesta.json(), indent=4))
    else:
        print(f"\n Error al modificar prestamo: {id}, {respuesta.status_code}", respuesta.text)

def devolver_prestamo():
    id = pedir_id(" \n Ingresa el ID del prestamo que quieres devolver: \n")

    respuesta = requests.patch(f"{URL_SERVER}/prestamo/{id}/devolver")

    if respuesta.status_code == 200:
        print("\n Prestamo devuelto con éxito", json.dumps(respuesta.json(), indent=4))
    else:
        print(f"\n Error al devolver el prestamo: {id}, {respuesta.status_code}", respuesta.text)


def mostrar_menu_prestamo():
    opcion = 0
    while opcion != 6:
        print("\n --- Menú prestamos --- \n")
        print(" 1 - Mostrar prestamo por ID \n 2 - Mostrar Todos los prestamos \n 3 - Crear prestamo \n 4 - Renovar prestamo \n 5 - Devolver prestamo \n 6 - Volver al menú principal \n")
        opcion = pedir_opcion()

        if opcion == 1:
            mostrar_prestamo()
        elif opcion == 2:
            mostrar_prestamos()
        elif opcion == 3:
            crear_prestamo()
        elif opcion == 4:
            renovar_prestamo()
        elif opcion == 5:
            devolver_prestamo()