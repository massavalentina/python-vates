from crud import *
from database import Base, engine, get_db
from routers import auth, items, test
from schemas import UserOutput

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

Base.metadata.create_all(bind=engine)                        ##voy a usar de Base, create_all + engine permite la conexion para crear las tablas

                                                
app.include_router(auth.router)
app.include_router(items.router)
app.include_router(test.router)





