from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import *
from schemas import UserOutput, UserCreate, ItemCreate
from database import get_db



router = APIRouter(
    prefix="/api/users",
    tags=["items"]
)   

@router.get("/{user_id}/items" )
def get_items_user(user_id: int, db: Session = Depends(get_db)):
    items_user = get_user(db, user_id) 
    if not items_user:                                          ##, response_model=UserOutput
        raise HTTPException(status_code=404, detail="User not found")
    return items_user.items

@router.post("/{user_id}/items")
def create_item(user_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    id_user = get_user(db, user_id)
    if not id_user:
        raise HTTPException(status_code=404, detail="User not found")
    item = create_book(db, item, user_id)
    return item 
 
##pydantic schemas para front-back
##base para subir base de datos 