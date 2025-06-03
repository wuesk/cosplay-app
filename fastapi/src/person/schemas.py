from pydantic import BaseModel, EmailStr
from typing import Optional, TYPE_CHECKING

#Person
class PersonBase(BaseModel):
    username: str
    is_active: bool = True
    is_verified: bool = False
    is_superuser: bool = False

class PersonCreate(PersonBase):
    password: str
    email: EmailStr

class PersonUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_verified: Optional[bool] = None
    is_superuser: Optional[bool] = None

class Person(PersonBase):
    id: int
    
    model_config = {"from_attributes": True}

# Cosplayer
class CosplayerBase(BaseModel):
    instagram: Optional[str] = None
    xitter: Optional[str] = None

class CosplayerCreate(CosplayerBase):
    person_id: int

class CosplayerUpdate(CosplayerBase):
    pass

class Cosplayer(CosplayerBase):
    id: int
    person_id: int
    person: Optional[Person] = None
    
    model_config = {"from_attributes": True}

# Photographer
class PhotographerBase(BaseModel):
    instagram: Optional[str] = None
    xitter: Optional[str] = None
    website: Optional[str] = None

class PhotographerCreate(PhotographerBase):
    person_id: int

class PhotographerUpdate(PhotographerBase):
    pass

class Photographer(PhotographerBase):
    id: int
    person_id: int
    person: Optional[Person] = None
    
    model_config = {"from_attributes": True}

# Shared
class CosplayerSimple(BaseModel):
    instagram: Optional[str] = None
    xitter: Optional[str] = None
    
    model_config = {"from_attributes": True}

class PhotographerSimple(BaseModel):
    instagram: Optional[str] = None
    xitter: Optional[str] = None
    website: Optional[str] = None
    
    model_config = {"from_attributes": True}
    
class PersonWithRoles(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr] = None
    cosplayer: Optional[CosplayerSimple] = None
    photographer: Optional[PhotographerSimple] = None
    
    model_config = {"from_attributes": True}