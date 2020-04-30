'''
Controller handling session management of users.
'''
import logging

from flask import request, g
from flask_restful import Resource

from vamble_core.event_manager import EventManager, TeamManager

from vamble_web import responses

from .. import jwt, db

logger = logging.getLogger(__name__)

event_manager: EventManager = EventManager(db.session)
team_manager: TeamManager = TeamManager(db.session)


class EventListController(Resource):
    def get(self):
        '''GET /events'''
        return responses.success(event_manager.get_events())


class EventController(Resource):
    def get(self, id):
        '''GET /events/<id>'''
        event_json = event_manager.get_event(id)
        if event_json:
            return responses.success(event_json)
        return responses.error('Not found.', 404)


class TeamListController(Resource):
	def get(self):
		'''GET /teams'''
		return responses.success(team_manager.get_teams())


class TeamController(Resource):
	def get(self, id):
		'''GET /teams/<id>'''
		team_json = team_manager.get_team(id)
		if team_json:
			return responses.success(team_json)
		return responses.error('Not found.', 404)