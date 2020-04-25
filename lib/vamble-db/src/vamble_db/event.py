from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import base


class Event(base.Base):
    '''Event table'''
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(1000))

    # Relationships
    esport_id = Column(Integer, ForeignKey('esports.id'))
    esport = relationship('ESport', back_populates='events')
    children_events = relationship(
        'Event', back_populates='parent_event', remote_side=[id])
    parent_event = relationship('Event', back_populates='children_events')
    parent_event_id = Column(Integer, ForeignKey('events.id'), nullable=True)
    teams = relationship('TeamToEvent')
    bets = relationship('Bet', back_populates='event')


class TeamToEvent(base.Base):
    '''Association table for Team and Event'''
    __tablename__ = 'teams_to_event'

    team_id = Column(Integer, ForeignKey('teams.id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)
    rank = Column(Integer)
