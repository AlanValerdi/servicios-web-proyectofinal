URL_SERVER = "http://127.0.0.1:8000"

def pedir_opcion() -> int:
    while True:
        try:
            return int(input("\n Elige tu opción: \n"))
            
        except ValueError:
            print("\n Debes ingresar numeros validos \n")

def pedir_id(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("El ID debe ser un numero entero")