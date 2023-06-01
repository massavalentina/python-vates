# Crear una lista inicial de items
# Campos de items: id(INT), name(STR), description(STR), price(INT), is_offer(BOOL)
#- 1) Crear un CRUD báscio completo (GET, GETxid PUT DELETE DETELExid)
# 2) Get => Obtener todos los items, que se puedan filtrar por estado (en oferta o no) y por limite de precios
# 3) Devolver listado de items filtrado y adicionalmente una leyenda con el porcentaje de items seleccionados
# 4) Get x id => Obtener un item por id y devolver el item SIN el campo de descripcion

from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()



#clase Item
class Item:
    id: int
    name: str
    description: str
    price: int
    is_offer: bool

#constructor que inicializa la clase Item (self referencia a clase(como el this))
    def __init__(self, id, name, description, price, is_offer):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.is_offer = is_offer


#Modelo de Base para la Request (PYDANTICS)
class ItemRequest(BaseModel):
    item_id: Optional[int] = Field(title='id is not required')
    name: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=200)
    price: int = Field(gt=0, lt=1000)
    # is_offer: bool = Field(ge=0, le=1) 

# INITIAL_ITEMS = [{'id':'1', 'name': '', 'description': '', 'price': '14', 'is_offer': 'true'},
#           {'id':'2', 'name': '', 'description': '', 'price': '20', 'is_offer': 'false'},
#           {'id':'3', 'name': '', 'description': '', 'price': '9', 'is_offer': 'false'},
#           {'id':'4', 'name': '', 'description': '', 'price': '23', 'is_offer': 'true'},
#           {'id':'5', 'name': '', 'description': '', 'price': '31', 'is_offer': 'false'}]

INITIAL_ITEMS = [
    Item(1, 'Item 1', 'Item 1 description', 14, True),
    Item(2, 'Item 2', 'Item 2 description', 20, False),
    Item(3, 'Item 3', 'Item 3 description', 9, False),
    Item(4, 'Item 4', 'Item 4 description', 23, True),
    Item(5, 'Item 5', 'Item 5 description', 31, False)
]


##---------- C R U D básico (falta delete general)

@app.get("/items")
async def show_all_items():
    return INITIAL_ITEMS

@app.post("/create-item")
async def create_item(item_request= Body()): 
    INITIAL_ITEMS.append(item_request)

@app.put("/items/update-item")
async def update_item(item: ItemRequest):
    for i in range(len(INITIAL_ITEMS)):
        if INITIAL_ITEMS[i].id == item.id:
            INITIAL_ITEMS[i] = item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int = Path(gt=0)):
    for i in range(len(INITIAL_ITEMS)):
        if INITIAL_ITEMS[i].id == item_id:
            INITIAL_ITEMS.pop(i)

##------------ GET BY ID

@app.get("/items/{item_id}")
async def get_by_id(item_id: int):
    item_by_id = []
    for item in INITIAL_ITEMS:
        if item.get('id').casefold() == item_by_id.casefold():
            item_by_id.append(item)
    return f"Item con id:{id} solicitado"



##---------------------------no se

@app.get("/items/{offer_status}/")
async def get_offer_status_by_query(offer_status : bool, price: int):
    item_by_offer = []
    for item in INITIAL_ITEMS:                                              ##filtro por offer status
        if item.get("is_offer").casefold() == offer_status.casefold() and \
            item.get("price").casefold() == price.casefold():               ##filtro por rango de precio
            item_by_offer.append(item)
            return item_by_offer