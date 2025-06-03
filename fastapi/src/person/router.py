from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from . import crud, schemas

router = APIRouter(prefix="/persons", tags=["persons"])

@router.post("/", response_model=schemas.Person, status_code=status.HTTP_201_CREATED)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_username(db, username=person.username)
    if db_person:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Username already registered"
        )
    
    if person.email:
        db_person = crud.get_person_by_email(db, email=person.email)
        if db_person:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    return crud.create_person(db=db, person=person)

@router.get("/", response_model=List[schemas.Person])
def read_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_persons(db, skip=skip, limit=limit)

@router.get("/{person_id}", response_model=schemas.PersonWithRoles)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@router.put("/{person_id}", response_model=schemas.Person)
def update_person(person_id: int, person_update: schemas.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.update_person(db, person_id=person_id, person_update=person_update)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@router.delete("/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.delete_person(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")