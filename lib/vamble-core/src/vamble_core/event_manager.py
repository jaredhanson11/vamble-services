import logging

from vamble_db.event import Event, TeamToEvent
from vamble_db.esport import Team, ESport

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

    def create_event(self, name, description, esport_name, parent_event_name, team_names, ranks):
        '''Creates and returns a new team record.'''
        new_event = Event()
        new_event.name = name
        new_event.description = description
        # query IDs for esport, parent event
        new_event.esport_id = self.session.query(ESport).filter_by(name=esport_name).first().id
        new_event.parent_event_id = self.session.query(Event).filter_by(name=parent_event_name).first().id
        self.session.add(new_event)
        for i in range(len(team_names)):
            team_name, rank = team_names[i], ranks[i]
            new_team = TeamToEvent()
            new_team.team_id = self.session.query(Team).filter_by(name=team_name).first().id
            new_team.event_id = new_event.id
            new_team.rank = rank
            self.session.add(new_team)
        self.session.commit()
        return self.get_event_model(new_event)

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
    Class for managing teams.
    '''
    session = None  # DB session

    def __init__(self, db_session):
        self.session = db_session

    def get_teams(self):
        '''Get all teams'''
        teams = list(map(lambda team: self.get_team_model(
            team), self.session.query(Team).all()))
        return teams

    def get_team(self, team_id: int):
        '''Get team by id'''
        team = self.session.query(Team).get(team_id)
        if team:
            return self.get_team_model(team)

    def create_team(self, name):
        '''Creates and returns a new team record.'''
        new_team = Team()
        new_team.name = name
        self.session.add(new_team)
        self.session.commit()
        return self.get_team_model(new_team)

    @staticmethod
    def get_team_model(team: Team):
        '''Get API safe model for team'''
        _team = {}
        _team['id'] = team.id
        _team['name'] = team.name
        return _team