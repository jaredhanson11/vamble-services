'''
Controller handling session management of Bets.
'''
import logging

from flask import request, g
from flask_restful import Resource

from vamble_core.bet_manager import BetManager
from vamble_web import responses

from .. import jwt, db

logger = logging.getLogger(__name__)

bet_manager: BetManager = BetManager(db.session)


class BetListController(Resource):
    def get(self):
        '''GET /bets'''
        return responses.success(bet_manager.get_bets())


class BetController(Resource):
    def get(self, id):
        '''GET /bets/<bet_id>'''
        bet = bet_manager.get_bet(id)
        if bet:
            return responses.success(bet)
        return responses.error('Not found', 404)


class BetOddsController(Resource):
    def get(self, id):
        '''GET /bets/odds/<odds_id>'''
        odds = bet_manager.get_bet_odds(id)
        if odds:
            return responses.success(odds)
        return responses.error('Not found', 404)


class BetTypeController(Resource):
    def get(self, id):
        '''GET /bets/types/<type_id>'''
        bet_type = bet_manager.get_bet_type(id)
        if bet_type:
            return responses.success(bet_type)
        return responses.error('Not found', 404)


class BetConditionController(Resource):
    def get(self, id):
        '''GET /bets/conditions/<condition_id>'''
        bet_condition = bet_manager.get_bet_condition(id)
        if bet_condition:
            return responses.success(bet_condition)
        return responses.error('Not found', 404)
