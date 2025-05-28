from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..core.models import Base  # Import shared Base

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    series_id = Column(Integer, ForeignKey('series.id'), unique=False)
    series = relationship("Series", back_populates="character")

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    character = relationship(Character, back_populates="series", uselist=True)
    