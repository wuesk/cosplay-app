from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, TYPE_CHECKING

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

# Character version
class CharacterVersionBase(BaseModel):
    name: str

class CharacterVersionCreate(CharacterVersionBase):
    pass

class CharacterVersionUpdate(CharacterVersionBase):
    pass

class CharacterVersion(CharacterVersionBase):
    id: int
    character_id: int
    character: Character

    model_config = {"from_attributes": True}

# Simple schemas for nested responses
class SeriesSimple(BaseModel):
    name: str

class CharacterVersionSimple(BaseModel):
    name: str

# Comprehensive response schema
class CharacterWhole(BaseModel):
    id: int
    name: str
    series: Optional[SeriesSimple] = None
    character_version: List[CharacterVersionSimple] = Field(default_factory=list)

    model_config = {"from_attributes": True}