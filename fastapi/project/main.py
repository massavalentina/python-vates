from database import engine, Base, get_db
from fastapi import FastAPI, Depends, HTTPException
from crud import *
from schemas import UserOutput
from routers import auth, items


app = FastAPI()

Base.metadata.create_all(bind=engine)                        ##voy a usar de Base, create_all + engine permite la conexion para crear las tablas

                                                
app.include_router(auth.router)
app.include_router(items.router)





