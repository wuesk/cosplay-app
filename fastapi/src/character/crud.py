from sqlalchemy.orm import Session
from . import models, schemas

# Series
def create_series(db: Session, series: schemas.Series):
    db_series = models.Series(
        name=series.name
    )
    db.add(db_series)
    db.commit()
    db.refresh(db_series)
    return db_series

# Characters
def create_character(db: Session, character: schemas.Character):
    db_character = models.Character(
        name=character.name,
        series=character.series
    )
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

def get_character_by_id(db: Session, character_id: int):
    return db.query(models.Character).filter(models.Character.id == character_id).first()