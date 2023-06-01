from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


## base de datos llamada libros, con dos tablas users e items
URL= "sqlite:///./libros.db"
engine = create_engine(URL, connect_args={'check_same_thread' : False}) ##(crea el motor de db) requiere un valor URL, y variable de sqlalchemy

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine) ##objeto que se al instanciarse crea la conexion a db

Base = declarative_base()  ##permite definir los modelos de la db



def get_db():              ##es una funcion que froma parte con la conformacion de una conexion a base de datos. Momento de conexion en db
    session = SessionLocal()      ##instancia el obj SessionLocal de arriba
    try:
        yield session             ##cuando yo llame a get_db voy a abrir una conexion a db, y cuando salga hace el finally
    finally:                   ## el finally cierra la conexion a la db
        session.close()
        