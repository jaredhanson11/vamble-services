from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String

from . import base


class User(base.Base):
    '''User table'''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    # login_id = UUID for JWT
    # login_id = Column(String(50), unique=True, default=lambda: str(uuid4()))

    # Login info and stream_key
    # email = Column(String(320), nullable=False, unique=True)
    # password_hash = Column(String(60), nullable=False)

    # Relationships
