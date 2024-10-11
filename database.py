from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///C:/Users/lisva/OneDrive/Desktop/tasks_db.sqlite"
#SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
                                                                                  

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)

# Crear las tablas en la base de datos
#Base.metadata.create_all(bind=engine)

#from sqlalchemy import inspect

#inspector = inspect(engine)
#print(inspector.get_table_names())




#print(engine.table_names())  # Deprecated en SQLAlchemy 1.4+

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
