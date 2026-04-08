from sqlalchemy.orm import Session
from . import models
from .utils import hash_password

def create_user(db: Session, email: str, password: str):
    hashed_pwd = hash_password(password)

    new_user = models.User(
        email=email,
        password=hashed_pwd
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()