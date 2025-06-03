import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship
from ..core.models import Base  # Import shared Base
from ..cosplay.models import cosplay_association

class CharacterVersion(Base):
    __tablename__ = 'character_version'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship("Character", back_populates="versions")

    cosplayers = relationship(
        "Cosplayer",
        secondary=cosplay_association,
        back_populates="character_versions"
    )

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    versions = relationship(
        CharacterVersion,
        back_populates="character",
        cascade="all, delete-orphan",
        uselist=True
    )

    series_id = Column(Integer, ForeignKey('series.id'), unique=False)
    series = relationship("Series", back_populates="character")

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    character = relationship(Character, back_populates="series", uselist=True)
    