'''
Setup all the api routes in add_routes(api) method.
'''
from flask_restful import Api


def v1_url(path: str) -> str:
    '''Generate full path for v1 url'''
    API_V1_PREFIX = '/api/v1.0'
    return API_V1_PREFIX + path


def add_routes(api: Api):
    '''
    Sets up all the api routes.
    '''
    pass
