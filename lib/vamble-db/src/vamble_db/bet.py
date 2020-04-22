from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from . import base


class Bet(base.Base):
    '''Bet table'''
    __tablename__ = 'bets'

    id = Column(Integer, primary_key=True)

    # Relationships
    bet_condition_id = Column(Integer, ForeignKey('bet_conditions.id'))
    bet_condition = relationship('BetCondition')

    bet_type_id = Column(Integer, ForeignKey('bet_types.id'))
    bet_type = relationship('BetType')

    bet_odds = relationship('BetOdds')

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship('Event', back_populates='bets')


class BetType(base.Base):
    '''BetTypes table'''
    __tablename__ = 'bet_types'

    id = Column(Integer, primary_key=True)

    name = Column(String(100))
    description = Column(String(1000))


class BetOdds(base.Base):
    '''BetOdds table'''
    __tablename__ = 'bet_odds'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    odds = Column(Integer)
    is_plus = Column(Boolean)  # Are odds +(odds), or -(odds)

    # Relationships
    bet_id = Column(Integer, ForeignKey('bets.id'),
                    nullable=False, back_populates='bet_odds')


class BetCondition(base.Base):
    '''Bet Conditions table'''
    __tablename__ = 'bet_conditions'

    id = Column(Integer, primary_key=True)

    name = Column(String(100))
    description = Column(String(1000))


class PlacedBet(base.Base):
    '''PlacedBet table'''
    __tablename__ = 'placed_bets'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    amount = Column(String(100))
    bet_id = Column(Integer, ForeignKey('bets.id'), nullable=False)
    odds_id = Column(Integer, ForeignKey('bet_odds.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
