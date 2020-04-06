from . import db
from flask_restful import Resource

from vamble_web import responses
from vamble_core.user_manager import UserManager


class TestController(Resource):
    '''Test controller'''

    user_manager = UserManager(db.session)

    def get(self):
        return responses.success({'num': self.user_manager.get_num_users()})

    def post(self):
        return responses.success({'id': self.user_manager.add_user().id})
