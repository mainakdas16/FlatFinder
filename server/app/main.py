from typing import Union

from fastapi import FastAPI, Depends
from app.db.database import get_db, Base, engine
from app.db.user import User
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/auth/login")
def login(username: str, db: Session = Depends(get_db)) -> Union[dict, str]:
    user = db.query(User).filter(username == User.username).first()
    created = False
    if not user:
        user = User(username=username)
        db.add(user)
        db.flush()
        db.commit()
        created = True
    return f"you are {'new' if created else 'ancient'} lil {username}"