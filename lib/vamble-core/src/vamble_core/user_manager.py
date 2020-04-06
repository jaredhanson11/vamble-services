from vamble_db.user import User


class UserManager:
    '''
    Class for managing accounts.
    '''
    session = None  # DB session

    def __init__(self, db_session):
        self.session = db_session

    def get_num_users(self):
        '''TODO remove sample method. Return number of users'''
        return len(list(self.session.query(User).all()))

    def add_user(self):
        '''TODO remove sample method. Return number of users'''
        new_user = User()
        self.session.add(new_user)
        self.session.commit()
        return new_user
