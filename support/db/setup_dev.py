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


# Setup DB
db_uri = sys.argv[1]
db_engine = create_engine(db_uri, echo=True)
Session = sessionmaker(bind=db_engine)
session = Session()

# Setup models
vamble_db.base.Base.metadata.drop_all(db_engine)
vamble_db.base.Base.metadata.create_all(db_engine)

# vamble.user
# create User
new_user = User()
new_user.email = 'test@gmail.com'
new_user.password_hash = 'asd012ek'
session.add(new_user)
session.commit()

# vamble.esport
# create ESport
new_esport = ESport()
new_esport.name = 'NBA 2k20'
new_esport.description = 'Flagship basketball video game'
session.add(new_esport)
session.commit()

# create Team
for i in range(1,6):
	new_team = Team()
	new_team.name = 'NBA 2k20 Team ' + str(i)
	session.add(new_team)
	session.commit()

# vamble.event
# create Event
new_event = Event()
new_event.name = 'NBA 2k20 Season'
new_event.description = 'NBA 2k20 season and all bets on the season'
new_event.esport_id = 1
# no parent event id, this is a parent

# create TeamToEvent
for i in range(1,6):
	new_teamToEvent = TeamToEvent()
	new_teamToEvent.team_id = i
	new_teamToEvent.event_id = 1
	new_teamToEvent.rank = i
	session.add(new_teamToEvent)
	session.commit()

# vamble.bet
# create Bet
# in this example, who will win season for each of 5 teams
for i in range(1,6):
	new_bet = Bet()
	new_bet.bet_condition_id = i
	new_bet.bet_type_id = 1
	new_bet.event_id = 1
	session.add(new_bet)
	session.commit()

# create BetType
new_betType = BetType()
new_betType.name = 'Moneyline'
new_betType.description = 'A bet with a binary outcome for which the user is paid as a function of the specified odds'
session.add(new_betType)
session.commit()

# create BetOdds
for i in range(1,6):
	new_betOdds = BetOdds()
	new_betOdds.odds = 375
	new_betOdds.is_plus = True
	new_betOdds.bet_id = i
	session.add(new_betOdds)
	session.commit()

# create BetCondition
for i in range(1,6):
	new_betCondition = BetCondition()
	new_betCondition.name = 'NBA 2k20 Team ' + str(i) + ' Season'
	new_betCondition.description = 'NBA 2k20 Team ' + str(i) + ' wins NBA 2k20 season'
	session.add(new_betCondition)
	session.commit()

# create PlacedBet
for i in range(1,6):
	new_placedBet = PlacedBet()
	new_placedBet.amount = '1000'
	new_placedBet.bet_id = i
	new_placedBet.odds_id = i
	new_placedBet.user_id = 1
	session.add(new_placedBet)
	session.commit()