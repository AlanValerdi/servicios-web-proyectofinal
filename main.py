from contextlib import asynccontextmanager
from datetime import datetime
from time import process_time_ns

from peewee import Model, CharField, DateTimeField, IntegerField, PrimaryKeyField

from database import database as connection
from database import Usuario, Libro, Prestamo, Autor

from fastapi import FastAPI
from uvicorn import lifespan

from schemas import UsuarioBaseModel

@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    print("El servidor está iniciando...")
    if connection.connect(reuse_if_open=True):
        print("Conexión con la base de datos exitosa")
        # connection.create_tables([Usuario, Libro, Prestamo, Autor])

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


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "API para administrar una libreria"}


# Usuario
@app.post("/usuario")
async def crear_usuario(usuario: UsuarioBaseModel):

    usuario = Usuario.create(
        nombre = usuario.nombre,
        password = usuario.password,
    )

    return {"usuario_id": usuario.id}

