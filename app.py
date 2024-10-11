import os
from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from . import models, database, schemas  # Asegúrate de que estas importaciones estén correctas
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from task_manager.schemas import TaskCreate
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .database import SessionLocal
from task_manager.models import Task
  # Asegúrate de que la importación es correcta


app = FastAPI()

# Obtén la ruta absoluta del directorio estático
static_dir = os.path.join(os.path.dirname(__file__), "static")

print(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

#Base.metadata.create_all(bind=engine)

# Crea todas las tablas en la base de datos
models.Base.metadata.create_all(bind=database.engine)

# Configuración de las plantillas
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo a dominios específicos.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TaskCreate(BaseModel):
    title: str
    description: str

# Ruta para la vista principal
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Mi lista de tareas"})


@app.get("/tasks", response_class=HTMLResponse)
async def tasks_view(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return templates.TemplateResponse("task_list.html", {"request": request, "tasks": tasks})



@app.post("/create_task")
async def create_task(task: TaskCreate, db: Session = Depends(database.get_db)):
    # Crea una nueva tarea usando el modelo de SQLAlchemy
    new_task = models.Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "Tarea creada", "task": new_task}


@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

@app.put("/update_task/{task_id}")
async def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    #db = SessionLocal()
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    db.refresh(db_task)
    return {"message": "Tarea actualizada exitosamente", "task": db_task}

@app.delete("/delete_task/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    print(f"Intentando eliminar la tarea con ID: {task_id}")
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        print(f"Tarea con ID {task_id} no encontrada")
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    print(f"Tarea encontrada: {task}")
    db.delete(task)
    db.commit()
    print("Tarea eliminada exitosamente")
    
    return {"message": "Tarea eliminada exitosamente"}


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    task.completed = True
    db.commit()
    db.refresh(task)
    return task
    

