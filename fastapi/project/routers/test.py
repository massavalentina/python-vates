from typing import Annotated

from crud import *
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from schemas import UserCreate, UserOutput
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

<<<<<<< HEAD
from passlib.context import CryptContext
=======
# from passlib.context import CryptContext
>>>>>>> 1eabee95714cedb80f111b41bce2ac4be0467d60


router = APIRouter(
    prefix="/token",
    tags=["tests"]
)

<<<<<<< HEAD
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

db_dependency = Annotated[Session, Depends(get_db)]  ## [*tipo*, *dependencia(funcion)*]
=======
# bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") // (!) consultar

db_dependency = Annotated[Session, Depends(get_db)]
>>>>>>> 1eabee95714cedb80f111b41bce2ac4be0467d60



def authenticate_user(db: Session, email: str, password: str):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
<<<<<<< HEAD
    if not bcrypt_context.verify(password, user.hashed_password):  ## .verify (metodo de bcrypt_context) verifica que el password sea el mismo que el de la db
                                                                    ## .hash (metodo de bcrypt_context) hashea el password
        raise HTTPException(status_code=400, detail="Incorrect password")
=======
    # if not bcrypt_context.verify(password, user.hashed_password):
    #     raise HTTPException(status_code=400, detail="Incorrect password")
>>>>>>> 1eabee95714cedb80f111b41bce2ac4be0467d60
    return True

##se usa python-multipart para hacer forms 
@router.post("/token")  
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.email, form_data.password, db)
    if not user:
        return 'Failed Authentication'
    return 'Successfull Authentication'