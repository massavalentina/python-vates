from fastapi import FastAPI, Path, Body
from pydantic import BaseModel 
from typing import Optional, Union

app = FastAPI()

# Crear una clase item que tenga los siguientes datos: nombre, descripcion, precio e impuestos
# la descripcion sea opcional al igual que los impuestos, que el nombre sea str y el precio e 
#impuestos float
#Crear un endpoint de tipo put. Va a recibir un path de tipo int que sea mayor que 0 y menor o igual a 1000
#Va a recibir un query de tipo str y va a recibir un item de tipo item (clase creada)

class Usuario(BaseModel):
    nombre: str
    apellido: str
    edad: int


class Item(BaseModel):
    nombre: str
    # descripcion: Optional[str]
    descripcion: Union[str, None] = None   # "O que sea str o nada(none), se puede mandar sin descripcion"
    # descripcion: str|None = None         # Solo para py de 3.10 para arriba
    precio: int
    impuestos: Union[str, None] = None
    etiqueta: set[str] = set()
    usuario: list[Usuario]

# ! Al ser Item de herencia BaseModel, ya no es necesario crear un constructor
# def __init__(self, nombre, descripcion, precio, impuestos):
#     self.nombre = nombre
#     self.descripcion = descripcion
#     self.precio = precio
#     self.impuestos = impuestos



@app.put("/item/{item_id}/")
async def update_item(item_id: int = Path(gt=0, le= 1000), q: Optional[str] = None, item: Union[Item, None] = None, importancia : str = Body(gt=0, le= 1000)):
# async def update_item(item_id: Annotated[int, Path(gt=0, le=1000)]):   #Con Annotated
    resultado = {
       'item': item_id,
    }
    if q:
       resultado.update({'q' : q})
    if item:
       resultado.update({'item' : item})
    if usuario:
        resultado.update({"usuario" : usuario})
    return resultado
       
    





