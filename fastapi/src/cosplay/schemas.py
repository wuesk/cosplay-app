from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CosplayBase(BaseModel):
    character_version_id: int
    notes: Optional[str] = None
    status: Optional[str] = "planned"

class CosplayCreate(CosplayBase):
    pass

class Cosplay(CosplayBase):
    id: int
    cosplayer_id: int
    created_at: datetime
    
    model_config = {"from_attributes": True}