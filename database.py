from datetime import datetime

from peewee import *
from peewee import BaseModelCursorWrapper

database = MySQLDatabase(
    "libreriadb",
    user="root",
    password="123",
    host="localhost",
    port=3306,
)

class BaseModel(Model):
    class Meta:
        database = database

# Modelos
class Usuario(BaseModel):
    nombre = CharField(max_length=50)
    password = CharField(max_length=50)
    creado_en = DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.nombre}"

class Autor(BaseModel):
    nombre = CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Libro(BaseModel):
    autor = ForeignKeyField(Autor, backref="autor")
    titulo = TextField()
    cantidad = IntegerField()

    def __str__(self):
        return f"{self.autor} {self.titulo}"

class Prestamo(BaseModel):
    usuario = ForeignKeyField(Usuario, backref="prestamos")
    libro = ForeignKeyField(Libro, backref="libro")
    creado_en = DateTimeField(default=datetime.now)
    actualizado_en = DateTimeField(null=True)
    activo = BooleanField(default=True)
    fecha_limite = DateTimeField(null=False)
    fecha_devolucion = DateTimeField(null=True)

    def __str__(self):
        return f"{self.usuario} {self.libro} {self.creado_en}"
