#!/usr/bin/env python3

'''
This script tears down and brings up a fresh database for a dev environment.
'''

import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import vamble_db
from vamble_db.bet import Bet, BetType, BetOdds, BetCondition, PlacedBet
from vamble_db.esport import ESport, Team
from vamble_db.event import Event, TeamToEvent
from vamble_db.user import User

from vamble_core.account_manager import AccountManager


# Setup DB
db_uri = sys.argv[1]
db_engine = create_engine(db_uri, echo=True)
Session = sessionmaker(bind=db_engine)
session = Session()

# Setup models
vamble_db.base.Base.metadata.drop_all(db_engine)
vamble_db.base.Base.metadata.create_all(db_engine)

# vamble.user
account_manager = AccountManager(session)
# create User
new_user = account_manager.create_new_user('test@gmail.com', 'password')

# vamble.esport
# create ESport
new_esport = ESport()
new_esport.name = 'NBA 2k20'
new_esport.description = 'Flagship basketball video game'
session.add(new_esport)
session.commit()

# no parent event id, this is a parent
# create Team
teams = []
for i in range(1, 6):
    new_team = Team()
    new_team.name = 'NBA 2k20 Team ' + str(i)
    session.add(new_team)
    session.commit()
    teams.append(new_team)

# vamble.event
# create Event
new_event = Event()
new_event.name = 'NBA 2k20 Season'
new_event.description = 'NBA 2k20 season and all bets on the season'
new_event.esport_id = new_esport.id

for i, team in enumerate(teams):
    new_teamToEvent = TeamToEvent()
    new_teamToEvent.team_id = team.id
    new_teamToEvent.rank = i
    new_event.teams.append(new_teamToEvent)
session.add(new_event)
session.flush()

# create BetType
new_betType = BetType()
new_betType.name = 'Moneyline'
new_betType.description = 'A bet with a binary outcome for which the user is paid as a function of the specified odds'
session.add(new_betType)
session.commit()

# create BetCondition
conditions = []
for i, t2e in enumerate(new_event.teams):
    new_betCondition = BetCondition()
    new_betCondition.name = 'NBA 2k20 Team ' + str(t2e.team_id) + ' Season'
    new_betCondition.description = 'NBA 2k20 Team ' + str(t2e.team_id) + ' wins NBA 2k20 season'
    session.add(new_betCondition)
    session.commit()
    conditions.append(new_betCondition)

# vamble.bet
# create Bet
# in this example, who will win season for each of 5 teams
bets = []
for condition in conditions:
    new_bet = Bet()
    new_bet.bet_condition_id = condition.id
    new_bet.bet_type_id = new_betType.id
    new_bet.event_id = new_event.id
    session.add(new_bet)
    session.commit()
    bets.append(new_bet)

# create BetOdds
for bet in bets:
    new_betOdds = BetOdds()
    new_betOdds.odds = 375
    new_betOdds.is_plus = True
    new_betOdds.bet_id = bet.id
    session.add(new_betOdds)
    session.commit()

# create PlacedBet
for bet in bets:
    new_placedBet = PlacedBet()
    new_placedBet.amount = '1000'
    new_placedBet.bet_id = bet.id
    latest_odds = session.query(BetOdds).filter_by(bet_id=bet.id).order_by(BetOdds.created_at.desc()).first()
    new_placedBet.odds_id = latest_odds.id
    new_placedBet.user_id = 1
    session.add(new_placedBet)
    session.commit()
