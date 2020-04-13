from . import db
from flask_restful import Resource

from vamble_web import responses
from vamble_core.account_manager import AccountManager


class TestController(Resource):
    '''Test controller'''

    account_manager = AccountManager(db.session)

    def get(self):
        return responses.success({'num': self.account_manager.get_num_users()})

    def post(self):
        return responses.success({'id': self.account_manager.add_user().id})
