from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import base


class ESport(base.Base):
    '''ESport table'''
    __tablename__ = 'esports'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(1000))

    # Relationships
    events = relationship('Event', back_populates='esport')


class Team(base.Base):
    '''Team table'''

    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
