from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..core.models import Base  # Import shared Base

class Cosplayer(Base):
    __tablename__ = 'cosplayer'
    id = Column(Integer, primary_key=True)
    instagram = Column(String)
    xitter = Column(String)

    # Relationships
    person_id = Column(Integer, ForeignKey('person.id'), unique=True)
    person = relationship("Person", back_populates="cosplayer")

class Photographer(Base):
    __tablename__ = 'photographer'
    id = Column(Integer, primary_key=True)
    instagram = Column(String)
    xitter = Column(String)
    website = Column(String)

    person_id = Column(Integer, ForeignKey('person.id'), unique=True)
    person = relationship("Person", back_populates="photographer")

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String)
    password_hash = Column(String)

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    cosplayer = relationship(Cosplayer, back_populates="person", uselist=False)
    photographer = relationship(Photographer, back_populates="person", uselist=False)
    