'''
Controller handling session management of users.
'''
import logging

from flask import request, g
from flask_restful import Resource

from vamble_core.account_manager import AccountManager
from vamble_web import responses

from .. import jwt, db

logger = logging.getLogger(__name__)

account_manager: AccountManager = AccountManager(db.session)


class LoginController(Resource):

    @jwt.requires_auth
    def get(self):
        ret = account_manager.get_user(g.user)
        return responses.success(ret, 200)

    def post(self):
        '''
        Attempt to login to you account.
        Sets a cookie with the JWT session token if login successful.
        '''
        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')
        user = account_manager.authenticate_user(email, password)
        jwt_token = jwt.encode_jwt(user.login_id)
        cookie_name = jwt.jwt_cookie_name
        ret = {'token': jwt_token}
        return responses.success(ret, 200, {
            'Set-Cookie': f'{cookie_name}={jwt_token}'
        })

    @jwt.requires_auth
    def delete(self):
        '''Sets empty cookie (to simulate logging out)'''
        cookie_name = jwt.jwt_cookie_name
        ret = 'Successfully logged out.'
        return responses.success(ret, 200, {
            'Set-Cookie': f'{cookie_name}=\'\''''
        })


class SignupController(Resource):
    def post(self):
        '''
        Attempt to signup a new user.
        Sets a cookie with the JWT session token if signup is successful.
        '''
        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')
        user = account_manager.create_new_user(email, password)
        jwt_token = jwt.encode_jwt(user.login_id)
        cookie_name = jwt.jwt_cookie_name
        ret = {'token': jwt_token}
        return responses.success(ret, 201, {
            'Set-Cookie': f'{cookie_name}={jwt_token}'
        })
