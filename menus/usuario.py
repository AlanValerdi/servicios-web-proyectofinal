from menus.utils import URL_SERVER, pedir_opcion, pedir_id

import requests

def crear_usuario():
    nombre = input("\n Ingresa el nombre del nuevo usuario \n").strip()
    password = input("\n Ingresa el password del nuevo usuario \n").strip()
    respuesta = requests.post(f"{URL_SERVER}/usuario", json={"nombre": nombre, "password": password})
    if respuesta.status_code == 200:
        print("Usuario Creado con éxito", respuesta.json())
    else:
        print(f"Error al crear {respuesta.status_code}: ", respuesta.text)

def mostrar_usuario():
    id_usuario = pedir_id(" \n Ingresa el ID del usuario del que quieres obtener información")
    respuesta = requests.get(f"{URL_SERVER}/usuario/{id_usuario}")
    if respuesta.status_code == 200:
        print("Información del usuario:", respuesta.json())
    else:
        print(f"Error al encontrar usuario{respuesta.status_code}:", respuesta.text)


def mostrar_usuarios():
    respuesta = requests.get(f"{URL_SERVER}/usuarios")
    if respuesta.status_code == 200:
        print(f"Listado de usuarios:\n", respuesta.json())
    else:
        print(f"Error al encontrar usuarios {respuesta.status_code}: ", respuesta.text)

def editar_usuario():
    id_usuario = pedir_id(" \n Ingresa el ID del usuario que deseas editar")
    nuevo_nombre =input("\n Ingresa el nombre del usuario \n").strip()
    nueva_password = input("\n Ingresa el password del usuario \n").strip()
    respuesta = requests.put(
        f"{URL_SERVER}/usuario/{id_usuario}",
        json={"nombre": nuevo_nombre, "password": nueva_password}
    )
    if respuesta.status_code == 200:
        print("Usuario editado correctamente", respuesta.json())
    else:
        print(f"Error al modificar usuario {respuesta.status_code}:", respuesta.text)

def eliminar_usuario():
    id_usuario = pedir_id(" \n Ingresa el ID del usuario que deseas eliminar")
    respuesta = requests.delete(f"{URL_SERVER}/usuario/{id_usuario}")
    if respuesta.status_code == 200:
        print("Usuario eliminado", respuesta.json())
    else:
        print(f"Error al eliminar usuario {respuesta.status_code}:", respuesta.text)


def mostrar_menu_usuario():
    opcion = 0
    while opcion != 6:
        print("\n --- Menú Usuario --- \n")
        print(" 1 - Mostrar Usuario por ID \n 2 - Mostrar Todos los usuarios \n 3 - Crear Usuario \n 4 - Editar Usuario \n 5 - Eliminar Usuario \n 6 - Volver al menú principal \n")
        opcion = pedir_opcion()

        if opcion == 1:
            mostrar_usuario()
        elif opcion == 2:
            mostrar_usuarios()
        elif opcion == 3:
            crear_usuario()
        elif opcion == 4:
            editar_usuario()
        elif opcion == 5:
            eliminar_usuario()
        elif opcion == 6:
            print("Volviendo al menu principal")
        else:
            print("Opcion invalida")
