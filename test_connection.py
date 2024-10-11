from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./tasks_db.sqlite"

try:
    # Crear el motor de la base de datos
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    # Probar la conexión
    connection = engine.connect()
    print("Conexión exitosa a la base de datos SQLite")
    connection.close()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
