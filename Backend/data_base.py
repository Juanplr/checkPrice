from sqlmodel import Session, create_engine
from typing import Annotated
from fastapi import Depends
import os
from dotenv import load_dotenv

load_dotenv()

user_db = os.getenv("USER_DB")
password_db = os.getenv("PASSWORD_DB")
host_db = os.getenv("HOST_DB")
port_db = os.getenv("PORT_DB")
name_db = os.getenv("NAME_DB")

url_connection = f"mysql+pymysql://{user_db}:{password_db}@{host_db}:{port_db}/{name_db}"

engine = create_engine(url_connection)

def get_session():
    with Session(engine) as session:
        yield session
        
session_dep = Annotated[Session, Depends(get_session)]