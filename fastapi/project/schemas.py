from pydantic import BaseModel

##esquemas de modelos para trabajar en pydantic dentro de fastapi
##Modelo de tipo basemodel(pydantic) para crear usuario se definen los tipos de datos como en python(int, str, etc)

class ItemCreate(BaseModel):
    title: str
    description: str
    
    
class Item(ItemCreate):
    id: int
    owner_id: int

class UserOutput(BaseModel):                     ##tipo de obj cuando el cliente pregunt por un usuario
    email: str
    is_active: bool

class UserCreate(UserOutput):                                                       
    password: str
   

class User(UserCreate):                          ##hereda los datos de UserCreate
    id : int
    items: list[Item] = []            ###si no existe la lista de items, devueve una lista vacia                             ##lista de items

    class Config:
        orm_mode = True                           ##toma la clse user  y 1) hace que la clase tenga una relacion con una tabla en la db (contraparte en base para la conexion)




    class Config:
        orm_mode = True










