import logging

from vamble_db.esport import ESport

logger = logging.getLogger(__name__)


class ESportManager:
    '''
    Class for managing esports.
    '''
    session = None  # DB session

    def __init__(self, db_session):
        self.session = db_session

    def get_esports(self):
        '''Get all esports'''
        esports = list(map(lambda esport: self.get_esport_model(
            esport), self.session.query(ESport).all()))
        return esports

    def get_esport(self, esport_id):
        '''Get ESport by id'''
        esport = self.session.query(ESport).get(esport_id)
        if esport:
            return self.get_esport_model(esport)

    def create_esport(self, name, description):
        '''Creates and returns a new esport record.'''
        new_esport = ESport()
        new_esport.name = name
        new_esport.description = description
        self.session.add(new_esport)
        self.session.commit()
        return self.get_esport_model(new_esport)


    @staticmethod
    def get_esport_model(esport: ESport):
        '''Get API safe model for esport'''
        _esport = {}
        _esport['id'] = esport.id
        _esport['name'] = esport.name
        _esport['description'] = esport.description
        _esport['events_ids'] = list(
            map(lambda event: event.id, esport.events))
        return _esport
