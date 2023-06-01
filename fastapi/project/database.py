from sqlalchemy import create_engine
from sqlalchemy.orm import session_maker
from sqlalchemy.ext.declarative import declarative_base

URL= "sqlite:///./libros.db"
engine = create_engine(URL, connect_args={'check_same_thread' : False}) ##(crea el motor de db) requiere un valor URL, y variable de sqlalchemy

SessionLocal = session_maker(autocommit=False, autoflush=False, bind= engine) ##objeto que se al instanciarse crea la conexion a db

Base = declarative_base()