'''
Controller handling session management of users.
'''
import logging

from flask import request, g
from flask_restful import Resource

from vamble_core.esport_manager import ESportManager
from vamble_web import responses

from .. import jwt, db

logger = logging.getLogger(__name__)

esport_manager: ESportManager = ESportManager(db.session)


class ESportListController(Resource):
    def get(self):
        '''GET /esports'''
        return responses.success(esport_manager.get_esports())

    def post(self):
    	'''POST /esports'''
    	post_data = request.get_json()
    	name = post_data.get('name')
    	description = post_data.get('description')
    	new_esport = esport_manager.create_esport(name, description)
    	return responses.success(new_esport, 204)


class ESportController(Resource):
    def get(self, id):
        '''GET /esports/id'''
        esport = esport_manager.get_esport(id)
        if esport:
            return responses.success(esport)
        return responses.error('Not found', 404)
