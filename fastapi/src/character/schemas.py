from pydantic import BaseModel, EmailStr
from typing import Optional, TYPE_CHECKING

# Series
class SeriesBase(BaseModel):
    name: str

class SeriesCreate(SeriesBase):
    pass

class SeriesUpdate(SeriesBase):
    pass

class Series(SeriesBase):
    id: int
    
    model_config = {"from_attributes": True}

# Character
class CharacterBase(BaseModel):
    name: str

class CharacterCreate(CharacterBase):
    series_id: int
    series: Optional[Series] = None

class CharacterUpdate(CharacterBase):
    pass

class Character(CharacterBase):
    id: int
    
    model_config = {"from_attributes": True}

#Shared
class SeriesSimple(BaseModel):
    name: str

class CharacterWithSeries(BaseModel):
    id: int
    name: str
    series: Optional[SeriesSimple] = None

    model_config = {"from_attributes": True}