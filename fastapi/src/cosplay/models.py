from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..core.models import Base

# Association table for many-to-many relationship
cosplay_association = Table(
    'cosplay',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('cosplayer_id', Integer, ForeignKey('cosplayer.id'), nullable=False),
    Column('character_version_id', Integer, ForeignKey('character_version.id'), nullable=False),
    Column('created_at', DateTime, default=datetime.utcnow),
    # You can add more fields here like:
    Column('notes', String),
    Column('is_active', Boolean, default=True),
)