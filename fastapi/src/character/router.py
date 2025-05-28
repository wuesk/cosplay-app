from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from . import crud, schemas

router = APIRouter(prefix="/character", tags=['characters'])

# Series
@router.post("/series", response_model=schemas.Series, status_code=status.HTTP_201_CREATED)
def create_series(series: schemas.SeriesCreate, db: Session = Depends(get_db)):
    return crud.create_series(db, series)

# Characters
@router.post("/", response_model=schemas.Character, status_code=status.HTTP_201_CREATED)
def create_character(character: schemas.CharacterCreate, db: Session = Depends(get_db)):
    return crud.create_character(db, character)

@router.get("/{character_id}", response_model=schemas.CharacterWithSeries)
def get_character(character_id: int, db: Session = Depends(get_db)):
    db_character = crud.get_character_by_id(db, character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character