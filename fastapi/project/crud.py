##logica de todo
from models import ItemModel, UserModel
from schemas import ItemCreate, UserCreate
from sqlalchemy.orm import Session


def get_users(db: Session):          ##db: algo para que defina como un tipo de dato que pueda recibir  ##objeto del tipo session recibe (coneccion a db abierta) 
    users_db = db.query(UserModel).all()             ##query metodo(consulta) de db. Luego del (UserModel). se pone un meteodo depende lo que quieras traer
    return users_db                                   ##.all() trae todo

def get_user(db: Session, user_id: int):        ##parámetros
    user_id_db = db.query(UserModel).filter(UserModel.id == user_id).first()
        ## abre una consulta query en UserModel, filtra allí el id. first() trae si lo encuentra como primero(sin buscar en todas la info)
    return user_id_db

def get_user_by_email(db: Session, user_email: str):                        ##igual que el de arriba
    user_email_db = db.query(UserModel).filter(UserModel.email == user_email).first()
    return user_email_db

def post_user(db: Session, user: UserCreate):              ##que user se base en el esquema de UserCreate
    fake_pass = user.password + 'fake'             ##contraseña más la palabra fake, para que no sea la pass real la que entre a db
    user_db = UserModel(                           ##crea un objeto de tipo UserModel, con los datos de user
        email=user.email, 
        hashed_password=fake_pass,
        is_active=user.is_active)      ##no hace falta poner esto ya que el valor que trae por default es true, y el user no debe estar activo hasta que lo active por verificacion por email       
    db.add(user_db)                  ## add user a la db
    db.commit()                      ## metodo que guarda los cambios en la db
    db.refresh(user_db)              ## los vuelve a traer
    return user_db
print("User created")

def get_all_books(db:Session):
    books_db = db.query(ItemModel).all()
    return books_db

def create_book(db:Session, book: ItemCreate, owner_id: int):         
    new_book = ItemModel(                          ##crea un obj de tipo ItemModel (declarative base)
        title=book.title,
        description=book.description,
        owner_id=owner_id
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
print("Book created")

################otra opcion para hacerlo

# book_db = ItemModel(**book.dict(), owner_id = owner_id)
# db.add(book_db)
# db.commit()
# db.refresh(book_db)
# return book_db




