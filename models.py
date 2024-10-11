from sqlalchemy import Column, Integer, String, Boolean
from .database import Base  # Importación relativa


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)  # Nuevo campo


