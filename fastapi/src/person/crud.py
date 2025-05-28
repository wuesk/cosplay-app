from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Person
def create_person(db: Session, person: schemas.PersonCreate):
    hashed_password = get_password_hash(person.password)
    db_person = models.Person(
        username=person.username,
        email=person.email,
        password_hash=hashed_password,
        is_active=person.is_active,
        is_verified=person.is_verified,
        is_superuser=person.is_superuser
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()

def get_person_by_username(db: Session, username: str):
    return db.query(models.Person).filter(models.Person.username == username).first()

def get_persons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()

def update_person(db: Session, person_id: int, person_update: schemas.PersonUpdate):
    db_person = get_person(db, person_id)
    if db_person:
        update_data = person_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_person, field, value)
        db.commit()
        db.refresh(db_person)
    return db_person

def delete_person(db: Session, person_id: int):
    db_person = get_person(db, person_id)
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person

# Cosplayer
def get_cosplayer(db: Session, cosplayer_id: int):
    return db.query(models.Cosplayer).filter(models.Cosplayer.id == cosplayer_id).first()