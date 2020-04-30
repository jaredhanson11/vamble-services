import logging

from vamble_db.event import Event, TeamToEvent
from vamble_db.esport import Team

logger = logging.getLogger(__name__)


class EventManager:
    '''
    Class for managing events.
    '''
    session = None  # DB session

    def __init__(self, db_session):
        self.session = db_session

    def get_events(self):
        '''Get all events'''
        events = list(map(lambda event: self.get_event_model(
            event), self.session.query(Event).all()))
        return events

    def get_event(self, event_id: int):
        '''Get event by id'''
        event = self.session.query(Event).get(event_id)
        if event:
            return self.get_event_model(event)

    @staticmethod
    def get_event_model(event: Event):
        '''Get API safe model for event'''
        _event = {}
        _event['id'] = event.id
        _event['name'] = event.name
        _event['description'] = event.description
        _event['esport_id'] = event.esport_id
        _event['children_events_ids'] = list(
            map(lambda e: e.id, event.children_events))
        _event['parent_event_id'] = event.parent_event_id
        _event['teams_ids'] = list(
            map(lambda t2e: EventManager.get_team_to_event_model(t2e),
                event.teams))
        return _event

    @staticmethod
    def get_team_to_event_model(team_to_event: TeamToEvent):
        '''Get API safe model for TeamToEvent'''
        _team_to_event = {}
        _team_to_event['team_id'] = team_to_event.team_id
        _team_to_event['event_id'] = team_to_event.event_id
        _team_to_event['rank'] = team_to_event.rank
        return _team_to_event

class TeamManager:
    '''
    Class for managing events.
    '''
    session = None  # DB session

    def __init__(self, db_session):
        self.session = db_session

    def get_teams(self):
        '''Get all events'''
        teams = list(map(lambda event: self.get_team_model(
            event), self.session.query(Team).all()))
        return teams

    def get_team(self, team_id: int):
        '''Get event by id'''
        team = self.session.query(Team).get(team_id)
        if team:
            return self.get_team_model(team)

    @staticmethod
    def get_team_model(team: Team):
        '''Get API safe model for event'''
        _team = {}
        _team['id'] = team.id
        _team['name'] = team.name
        return _team