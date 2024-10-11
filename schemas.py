from pydantic import BaseModel

# Esquema para crear una nueva tarea
class TaskCreate(BaseModel):
    title: str
    description: str

# Esquema para actualizar una tarea existente
class TaskUpdate(BaseModel):
    title: str
    description: str

# Esquema que representa una tarea (tanto para entrada como salida)
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True  # Esto es necesario para que Pydantic funcione bien con SQLAlchemy
