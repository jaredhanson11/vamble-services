import bcrypt
import logging

from vamble_db.user import User

logger = logging.getLogger(__name__)


class AccountManager:
    '''
    Class for managing accounts.
    '''
    PW_SALT = bcrypt.gensalt(rounds=12)
    session = None  # DB session

    def __init__(self, db_session):
        self.session = db_session

    def get_user(self, user_model: User):
        '''Return dict of user record, cleaned of any sensitive data'''
        return self._get_user_model(user_model)

    def create_new_user(self, email, password, f_name=None, l_name=None):
        '''Creates and returns the new user record.'''
        new_user = User()
        new_user.email = email
        new_user.password_hash = self._encrypt_pw(password)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def authenticate_user(self, email, password) -> User:
        '''Returns user if email/password combo is valid, else None'''
        user = self.session.query(User).filter_by(email=email).one()
        if user is not None:
            if self._check_pw(password, user.password_hash):
                return user

    # Private methods #
    def _encrypt_pw(self, password: str) -> str:
        '''Generate salted password hash'''
        hashed = bcrypt.hashpw(str(password).encode('utf-8'), self.PW_SALT)
        return hashed.decode('utf-8')

    def _check_pw(self, password: str, password_hash: str) -> bool:
        '''Check that password and password_hash match'''
        _password = password.encode('utf-8')
        _password_hash = password_hash.encode('utf-8')
        return bcrypt.checkpw(_password, _password_hash)

    def _get_user_model(self, user: User):
        '''Return API safe model for User object'''
        ret: dict = {}
        ret['id'] = user.id
        ret['email'] = user.email
        return ret

    # Sample Methods (to delete) #
    def get_num_users(self):
        '''TODO remove sample method. Return number of users'''
        return len(list(self.session.query(User).all()))

    def add_user(self):
        '''TODO remove sample method. Return number of users'''
        new_user = User()
        self.session.add(new_user)
        self.session.commit()
        return new_user
