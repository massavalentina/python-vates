from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class UserModel(Base) :
    __tablename__ = "users"                                  
    id = Column(Integer, primary_key=True, index=True)                     ##indexando la tabla con el valor
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
     ##relacion
    items = relationship("ItemModel", back_populates='owner')                   ##relacion entre tablas, el primer parametro es el nombre de la tabla, el segundo parametro es el nombre de la columna


class ItemModel(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)                     ##siempre viene solo                    
    title = Column(String, unique=True, index=True)
    description = Column(String, unique=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))                     ##fk proveniente de la tabla users(el id de la tabla users)
    
    owner = relationship("UserModel", back_populates='items')                   ##relación 



