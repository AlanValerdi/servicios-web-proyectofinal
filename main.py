from contextlib import asynccontextmanager
from datetime import datetime
from time import process_time_ns

from peewee import Model, CharField, DateTimeField, IntegerField, PrimaryKeyField

from database import database as connection
from database import Usuario, Libro, Prestamo, Autor

from fastapi import FastAPI, HTTPException
from uvicorn import lifespan

from schemas import UsuarioBaseModel, AutorBaseModel

@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    print("El servidor está iniciando...")
    if connection.connect(reuse_if_open=True):
        print("Conexión con la base de datos exitosa")
        connection.create_tables([Usuario, Libro, Prestamo, Autor])

    else:
        print("Algo salió mal con la base de datos")

    yield

    if connection.close():
        print("Se cerró la conexión de base de datos")
    else:
        print("Algo salió mal con la base de datos")
    print( "El servidor está finalizando...")

app = FastAPI(
    title="Proyecto Libreria - Servicios Web",
    description="API para una libreria",
    version="1.0",
    lifespan=ciclo_de_vida,
)

# Deprecado
# @app.on_event("startup")
# @app.on_ecent("shutdown")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "API para administrar una libreria"}


# USUARIO
#FUNCION POST
@app.post("/usuario")
async def crear_usuario(usuario: UsuarioBaseModel):

    usuario = Usuario.create(
        nombre = usuario.nombre,
        password = usuario.password,
    )

    return {"usuario_id": usuario.id}

#FUNCION GET
@app.get("/usuario/{id}")
async def obtener_usuario(id: int):
    usuario = Usuario.get_or_none(Usuario.id == id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"id":usuario.id, "nombre":usuario.nombre}

#FUNCION GET USUARIOS
@app.get("/usuarios")
async def obtener_usuarios():
    usuarios = Usuario.select()

    return [
        {"id": usuario.id, "nombre": usuario.nombre}
        for usuario in usuarios
    ]
#FUNCION PUT
@app.put("/usuario/{id}")
async def actualizar_usuario(id: int,usuario_actualizado: UsuarioBaseModel):
    usuario = Usuario.get_or_none(Usuario.id == id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.nombre = usuario_actualizado.nombre
    usuario.password = usuario_actualizado.password
    usuario.save()

    return {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "mensaje": "Usuario actualizado con exito"
    }
#FUNCION DELETE
@app.delete("/usuario/{id}")
async def eliminar_usuario(id: int):
    usuario = Usuario.get_or_none(Usuario.id == id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.delete_instance()

    return {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "mensaje": "Usuario eliminado con exito"
    }

# Autor
# POST
@app.post('/autor')
async def crear_autor(autor: AutorBaseModel):

    autor = Autor.create(
        nombre = autor.nombre
    )
    return {"id_autor": autor.id ,"nombre_autor": autor.nombre}

# GET
@app.get("/autor/{id}")
async def obtener_autor(id: int):
    autor = Autor.get_or_none(Autor.id == id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return {"id": autor.id, "nombre_autor": autor.nombre}

@app.get("/autores")
async def obtener_autores():
    autores = Autor.select()

    return [
        {"id": autor.id, "nombre": autor.nombre}
        for autor in autores
    ]

# PUT
@app.put("/autor/{id}")
async def actualizar_autor(id: int, autor_actualizado: AutorBaseModel):
    autor = Autor.get_or_none(Autor.id == id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    autor.nombre = autor_actualizado.nombre
    autor.save()

    return {
        "id": autor.id,
        "nombre": autor.nombre,
        "mensaje": "Autor actualizado con exito"
    }

# DELETE
@app.delete("/autor/{id}")
async def eliminar_autor(id: int):
    autor = Autor.get_or_none(Autor.id == id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    autor.delete_instance()

    return {
        "id": autor.id,
        "nombre": autor.nombre,
        "mensaje": "Autor eliminado con exito"
    }


# Libro

