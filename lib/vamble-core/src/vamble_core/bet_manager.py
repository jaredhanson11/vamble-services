import bcrypt
import logging

from vamble_db.bet import Bet, BetCondition, BetOdds, BetType

logger = logging.getLogger(__name__)


class BetManager:
    '''
    Class for managing Bets
    '''
    session = None  # DB session

    def __init__(self, db_session):
        self.session = db_session

    def get_bets(self):
        '''Get list of all available bets'''
        bets = list(map(self.get_bet_model, self.session.query(Bet).all()))
        return bets

    def get_bet(self, bet_id: int):
        '''Get bet by id'''
        bet = self.session.query(Bet).get(bet_id)
        if bet:
            return self.get_bet_model(bet)

    def get_bet_condition(self, condition_id: int):
        '''Get bet condition by id'''
        condition = self.session.query(BetCondition).get(condition_id)
        if condition:
            return self.get_bet_condition_model(condition)

    def get_bet_odds(self, odds_id: int):
        '''Get bet odds by id'''
        odds = self.session.query(BetOdds).get(odds_id)
        if odds:
            return self.get_bet_odds_model(odds)

    def get_bet_type(self, type_id: int):
        '''Get bet type by id'''
        bet_type = self.session.query(BetType).get(type_id)
        if bet_type:
            return self.get_bet_type_model(bet_type)

    @staticmethod
    def get_bet_model(bet: Bet):
        _bet = {}
        _bet['id'] = bet.id
        _bet['bet_condition_id'] = bet.bet_condition_id
        _bet['bet_type_id'] = bet.bet_type_id
        _bet['event_id'] = bet.event_id

        # BetOdds
        _bet['bet_odds_id'] = None
        if bet.bet_odds[0]:
            _bet['bet_odds_id'] = bet.bet_odds[0].id

        return _bet

    @staticmethod
    def get_bet_condition_model(bet_condition: BetCondition):
        _bet_condition = {}
        _bet_condition['id'] = bet_condition.id
        _bet_condition['name'] = bet_condition.name
        _bet_condition['description'] = bet_condition.description
        return _bet_condition

    @staticmethod
    def get_bet_odds_model(bet_odds: BetOdds):
        _bet_odds = {}
        _bet_odds['id'] = bet_odds.id
        _bet_odds['created_at'] = int(bet_odds.created_at.timestamp())
        _bet_odds['odds'] = bet_odds.odds
        _bet_odds['is_plus'] = bet_odds.is_plus
        _bet_odds['bet_id'] = bet_odds.bet_id
        return _bet_odds

    @staticmethod
    def get_bet_type_model(bet_type: BetType):
        _bet_type = {}
        _bet_type['id'] = bet_type.id
        _bet_type['name'] = bet_type.name
        _bet_type['description'] = bet_type.description
        return _bet_type
