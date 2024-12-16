from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar la base de datos
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Crear sesion
Session = sessionmaker(bind=engine)
session = Session()
