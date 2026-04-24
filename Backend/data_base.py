from sqlmodel import Session, create_engine
from typing import Annotated
from fastapi import Depends


url_connection = "mysql+pymysql://usercheckprice:Perro16tonto@localhost:3306/checkprice"

engine = create_engine(url_connection)

def get_session():
    with Session(engine) as session:
        yield session
        
session_dep = Annotated[Session, Depends(get_session)]