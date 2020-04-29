'''
Setup all the api routes in add_routes(api) method.
'''
from flask_restful import Api
from .controllers.login import LoginController, SignupController
from .controllers.test import TestController
from .controllers.esport import ESportListController, ESportController
from .controllers.event import EventListController, EventController
from .controllers.bet import BetListController, BetController, \
    BetTypeController, BetOddsController, BetConditionController


def v1_url(path: str) -> str:
    '''Generate full path for v1 url'''
    API_V1_PREFIX = '/api/v1.0'
    return API_V1_PREFIX + path


def add_routes(api: Api):
    '''
    Sets up all the api routes.
    '''
    # Misc
    api.add_resource(TestController, v1_url('/test'))

    # Login/Signup
    api.add_resource(LoginController, v1_url('/login'))
    api.add_resource(SignupController, v1_url('/signup'))

    # Esports
    api.add_resource(ESportListController, v1_url('/esports'))
    api.add_resource(ESportController, v1_url('/esports/<int:id>'))

    # Events
    api.add_resource(EventListController, v1_url('/events'))
    api.add_resource(EventController, v1_url('/events/<int:id>'))

    # Bets + related
    api.add_resource(BetListController, v1_url('/bets'))
    api.add_resource(BetController, v1_url('/bets/<int:id>'))
    api.add_resource(BetOddsController, v1_url('/bets/odds/<int:id>'))
    api.add_resource(BetConditionController,
                     v1_url('/bets/conditions/<int:id>'))
    api.add_resource(BetTypeController, v1_url('/bets/types/<int:id>'))
    # /bets/placed/<id>
