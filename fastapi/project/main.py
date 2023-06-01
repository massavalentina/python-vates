from database import engine, Base, get_db
from fastapi import FastAPI, Depends, HTTPException
from crud import *
from schemas import UserOutput



app = FastAPI()

Base.metadata.create_all(bind=engine)   ##voy a usar de Base, create_all + engine permite la conexion para crear las tablas

@app.get("/api/users", response_model= list[UserOutput]) ##establece debe retornar (a que me comprometo a devolver)
async def get_all_users(db: Session = Depends(get_db)): ##db:Session va a ser igual a una dependencia de una funcion (get_db)  ##Depends metodo de fastapi.Permite que mientras use este endpoint voy a tener una sesion de conexion a db abierta
    users_list = get_users(db)  ##guardo en user_list la lista que me trae el servicio, y por parametro debo pasar una conexion a db
    return users_list

@app.post("/api/users", response_model= UserOutput)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):                     
    email_user= get_user_by_email(db, user.email)                                ##se corrobora que no
    if email_user:
        raise HTTPException(status_code=400, detail="Email already registered")  ##siempre tiene un status cod y un detail
    user = create_user(db, user)
    return user
