from sqlalchemy import Column, Integer, String
from db import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    status = Column(String, nullable=False)
