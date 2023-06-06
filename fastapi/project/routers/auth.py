from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserOutput, UserCreate
from crud import *
from database import get_db



router = APIRouter(
    prefix="/api/users",
    tags=["auth"]
)

@router.get("/")      ##, response_model=UserOutput    ##establece debe retornar (a que me comprometo a devolver)
async def get_all_users(db: Session = Depends(get_db)):      ##db:Session va a ser igual a una dependencia de una funcion (get_db)  ##Depends metodo de fastapi.Permite que mientras use este endpoint voy a tener una sesion de conexion a db abierta
    users_list = get_users(db)                               ##guardo en user_list la lista que me trae el servicio, y por parametro debo pasar una conexion a db
    return users_list

@router.post("/")            ##, response_model=UserOutput
async def create_user_query(user: UserCreate, db: Session = Depends(get_db)):                     
    email_user= get_user_by_email(db, user.email)                                ##se corrobora que no
    if email_user:
        raise HTTPException(status_code=400, detail="Email already registered")  ##siempre tiene un status cod y un detail
    user = post_user(db, user)
    return user


@router.get("/api/users/{user_id}", response_model=UserOutput)                       ##pertnece a la clase UserOutput
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_response = UserOutput(email= user.email, is_active= user.is_active)
    return user_response  